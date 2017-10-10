package joe.spring.springservice.handler;

import java.util.ArrayList;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

import joe.spring.springdomain.ApiFieldError;
import joe.spring.springdomain.ApiGlobalError;
import joe.spring.springdomain.ErrorResponse;
import joe.spring.springservice.ApiErrorCode;
import joe.spring.springservice.ApiException;
import joe.spring.springservice.ApiMessages;


/**
 * Exception handler for the web service API.
 * 
 * @author joseph_sicree
 *
 */
@ControllerAdvice(basePackages={"joe.spring.springweb.mvc.controller"})
public class ApiExceptionHandler extends ResponseEntityExceptionHandler {

	protected final static Logger log = LoggerFactory
			.getLogger(ApiExceptionHandler.class);
		
	@Override
	protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException ex,
			HttpHeaders headers, HttpStatus status, WebRequest request) {
		
		log.debug("In handleMethodArgumentNotValid.");

		BindingResult bindingResult = ex.getBindingResult();
		
		ArrayList<ApiFieldError> fieldErrors = new ArrayList<ApiFieldError>();
		
		for (FieldError fe: bindingResult.getFieldErrors()) {
			ApiFieldError fieldError = new ApiFieldError();
			fieldError.setCode(fe.getCode());
			fieldError.setField(fe.getField());
			fieldError.setMessage(fe.getDefaultMessage());
			fieldErrors.add(fieldError);
		}
		
		ArrayList<ApiGlobalError> globalErrors = new ArrayList<ApiGlobalError>();
		
		for (ObjectError oe : bindingResult.getGlobalErrors()) {
			ApiGlobalError globalError = new ApiGlobalError();
			globalError.setCode(oe.getCode());
			globalError.setMessage(oe.getDefaultMessage());
			globalErrors.add(globalError);
		}

		ErrorResponse resp = new ErrorResponse();
		resp.getFieldErrors().addAll(fieldErrors);
		resp.getGlobalErrors().addAll(globalErrors);

		return new ResponseEntity<>(resp, HttpStatus.UNPROCESSABLE_ENTITY);
	}

	/**
	 * Handler for <code>ApiException</code>.
	 * 
	 * @param ex
	 * @param request
	 * @return 
	 */
	@ExceptionHandler(value={ApiException.class})
	public ResponseEntity<Object> handleApiException(Exception ex, WebRequest request) {

		log.debug("In handleApiException. Exception = " + ex.getMessage());
		log.error(ex.getMessage());
		
		ArrayList<ApiGlobalError> globalErrors = new ArrayList<ApiGlobalError>();
		
		ApiGlobalError globalError = new ApiGlobalError();
		globalError.setCode(ApiErrorCode.SERVICE_EXCEPTION.getCode());
		globalError.setMessage(ApiMessages.SERVICE_EXCEPTION_MSG);
		globalErrors.add(globalError);

		ErrorResponse resp = new ErrorResponse();
		resp.getGlobalErrors().addAll(globalErrors);
				
		return new ResponseEntity<>(resp, HttpStatus.INTERNAL_SERVER_ERROR);
		
	}
	
//	@ExceptionHandler(value={AccessDeniedException.class})
//	public ResponseEntity<Object> handleAccessDeniedException(Exception ex, WebRequest request) {
//
//		log.debug("In handleAccessDeniedException.");
//		log.error(ex.getMessage());
//		
//		ArrayList<ApiGlobalError> globalErrors = new ArrayList<ApiGlobalError>();
//		
//		ApiGlobalError globalError = new ApiGlobalError();
//		globalError.setCode(ApiErrorCode.ACCESS_DENIED.getCode());
//		globalError.setMessage(ApiMessages.ACCESS_DENIED_MSG);
//		globalErrors.add(globalError);
//
//		ErrorResponse resp = new ErrorResponse();
//		resp.getGlobalErrors().addAll(globalErrors);
//				
//		return new ResponseEntity<>(resp, HttpStatus.FORBIDDEN);
//		
//	}
	
}
