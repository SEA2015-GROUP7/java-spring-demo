package joe.spring.springweb.mvc.controller;

import java.util.ArrayList;
import java.util.List;

import javax.validation.Valid;

import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.data.reference.Title;
import joe.spring.springapp.services.CustomerService;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springweb.mvc.data.DropDownData;
import joe.spring.springweb.mvc.data.FormFieldError;
import joe.spring.springweb.mvc.data.ValidationResponse;
import joe.spring.springweb.mvc.model.CustomerModel;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * Handles requests for the form page examples.
 */
@Controller
public class CustomerController {
	@Autowired
	protected CustomerService customerService;
	@Autowired
	protected ReferenceService refService;

	protected final static Logger log = LoggerFactory
			.getLogger(CustomerController.class);

	public CustomerController() {

	}

	// Displays a list of all customers.

	@RequestMapping(value = "/customers")
	public String home() {
		log.info("Displaying the customers page.");

		return "customers";
	}

	@RequestMapping(value = "/getAllCustomers", method = RequestMethod.GET)
	public @ResponseBody
	List<Customer> getCustomers() {
		log.debug("Fetching a list of all customers");
		ArrayList<Customer> customerList = (ArrayList<Customer>) customerService
				.getAllCustomers();
		log.debug("CustomerService.getCustomers() returned "
				+ customerList.size() + " customers.");
		return customerList;
	}

	// ******************************************************************

	// Customer search example. Takes a single search term and searches
	// by customer first, last and user name for matches.

	@RequestMapping(value = "/customerSearch", method = RequestMethod.GET)
	public String displayCustomerSearch() {
		log.info("Displaying customer search page");

		return "customerSearch";
	}

	@RequestMapping(value = "/searchCustomers", method = RequestMethod.POST)
	public @ResponseBody
	List<Customer> searchCustomers(
			@RequestParam(value = "searchTerm", required = false) String searchTerm) {
		log.debug("Searching for customers with searchTerm = " + searchTerm);
		ArrayList<Customer> customerList = (ArrayList<Customer>) customerService
				.searchCustomers(searchTerm);
		log.debug("CustomerService.searchCustomers() returned "
				+ customerList.size() + " customers.");
		return customerList;
	}

	// ******************************************************************

	// Spring MVC example to display a customer form and process a create
	// customer request.

	@RequestMapping(value = "/createCustomer", method = RequestMethod.GET)
	public String displayNewCustomerForm(Model model) {

		model.addAttribute("titleList", getTitleList());
		model.addAttribute("customerModel", new CustomerModel());
		log.info("Displaying the create customer form");

		return "createCustomer";
	}

	@RequestMapping(value = "/createCustomer", method = RequestMethod.POST)
	public String createNewCustomer(@Valid CustomerModel customerModel,
			BindingResult result, Model model) {

		String dest = "createCustomerThanks";
		log.info("CustomerModel:" + customerModel);
		if (result.hasErrors()) {
			log.info("Form validation errors: " + result.getErrorCount());
			model.addAttribute("titleList", getTitleList());
			dest = "createCustomer";
		} else {
			log.info("NO form validation errors found. Creating a new customer!");
			model.addAttribute("firstName", customerModel.getFirstName());
		}
		return dest;
	}

	private List<DropDownData> getTitleList() {
		List<Title> titleList = new ArrayList<Title>();
		List<DropDownData> titleDropDownList = new ArrayList<DropDownData>();
		titleList = refService.getAllTitles();
		for (Title t : titleList) {
			titleDropDownList.add(new DropDownData(t.id(), t.name()));
		}
		return titleDropDownList;
	}

	// ******************************************************************

	// Spring MVC & JQuery example to display a customer form and process a
	// create customer request.

	@RequestMapping(value = "/newCustomer", method = RequestMethod.GET)
	public String displayNewCustomerForm() {
		log.info("Displaying the new customer form");
		return "newCustomerForm";
	}

	@RequestMapping(value = "/newCustomerJson", method = RequestMethod.POST)
	public @ResponseBody
	ValidationResponse createNewCustomerJson(
			@Valid CustomerModel customerModel, BindingResult result,
			Model model) {

		ValidationResponse response = new ValidationResponse();
		log.info("CustomerModel:" + customerModel);
		if (result.hasErrors()) {
			response.setStatus("ERROR");
			List<FormFieldError> errorList = new ArrayList<FormFieldError>();
			log.info("Form validation errors: " + result.getErrorCount());
			for (ObjectError oe : result.getAllErrors()) {
				errorList.add(new FormFieldError(((FieldError) oe).getField(),
						((FieldError) oe).getDefaultMessage()));
				log.info(oe.toString());
			}
			response.setErrorMessageList(errorList);
		} else {
			response.setStatus("OK");
			log.info("NO form validation errors found.");
			// TODO: With no validation errors, time to create a new customer.
		}
		return response;
	}

}