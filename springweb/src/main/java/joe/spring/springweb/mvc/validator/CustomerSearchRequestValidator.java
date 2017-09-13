package joe.spring.springweb.mvc.validator;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

import joe.spring.springdomain.CustomerSearchRequest;
import joe.spring.springdomain.GetCustomerByUserNameRequest;
import joe.spring.springweb.mvc.ApiErrorCode;
import joe.spring.springweb.mvc.ApiMessages;

@Component
public class CustomerSearchRequestValidator implements Validator {
		
	protected final static Logger log = LoggerFactory
			.getLogger(CustomerSearchRequestValidator.class);
	

	public CustomerSearchRequestValidator() {
		super();
	}

	@Override
	public boolean supports(Class<?> arg0) {
		return CustomerSearchRequest.class.isAssignableFrom(arg0);
	}

	@Override
	public void validate(Object target, Errors errors) {
		CustomerSearchRequest request = (CustomerSearchRequest) target;

		log.debug("Validating customer search request.");
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "searchTerm", ApiErrorCode.NULL_OR_EMPTY_VALUE.getCode(), ApiMessages.NULL_OR_EMPTY_VALUE_MSG);

		//TODO: Add regex to check for length and composition of username		
	}

}
