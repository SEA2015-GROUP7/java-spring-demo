package joe.spring.springservice.validator;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;

import joe.spring.springapp.data.reference.State;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springapp.services.ServiceException;
import joe.spring.springdomain.StateByCodeRequest;
import joe.spring.springservice.ApiErrorCode;
import joe.spring.springservice.ApiMessages;

@Component
public class StateByCodeRequestValidator implements Validator {
	
	@Autowired
	private ReferenceService refDataService;
	
	protected final static Logger log = LoggerFactory
			.getLogger(StateByCodeRequestValidator.class);
	

	public StateByCodeRequestValidator() {
		super();
	}

	@Override
	public boolean supports(Class<?> arg0) {
		return StateByCodeRequest.class.isAssignableFrom(arg0);
	}

	@Override
	public void validate(Object target, Errors errors) {
		StateByCodeRequest request = (StateByCodeRequest) target;

		log.debug("Validating state code " + request.getStateCode());
		ValidationUtils.rejectIfEmptyOrWhitespace(errors, "stateCode", ApiErrorCode.NULL_OR_EMPTY_VALUE.getCode(), ApiMessages.NULL_OR_EMPTY_VALUE_MSG);
		if (!errors.hasErrors()) {
			State s;
			try {
				s = refDataService.getStateByCode(request.getStateCode());
				if (s == null) {
					errors.reject(ApiErrorCode.UNKNOWN_STATE_CODE.getCode(), ApiMessages.UNKNOWN_STATE_CODE_MSG);				
				}
			} catch (ServiceException e) {
				e.printStackTrace();
				errors.reject(ApiErrorCode.SERVICE_EXCEPTION.getCode(), ApiMessages.SERVICE_EXCEPTION_MSG);				
			}
		}
		
	}

}
