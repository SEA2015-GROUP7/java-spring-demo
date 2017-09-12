package joe.spring.springweb.mvc.controller;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import joe.spring.springapp.data.dto.DtoConverter;
import joe.spring.springapp.data.reference.Country;
import joe.spring.springapp.data.reference.State;
import joe.spring.springapp.data.reference.Title;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springapp.services.ServiceException;
import joe.spring.springdomain.CountriesResponse;
import joe.spring.springdomain.CountryDto;
import joe.spring.springdomain.CountryDtoList;
import joe.spring.springdomain.StateDto;
import joe.spring.springdomain.StateDtoList;
import joe.spring.springdomain.StatesByCountryRequest;
import joe.spring.springdomain.StatesResponse;
import joe.spring.springweb.mvc.data.DropDownData;
import joe.spring.springweb.mvc.services.client.BasicAuthRestTemplate;

/**
 * Handles requests for the application home page.
 */
@RestController
public class ReferenceController {

	@Autowired
	protected ReferenceService refService;

//	@Autowired
//	protected RestTemplate apiRestTemplate;
	
	protected final static Logger log = LoggerFactory
			.getLogger(ReferenceController.class);

	@RequestMapping(value = "/getStates", method = RequestMethod.GET, produces = "application/json")
	public ResponseEntity<List<StateDto>> getStatesByCountryCode(
			@RequestParam(value = "countryCode",required=false) String countryCode) {
		log.debug("Calling JSON service getStates() with countryCode = " + countryCode);

		StateDtoList stateDtoList = null;

		BasicAuthRestTemplate rt = new BasicAuthRestTemplate("user","password");
		StatesByCountryRequest req = new StatesByCountryRequest();
		req.setCountryCode(countryCode);
		StatesResponse resp = rt.postForObject("http://localhost:8080/springweb/api/reference/v1/getStatesByCountry", req, StatesResponse.class);
		if (resp != null) {
			stateDtoList = resp.getStates();
		}
		return new ResponseEntity<>(stateDtoList.getStates(),HttpStatus.OK);
	}
	
	
	@RequestMapping(value = "/getStatesDropDownData", method = RequestMethod.GET, produces = "application/json")
	public List<DropDownData> getStatesDropDownDataByCountryId(
			@RequestParam(value = "countryCode",required=false) String countryCode) {
		log.debug("Calling JSON service getStatesDropDownData() with countryCode = " + countryCode);

		ArrayList<DropDownData> dropDownList = new ArrayList<DropDownData>();

		BasicAuthRestTemplate rt = new BasicAuthRestTemplate("user","password");
		StatesByCountryRequest req = new StatesByCountryRequest();
		req.setCountryCode(countryCode);
		StatesResponse resp = rt.postForObject("http://localhost:8080/springweb/api/reference/v1/getStatesByCountry", req, StatesResponse.class);
		if (resp != null) {
			StateDtoList stateDtoList = resp.getStates();
			for (StateDto s : stateDtoList.getStates()) {
				dropDownList.add(new DropDownData(s.getId(), s.getName() + " (" + s.getCode() + ")"));
				
			}
		}
		return dropDownList;
	}

	@RequestMapping(value = "/getTitlesDropDownData", method = RequestMethod.GET, produces = "application/json")
	public List<DropDownData> getTitlesDropDownData() {
		log.debug("Calling JSON service getTitlesAsJSON()");
		ArrayList<DropDownData> dropDownList = new ArrayList<DropDownData>();
		ArrayList<Title> titleList;
		try {
			titleList = (ArrayList<Title>) refService
					.getAllTitles();
			if (titleList != null && titleList.size() > 0) {
				for (Title t : titleList) {
					dropDownList.add(new DropDownData(t.id(), t.name()));
				}
			}
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return dropDownList;
	}

	@RequestMapping(value = "/getCountriesDropDownData", method = RequestMethod.GET, produces = "application/json")
	public List<DropDownData> getCountriesDropDownData() {
		log.debug("Calling JSON service getCountriesAsJSON()");
		ArrayList<DropDownData> dropDownList = new ArrayList<DropDownData>();
		
		BasicAuthRestTemplate rt = new BasicAuthRestTemplate("user","password");
		CountriesResponse resp = rt.postForObject("http://localhost:8080/springweb/api/reference/v1/getAllCountries", null, CountriesResponse.class);
		if (resp != null) {
			CountryDtoList cdtoList = resp.getCountries();
			for (CountryDto c : cdtoList.getCountries()) {
				dropDownList.add(new DropDownData(c.getId(), c.getCode(), c.getName()));
			}			
		}
		
		return dropDownList;
	}
	
	private ArrayList<StateDto> lookupStatesByCountryId(Long countryId) {
		ArrayList<State> stateList = new ArrayList<State>();
		ArrayList<StateDto> stateDtoList = new ArrayList<StateDto>();
			
		Country c = null;
		if (countryId != null) {
			try {
				c = refService.getCountryById(countryId);
				if (c != null) {
					stateList = (ArrayList<State>) refService.getStatesByCountry(c);
				} else {	
					log.warn("Country was null. Getting all states / provinces");
					stateList = (ArrayList<State>) refService.getAllStates();
				}		
				
				if (stateList != null && stateList.size() > 0) {
					stateDtoList = (ArrayList<StateDto>) DtoConverter.toStateDtoList(stateList);
				}
			} catch (ServiceException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}			
		}		
		return stateDtoList;
	}

}