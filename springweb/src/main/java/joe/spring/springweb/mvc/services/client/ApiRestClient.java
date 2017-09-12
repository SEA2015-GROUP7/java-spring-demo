package joe.spring.springweb.mvc.services.client;

import java.util.List;

import org.springframework.stereotype.Component;

import joe.spring.springdomain.CountriesResponse;
import joe.spring.springdomain.CountryDto;
import joe.spring.springdomain.StateDto;
import joe.spring.springdomain.StatesByCountryRequest;
import joe.spring.springdomain.StatesResponse;

/**
 * Rest client wrapper class.
 * 
 * @author joseph_sicree
 *
 */
@Component
public class ApiRestClient {
	
	private String allCountriesUrl;
	private String statesByCountryUrl;
	
	private BasicAuthRestTemplate restTemplate;
	
	public ApiRestClient() {
		super();
		// TODO Auto-generated constructor stub
	}

	public ApiRestClient(String username, String password) {
		super();
		restTemplate = new BasicAuthRestTemplate(username, password);
	}

	public List<CountryDto> getAllCountries() {
		
		CountriesResponse response = new CountriesResponse();
		response = restTemplate.postForObject(allCountriesUrl, null, CountriesResponse.class);		
		return response.getCountries().getCountries();
	}

	public List<StateDto> getStatesByCountry(final String countryCode) {
		
		StatesResponse response = new StatesResponse();
		StatesByCountryRequest request = new StatesByCountryRequest();
		request.setCountryCode(countryCode);
		response = restTemplate.postForObject(statesByCountryUrl, request, StatesResponse.class);		
		return response.getStates().getStates();
	}
	
	
	public String getAllCountriesUrl() {
		return allCountriesUrl;
	}

	public void setAllCountriesUrl(String allCountriesUrl) {
		this.allCountriesUrl = allCountriesUrl;
	}

	public String getStatesByCountryUrl() {
		return statesByCountryUrl;
	}

	public void setStatesByCountryUrl(String statesByCountryUrl) {
		this.statesByCountryUrl = statesByCountryUrl;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("ApiRestClient [allCountriesUrl=");
		builder.append(allCountriesUrl);
		builder.append(", statesByCountryUrl=");
		builder.append(statesByCountryUrl);
		builder.append("]");
		return builder.toString();
	}

	
	
}
