package joe.spring.springservice;

import java.util.Properties;

import javax.annotation.Resource;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.context.support.ReloadableResourceBundleMessageSource;
import org.springframework.core.env.Environment;
import org.springframework.http.MediaType;
import org.springframework.validation.Validator;
import org.springframework.web.accept.ContentNegotiationManagerFactoryBean;
import org.springframework.web.servlet.ViewResolver;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;
import org.springframework.web.servlet.view.InternalResourceViewResolver;
import org.springframework.web.servlet.view.JstlView;

import joe.spring.springservice.client.ApiRestClient;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = { "joe.spring.springservice" })
@PropertySource({ "classpath:api.properties", "classpath:swagger.properties"})
public class MvcWebConfig extends WebMvcConfigurerAdapter {

	private static final String PROPERTY_NAME_API_USERNAME = "api.user";
	private static final String PROPERTY_NAME_API_PASSWORD = "api.password";
	private static final String PROPERTY_NAME_API_GET_ALL_COUNTRIES_URL = "api.getAllCountries.url";
	private static final String PROPERTY_NAME_API_GET_STATES_BY_CODE_URL = "api.getStatesByCountry.url";

	@Resource
	private Environment environment;

	@Override
	public void addResourceHandlers(ResourceHandlerRegistry registry) {
		registry.addResourceHandler("/resources/**").addResourceLocations("/resources/");

		registry.addResourceHandler("swagger-ui.html")
	      .addResourceLocations("classpath:/META-INF/resources/");
	 
	    registry.addResourceHandler("/webjars/**")
	      .addResourceLocations("classpath:/META-INF/resources/webjars/");
	
	}

		
	@Bean
	public Validator countryByCodeValidator() {
		return new joe.spring.springservice.validator.CountryByCodeRequestValidator();
	}
	
	@Bean
	public Validator createCustomerValidator() {
		return new joe.spring.springservice.validator.CreateCustomerRequestValidator();
	}

	@Bean
	public Validator customerByUserNameValidator() {
		return new joe.spring.springservice.validator.CustomerByUserNameRequestValidator();
	}

	@Bean
	public Validator customerSearchValidator() {
		return new joe.spring.springservice.validator.CustomerSearchRequestValidator();
	}
	
	@Bean
	public Validator deleteCustomerValidator() {
		return new joe.spring.springservice.validator.DeleteCustomerRequestValidator();
	}
	
	@Bean
	public Validator stateByCodeValidator() {
		return new joe.spring.springservice.validator.StateByCodeRequestValidator();
	}

	@Bean
	public Validator statesByCountryValidator() {
		return new joe.spring.springservice.validator.StatesByCountryRequestValidator();
	}

	@Bean
	public ApiRestClient apiRestClient() {

		ApiRestClient client = new ApiRestClient(
				environment.getRequiredProperty(PROPERTY_NAME_API_USERNAME),
				environment.getRequiredProperty(PROPERTY_NAME_API_PASSWORD));
		client.setAllCountriesUrl(environment.getRequiredProperty(PROPERTY_NAME_API_GET_ALL_COUNTRIES_URL));
		client.setStatesByCountryUrl(environment.getRequiredProperty(PROPERTY_NAME_API_GET_STATES_BY_CODE_URL));
		return client;
	}

}