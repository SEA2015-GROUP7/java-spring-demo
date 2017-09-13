package joe.spring.springweb.mvc.services.client;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import org.springframework.web.client.HttpStatusCodeException;

import joe.spring.springdomain.CountriesResponse;
import joe.spring.springdomain.CountryDto;
import joe.spring.springdomain.StateDto;
import joe.spring.springdomain.StateDtoList;
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

	protected final static Logger log = LoggerFactory
			.getLogger(ApiRestClient.class);

	public ApiRestClient() {
		super();
	}

	public ApiRestClient(String username, String password) {
		super();
		restTemplate = new BasicAuthRestTemplate(username, password);
	}

	public List<CountryDto> getAllCountries() throws ApiClientException {

		CountriesResponse response = new CountriesResponse();
		try {
			response = restTemplate.postForObject(allCountriesUrl, null, CountriesResponse.class);
		} catch (HttpStatusCodeException sce) {
			log.error("An HttpStatusCodeException was thrown calling the getAllCountries service. HTTP status code: " + sce.getRawStatusCode());
			log.error("ErrorResponse for HttpStatusCodeException: " + sce.getResponseBodyAsString());
			throw new ApiClientException("HttpStatusCodeException caught after call to getAllCountries service. HTTP status code: " + sce.getRawStatusCode(), sce);			
		}		
		return response.getCountries().getCountries();
	}

	public List<StateDto> getStatesByCountry(final String countryCode) throws ApiClientException {

		StatesResponse response = new StatesResponse();
		StatesByCountryRequest request = new StatesByCountryRequest();
		request.setCountryCode(countryCode);
		try {
			response = restTemplate.postForObject(statesByCountryUrl, request, StatesResponse.class);
		} catch (HttpStatusCodeException sce) {
			log.error("An HttpStatusCodeException was thrown calling the getStatesByCountry service. HTTP status code: " + sce.getRawStatusCode());
			log.error("ErrorResponse for HttpStatusCodeException: " + sce.getResponseBodyAsString());
			throw new ApiClientException("HttpStatusCodeException caught after call to getStatesByCountry service. HTTP status code: " + sce.getRawStatusCode(), sce);			
		}
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
