package joe.spring.springweb.mvc.controller;

import java.util.ArrayList;

import javax.validation.Valid;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.MessageSource;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.Validator;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.data.dto.DtoConverter;
import joe.spring.springapp.services.CustomerService;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springapp.services.ServiceException;
import joe.spring.springdomain.CreateCustomerRequest;
import joe.spring.springdomain.CustomerDto;
import joe.spring.springdomain.CustomerDtoList;
import joe.spring.springdomain.CustomerResponse;
import joe.spring.springdomain.CustomerSearchRequest;
import joe.spring.springdomain.CustomersResponse;
import joe.spring.springdomain.DeleteAllCustomersResponse;
import joe.spring.springdomain.DeleteCustomerRequest;
import joe.spring.springdomain.DeleteCustomerResponse;
import joe.spring.springdomain.GetCustomerByUserNameRequest;
import joe.spring.springdomain.RequestStatus;
import joe.spring.springweb.mvc.ApiException;
import joe.spring.springweb.mvc.ApiMessages;

/**
 * Handles requests for the form page examples.
 */
@RestController
@RequestMapping("api/customer")
public class CustomerServiceController {

	@Autowired
	protected CustomerService customerService;

	@Autowired
	protected ReferenceService refService;

	@Autowired
	protected MessageSource messageSource;

	protected final static Logger log = LoggerFactory.getLogger(CustomerServiceController.class);

	@Autowired
	@Qualifier("createCustomerValidator")
	private Validator createCustomerValidator;

	@Autowired
	@Qualifier("deleteCustomerValidator")
	private Validator deleteCustomerValidator;

	@InitBinder("createCustomerRequest")
	public void setupCreateCustomerBinder(WebDataBinder binder) {
		binder.addValidators(createCustomerValidator);
	}

	@InitBinder("deleteCustomerRequest")
	public void setupDeleteCustomerBinder(WebDataBinder binder) {
		binder.addValidators(deleteCustomerValidator);
	}

	public CustomerServiceController() {

	}

	@RequestMapping(value = "/v1/createCustomer", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<CustomerResponse> createCustomer(@Valid @RequestBody CreateCustomerRequest request)
			throws ApiException {
		log.info("In createCustomer...");
		CustomerResponse response = new CustomerResponse();

		Customer customer = null;

		try {
			customer = customerService.getCustomerByUserName(request.getUserName());
			if (customer == null) {
				customer = customerService.createCustomer(request.getFirstName(), request.getLastName(),
						request.getUserName(), request.getBirthDate().getTime(), request.getPassword());
				if (customer != null) {
					response.setCustomer(DtoConverter.toCustomerDto(customer));
				} else {
					throw new ApiException("Customer returned null from createCustomer().");
				}
			} else {
				throw new ApiException(ApiMessages.USERNAME_EXISTS_MSG);
			}
		} catch (ServiceException e) {
			log.error("ServiceException thrown while creating customer.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
		return new ResponseEntity<>(response, HttpStatus.OK);
	}

	@RequestMapping(value = "/v1/getCustomerByUserName", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<CustomerResponse> getCustomerByUserName(@RequestBody GetCustomerByUserNameRequest request)
			throws ApiException {
		CustomerResponse response = new CustomerResponse();

		log.debug("Searching for customer with user name = " + request.getUserName());
		Customer customer = null;
		try {
			customer = customerService.getCustomerByUserName(request.getUserName());
			if (customer != null) {
				CustomerDto customerDto = DtoConverter.toCustomerDto(customer);
				response.setCustomer(customerDto);
			}
		} catch (ServiceException e) {
			log.error("ServiceException thrown while getting customer by user name.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
		return new ResponseEntity<>(response, HttpStatus.OK);
	}

	@RequestMapping(value = "/v1/getAllCustomers", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<CustomersResponse> getAllCustomers() throws ApiException {
		CustomersResponse response = new CustomersResponse();

		log.debug("Getting all customers");
		ArrayList<Customer> customerList = null;
		try {
			customerList = (ArrayList<Customer>) customerService.getAllCustomers();
			CustomerDtoList customers = new CustomerDtoList();
			customers.getCustomers().addAll(DtoConverter.toCustomerDtoList(customerList));
			response.setCustomers(customers);
		} catch (ServiceException e) {
			log.error("ServiceException thrown while getting all customers.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
		return new ResponseEntity<>(response, HttpStatus.OK);
	}

	@RequestMapping(value = "/v1/customerSearch", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<CustomersResponse> searchForCustomers(@RequestBody CustomerSearchRequest request)
			throws ApiException {
		CustomersResponse response = new CustomersResponse();

		log.debug("Searching for customers with searchTerm = " + request.getSearchTerm());
		ArrayList<Customer> customerList = null;
		try {
			customerList = (ArrayList<Customer>) customerService.searchCustomers(request.getSearchTerm());
			log.debug("CustomerService.searchCustomers() returned " + customerList.size() + " customers.");
			CustomerDtoList customers = new CustomerDtoList();
			customers.getCustomers().addAll(DtoConverter.toCustomerDtoList(customerList));
			response.setCustomers(customers);
		} catch (ServiceException e) {
			log.error("ServiceException thrown during customer search.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
		return new ResponseEntity<>(response, HttpStatus.OK);
	}

	@RequestMapping(value = "/v1/deleteCustomer", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<DeleteCustomerResponse> deleteCustomer(
			@Valid @RequestBody DeleteCustomerRequest deleteCustomerRequest) throws ApiException {
		DeleteCustomerResponse response = new DeleteCustomerResponse();
		response.setStatus(RequestStatus.ERROR);

		log.debug("Searching for customer with user name = " + deleteCustomerRequest.getUserName());
		Customer customer = null;
		try {
			customer = customerService.getCustomerByUserName(deleteCustomerRequest.getUserName());
			if (customer != null) {
				customerService.removeCustomer(customer.getId());
				response.setStatus(RequestStatus.OK);
			}
		} catch (ServiceException e) {
			log.error("ServiceException thrown during delete customer.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
		return new ResponseEntity<>(response, HttpStatus.OK);
	}

	@RequestMapping(value = "/v1/deleteAllCustomers", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<DeleteAllCustomersResponse> deleteAllCustomers() throws ApiException {
		DeleteAllCustomersResponse response = new DeleteAllCustomersResponse();
		response.setStatus(RequestStatus.ERROR);

		log.debug("Deleting all customers");
		try {
			customerService.removeAllCustomers();
			response.setStatus(RequestStatus.OK);
		} catch (ServiceException e) {
			log.error("ServiceException thrown during delete all customers.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
		return new ResponseEntity<>(response, HttpStatus.OK);
	}

}