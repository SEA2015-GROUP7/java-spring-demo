package joe.spring.springapp.services;

import java.util.List;

import joe.spring.springapp.data.reference.Country;
import joe.spring.springapp.data.reference.State;
import joe.spring.springapp.data.reference.Title;

/**
 * An administrative service used to manage customers and accounts.
 * 
 * @author joeontech
 *
 */
public interface ReferenceService {

	public List<Country> getAllCountries() throws ServiceException;
	public Country getCountryById(final Long countryId) throws ServiceException;
	public Country getCountryByCode(String code) throws ServiceException;
	public List<State> getAllStates() throws ServiceException;	
	public State getStateById(final Long stateId) throws ServiceException;
	public State getStateByCode(final String code) throws ServiceException;
	public List<State> getStatesByCountry(Country country) throws ServiceException;	
	public List<Title> getAllTitles() throws ServiceException;	
}


