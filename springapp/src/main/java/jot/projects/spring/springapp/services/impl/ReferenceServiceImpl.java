package jot.projects.spring.springapp.services.impl;

import java.util.ArrayList;
import java.util.List;

import jot.projects.spring.springapp.data.jpa.repository.CountryRepository;
import jot.projects.spring.springapp.data.jpa.repository.StateRepository;
import jot.projects.spring.springapp.data.reference.Country;
import jot.projects.spring.springapp.data.reference.State;
import jot.projects.spring.springapp.data.reference.Title;
import jot.projects.spring.springapp.services.ReferenceService;

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

	public State getStateById(final Long stateId) {
		State state = null;

		if (stateId != null) {
			state = stateRepo.findOne(stateId);	
		} else {
			throw new IllegalStateException("Missing method parameter.");
		}
		
		return state;
	}

	
	public State getStateByCode(final String code) {
		return stateRepo.findByCode(code);
		
	}

	public List<State> getAllStates() {
		return stateRepo.findAll();
	}

	public List<State> getStatesByCountry(Country country) {
		return stateRepo.findByCountry(country);
	}

	public List<Country> getAllCountries() {
		return countryRepo.findAll();
	}

	public Country getCountryByCode(String code) {
		return countryRepo.findByCode(code);
	}
	
	public Country getCountryById(final Long countryId) {
		Country country = null;

		if (countryId != null) {
			country = countryRepo.findOne(countryId);	
		} else {
			throw new IllegalStateException("Missing method parameter.");
		}
		
		return country;
	}
	
	public List<Title> getAllTitles() {
		ArrayList<Title> titles = new ArrayList<Title>();
		titles.add(Title.MR);
		titles.add(Title.MS);
		titles.add(Title.MRS);		
		return titles;
		
	}

	
}
