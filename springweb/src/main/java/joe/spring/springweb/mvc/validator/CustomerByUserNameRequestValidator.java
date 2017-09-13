package joe.spring.springweb.mvc.validator;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

import joe.spring.springdomain.GetCustomerByUserNameRequest;
import joe.spring.springweb.mvc.ApiErrorCode;
import joe.spring.springweb.mvc.ApiMessages;

@Component
public class CustomerByUserNameRequestValidator implements Validator {
	
//	@Autowired
//	private CustomerService customerService;
	
	protected final static Logger log = LoggerFactory
			.getLogger(CustomerByUserNameRequestValidator.class);
	

	public CustomerByUserNameRequestValidator() {
		super();
	}

	@Override
	public boolean supports(Class<?> arg0) {
		return GetCustomerByUserNameRequest.class.isAssignableFrom(arg0);
	}

	@Override
	public void validate(Object target, Errors errors) {
		GetCustomerByUserNameRequest request = (GetCustomerByUserNameRequest) target;

		log.debug("Validating create customer request.");
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "userName", ApiErrorCode.NULL_OR_EMPTY_VALUE.getCode(), ApiMessages.NULL_OR_EMPTY_VALUE_MSG);

		//TODO: Add regex to check for length and composition of username
		
//		if (!errors.hasErrors()) {
//			try {
//				Customer c = customerService.getCustomerByUserName(request.getUserName());
//				if (c != null) {
//					errors.reject(ApiErrorCode.USERNAME_EXISTS.getCode(), ApiMessages.USERNAME_EXISTS_MSG);
//				}
//			} catch (ServiceException e) {
//				log.error("An exception occurred while looking up customer for create. Username: " + request.getUserName(), e);
//				errors.reject(ApiErrorCode.SERVICE_EXCEPTION.getCode(), ApiMessages.SERVICE_EXCEPTION_MSG);
//			}
//		}		
	}

}
