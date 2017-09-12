package joe.spring.springapp.services.impl;

import java.util.ArrayList;
import java.util.List;

import joe.spring.springapp.data.jpa.repository.CountryRepository;
import joe.spring.springapp.data.jpa.repository.StateRepository;
import joe.spring.springapp.data.reference.Country;
import joe.spring.springapp.data.reference.State;
import joe.spring.springapp.data.reference.Title;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springapp.services.ServiceException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ReferenceServiceImpl implements ReferenceService {

	@Autowired 
	private StateRepository stateRepo;

	@Autowired 
	private CountryRepository countryRepo;
	
	public ReferenceServiceImpl() {
	}

	public State getStateById(final Long stateId) throws ServiceException {
		State state = null;

		if (stateId != null) {
			state = stateRepo.findOne(stateId);	
		} else {
			throw new ServiceException("getStateById missing stateId parameter.");
		}
		
		return state;
	}

	
	public State getStateByCode(final String code) throws ServiceException {
		State state = null;
		if (code != null && !code.isEmpty()) {
			state = stateRepo.findByCode(code);			
		} else {
			throw new ServiceException("getStateByCode missing code parameter.");
		}		
		return state;
		
	}

	public List<State> getAllStates() throws ServiceException {
		return stateRepo.findAll();
	}

	public List<State> getStatesByCountry(Country country) throws ServiceException {
		List<State> states = null;
		if (country != null)
			states = stateRepo.findByCountry(country);
		else {
			throw new ServiceException("getStatesByCountry has null country parameter.");
		}
		return states;
	}

	public List<Country> getAllCountries() throws ServiceException {
		return countryRepo.findAll();
	}

	public Country getCountryByCode(String code) throws ServiceException {
		Country country = null;
		
		if (code != null && !code.isEmpty()) {
			country = countryRepo.findByCode(code);
		} else {
			throw new ServiceException("getCountryByCode missing code parameter.");
		}		
		return country;
	}
	
	public Country getCountryById(final Long countryId) throws ServiceException {
		Country country = null;

		if (countryId != null) {
			country = countryRepo.findOne(countryId);	
		} else {
			throw new ServiceException("getCountryById missing id parameter.");
		}
		
		return country;
	}
	
	public List<Title> getAllTitles() throws ServiceException {
		ArrayList<Title> titles = new ArrayList<Title>();
		titles.add(Title.MR);
		titles.add(Title.MS);
		titles.add(Title.MRS);		
		return titles;
		
	}
	
}
