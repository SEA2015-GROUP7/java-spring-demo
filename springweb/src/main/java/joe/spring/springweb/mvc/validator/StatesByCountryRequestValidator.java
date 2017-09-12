package joe.spring.springweb.mvc.validator;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

import joe.spring.springapp.data.reference.Country;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springapp.services.ServiceException;
import joe.spring.springdomain.StatesByCountryRequest;
import joe.spring.springweb.mvc.ApiErrorCode;
import joe.spring.springweb.mvc.ApiMessages;

@Component
public class StatesByCountryRequestValidator implements Validator {
	
	@Autowired
	private ReferenceService refDataService;
	
	protected final static Logger log = LoggerFactory
			.getLogger(StatesByCountryRequestValidator.class);
	

	public StatesByCountryRequestValidator() {
		super();
	}

	@Override
	public boolean supports(Class<?> arg0) {
		return StatesByCountryRequest.class.isAssignableFrom(arg0);
	}

	@Override
	public void validate(Object target, Errors errors) {
		StatesByCountryRequest request = (StatesByCountryRequest) target;

		log.debug("Validating country code " + request.getCountryCode());
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "countryCode", ApiErrorCode.NULL_OR_EMPTY_VALUE.getCode(), ApiMessages.NULL_OR_EMPTY_VALUE_MSG);
		if (!errors.hasErrors()) {
			Country c;
			try {
				c = refDataService.getCountryByCode(request.getCountryCode());
				if (c == null) {
					errors.reject(ApiErrorCode.UNKNOWN_COUNTRY_CODE.getCode(), ApiMessages.UNKNOWN_COUNTRY_CODE_MSG);				
				}
			} catch (ServiceException e) {
				e.printStackTrace();
				errors.reject(ApiErrorCode.SERVICE_EXCEPTION.getCode(), ApiMessages.SERVICE_EXCEPTION_MSG);				
			}
		}
		
	}

}
