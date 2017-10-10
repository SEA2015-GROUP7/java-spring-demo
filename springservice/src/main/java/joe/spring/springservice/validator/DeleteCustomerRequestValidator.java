package joe.spring.springservice.validator;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.services.CustomerService;
import joe.spring.springapp.services.ServiceException;
import joe.spring.springdomain.DeleteCustomerRequest;
import joe.spring.springservice.ApiErrorCode;
import joe.spring.springservice.ApiMessages;

@Component
public class DeleteCustomerRequestValidator implements Validator {
	
	@Autowired
	private CustomerService customerService;
	
	protected final static Logger log = LoggerFactory
			.getLogger(DeleteCustomerRequestValidator.class);
	

	public DeleteCustomerRequestValidator() {
		super();
	}

	@Override
	public boolean supports(Class<?> arg0) {
		return DeleteCustomerRequest.class.isAssignableFrom(arg0);
	}

	@Override
	public void validate(Object target, Errors errors) {
		DeleteCustomerRequest request = (DeleteCustomerRequest) target;

		log.debug("Validating delete customer request.");
		
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "userName", ApiErrorCode.NULL_OR_EMPTY_VALUE.getCode(), ApiMessages.NULL_OR_EMPTY_VALUE_MSG);
		
		if (!errors.hasErrors()) {
			try {
				Customer c = customerService.getCustomerByUserName(request.getUserName());
				if (c == null) {
					errors.reject(ApiErrorCode.CUSTOMER_DOES_NOT_EXIST.getCode(), ApiMessages.CUSTOMER_DOES_NOT_EXIST_MSG);
				}
			} catch (ServiceException e) {
				log.error("An exception occurred while looking up customer for delete. Username: " + request.getUserName(), e);
				errors.reject(ApiErrorCode.SERVICE_EXCEPTION.getCode(), ApiMessages.SERVICE_EXCEPTION_MSG);
			}
		}
	}

}
