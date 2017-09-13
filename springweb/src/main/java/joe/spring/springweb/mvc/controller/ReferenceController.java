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

import joe.spring.springapp.data.reference.Title;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springapp.services.ServiceException;
import joe.spring.springdomain.CountryDto;
import joe.spring.springdomain.StateDto;
import joe.spring.springweb.mvc.data.DropDownData;
import joe.spring.springweb.mvc.services.client.ApiClientException;
import joe.spring.springweb.mvc.services.client.ApiRestClient;

/**
 * Handles requests for the application home page.
 */
@RestController
public class ReferenceController {

	@Autowired
	protected ReferenceService refService;

	@Autowired
	protected ApiRestClient apiRestClient;
	
	protected final static Logger log = LoggerFactory
			.getLogger(ReferenceController.class);

	@RequestMapping(value = "/getStates", method = RequestMethod.GET, produces = "application/json")
	public ResponseEntity<List<StateDto>> getStatesByCountryCode(
			@RequestParam(value = "countryCode",required=false) String countryCode) {
		log.debug("Calling service getStatesByCountryCode() with countryCode = " + countryCode);

		List<StateDto> statesList = new ArrayList<StateDto>();
		try {
			statesList = apiRestClient.getStatesByCountry(countryCode);
		} catch (ApiClientException e) {
			e.printStackTrace();
		}

		return new ResponseEntity<>(statesList,HttpStatus.OK);
	}
		
	@RequestMapping(value = "/getStatesDropDownData", method = RequestMethod.GET, produces = "application/json")
	public ResponseEntity<List<DropDownData>> getStatesDropDownDataByCountryCode(
			@RequestParam(value = "countryCode",required=false) String countryCode) {
		log.debug("Calling service getStatesDropDownDataByCountryCode() with countryCode = " + countryCode);

		ArrayList<DropDownData> dropDownList = new ArrayList<DropDownData>();

		List<StateDto> statesList = new ArrayList<StateDto>();
		try {
			statesList = apiRestClient.getStatesByCountry(countryCode);
		} catch (ApiClientException e) {
			e.printStackTrace();
		}

		for (StateDto s : statesList) {
			dropDownList.add(new DropDownData(s.getId(), s.getName() + " (" + s.getCode() + ")"));			
		}

		return new ResponseEntity<>(dropDownList,HttpStatus.OK);
	}

	@RequestMapping(value = "/getTitlesDropDownData", method = RequestMethod.GET, produces = "application/json")
	public ResponseEntity<List<DropDownData>> getTitlesDropDownData() {
		log.debug("Calling service getTitlesDropDownData()");
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
			e.printStackTrace();
		}

		return new ResponseEntity<>(dropDownList,HttpStatus.OK);
	}

	@RequestMapping(value = "/getCountriesDropDownData", method = RequestMethod.GET, produces = "application/json")
	public ResponseEntity<List<DropDownData>> getCountriesDropDownData() {
		log.debug("Calling service getCountriesDropDownData()");
		ArrayList<DropDownData> dropDownList = new ArrayList<DropDownData>();
		
		log.info("apiRestClient = " + apiRestClient);
		List<CountryDto> countryList = new ArrayList<CountryDto>();
		try {
			countryList = apiRestClient.getAllCountries();
		} catch (ApiClientException e) {
			e.printStackTrace();
		}
		for (CountryDto c : countryList) {
			dropDownList.add(new DropDownData(c.getId(), c.getCode(), c.getName()));
		}			
		
		return new ResponseEntity<>(dropDownList,HttpStatus.OK);
	}

}