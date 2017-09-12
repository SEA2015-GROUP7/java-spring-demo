package joe.spring.springweb.mvc.controller;

import java.util.ArrayList;

import javax.validation.Valid;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.Validator;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import joe.spring.springapp.data.dto.DtoConverter;
import joe.spring.springapp.data.reference.Country;
import joe.spring.springapp.data.reference.State;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springapp.services.ServiceException;
import joe.spring.springdomain.CountriesResponse;
import joe.spring.springdomain.CountryByCodeRequest;
import joe.spring.springdomain.CountryResponse;
import joe.spring.springdomain.RequestStatus;
import joe.spring.springdomain.StateByCodeRequest;
import joe.spring.springdomain.StateDto;
import joe.spring.springdomain.StateDtoList;
import joe.spring.springdomain.StateResponse;
import joe.spring.springdomain.StatesByCountryRequest;
import joe.spring.springdomain.StatesResponse;

/**
 * Handles requests for the application home page.
 */
@RestController
@RequestMapping("api/test")
public class TestServiceController {

	protected final static Logger log = LoggerFactory
			.getLogger(TestServiceController.class);

	@RequestMapping(value = "/v1/throwException", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<StatesResponse> throwException() throws ServiceException {
		
		log.debug("Calling /v1/throwException");

//		StatesResponse response = new StatesResponse();
		
		throw new ServiceException("Fi fi fo fum");
		
		//return new ResponseEntity<>(response,HttpStatus.OK);
	}

	@RequestMapping(value = "/v1/throwNpeException", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<StatesResponse> throwNpeException() throws ServiceException {
		
		log.debug("Calling /v1/throwNpeException");

		StatesResponse response = new StatesResponse();
//		response.setStatus(RequestStatus.ERROR);

		
		throw new NullPointerException("This is a NPE");
		
		//return new ResponseEntity<>(response,HttpStatus.OK);
	}
	
	
	
}