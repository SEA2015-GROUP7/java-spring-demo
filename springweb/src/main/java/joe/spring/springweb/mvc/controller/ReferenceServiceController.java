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
import joe.spring.springdomain.CountryDtoList;
import joe.spring.springdomain.CountryResponse;
import joe.spring.springdomain.StateByCodeRequest;
import joe.spring.springdomain.StateDto;
import joe.spring.springdomain.StateDtoList;
import joe.spring.springdomain.StateResponse;
import joe.spring.springdomain.StatesByCountryRequest;
import joe.spring.springdomain.StatesResponse;
import joe.spring.springweb.mvc.ApiException;
import joe.spring.springweb.mvc.ApiMessages;

/**
 * Handles requests for the application home page.
 */
@RestController
@RequestMapping("api/reference")
public class ReferenceServiceController {

	@Autowired
	protected ReferenceService refService;

	@Autowired
	@Qualifier("statesByCountryValidator")
	private Validator statesByCountryValidator;

	protected final static Logger log = LoggerFactory
			.getLogger(ReferenceServiceController.class);

	@InitBinder("statesByCountryRequest")
	public void setupStatesByCountryBinder(WebDataBinder binder) {
		binder.addValidators(statesByCountryValidator);
	}

	@RequestMapping(value = "/v1/getCountryByCode", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<CountryResponse> getCountryByCode(@RequestBody CountryByCodeRequest request) throws ApiException {
		
		log.debug("Calling /v1/getCountryByCode with countryCode = " + request.getCountryCode());

		CountryResponse response = new CountryResponse();
		
		Country c = null;
		try {
			c = refService.getCountryByCode(request.getCountryCode());
			if (c != null) {
				response.setCountry(DtoConverter.toCountryDto(c));
			}
		} catch (ServiceException e) {
			log.error("ServiceException thrown while getting country by code.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
				
		return new ResponseEntity<>(response,HttpStatus.OK);
	}

	@RequestMapping(value = "/v1/getAllCountries", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<CountriesResponse> getAllCountries() throws ApiException {
		
		log.debug("Calling /v1/getAllCountries");

		CountriesResponse response = new CountriesResponse();

		ArrayList<Country> countryList = new ArrayList<Country>();		
		try {
			countryList = (ArrayList<Country>) refService.getAllCountries();
			if (countryList != null) {
				CountryDtoList cdtoList = new CountryDtoList();
				cdtoList.getCountries().addAll(DtoConverter.toCountryDtoList(countryList));
				response.setCountries(cdtoList);
			}
		} catch (ServiceException e) {
			log.error("ServiceException thrown while getting all countries.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
		
		return new ResponseEntity<>(response,HttpStatus.OK);
	}
	
	@RequestMapping(value = "/v1/getStatesByCountry", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<StatesResponse> getStatesByCountryCode(@Valid @RequestBody StatesByCountryRequest statesByCountryRequest) throws ApiException {
		
		log.debug("Calling /v1/getStatesByCountry with countryCode = " + statesByCountryRequest.getCountryCode());

		StatesResponse response = new StatesResponse();
		
		Country c = null;
		try {
			c = refService.getCountryByCode(statesByCountryRequest.getCountryCode());
			if (c != null) {
				//TODO - Optimize this.
				ArrayList<State> stateList = new ArrayList<State>();
				ArrayList<StateDto> stateDtoList = new ArrayList<StateDto>();
				stateList = (ArrayList<State>) refService.getStatesByCountry(c);
				if (stateList != null && stateList.size() > 0) {
					stateDtoList = (ArrayList<StateDto>) DtoConverter.toStateDtoList(stateList);
				}
				StateDtoList dtoList = new StateDtoList();
				dtoList.getStates().addAll(stateDtoList);
				response.setStates(dtoList);
			}
		} catch (ServiceException e) {
			log.error("ServiceException thrown while getting states by country.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
		
		
		return new ResponseEntity<>(response,HttpStatus.OK);
	}
	
	@RequestMapping(value = "/v1/getStateByCode", method = RequestMethod.POST, produces = "application/json")
	public ResponseEntity<StateResponse> getStateByCode(@RequestBody StateByCodeRequest request) throws ApiException {
		
		log.debug("Calling /v1/getStateByCode with stateCode = " + request.getStateCode());

		StateResponse response = new StateResponse();
		
		State s = null;
		try {
			s = refService.getStateByCode(request.getStateCode());
			if (s != null) {
				response.setState(DtoConverter.toStateDto(s));
			}
		} catch (ServiceException e) {
			log.error("ServiceException thrown while getting state by code.", e);
			e.printStackTrace();
			throw new ApiException(ApiMessages.SERVICE_EXCEPTION_MSG, e);
		}
				
		return new ResponseEntity<>(response,HttpStatus.OK);
	}
	
}