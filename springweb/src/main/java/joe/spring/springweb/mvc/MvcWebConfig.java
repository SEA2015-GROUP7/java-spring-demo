package joe.spring.springweb.mvc;

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

import joe.spring.springweb.mvc.services.client.ApiRestClient;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = { "joe.spring.springweb.mvc" })
@PropertySource({ "classpath:api.properties" })
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
	}

	@Bean
	public ViewResolver viewResolver() {

		InternalResourceViewResolver viewResolver = new InternalResourceViewResolver();
		viewResolver.setViewClass(JstlView.class);
		viewResolver.setPrefix("/WEB-INF/views/");
		viewResolver.setSuffix(".jsp");
		return viewResolver;
	}

	@Bean
	public Validator customerModelValidator() {
		return new joe.spring.springweb.mvc.validator.CustomerModelValidator();
	}

	@Bean
	public Validator loginModelValidator() {
		return new joe.spring.springweb.mvc.validator.LoginModelValidator();
	}

	@Bean
	public Validator statesByCountryValidator() {
		return new joe.spring.springweb.mvc.validator.StatesByCountryRequestValidator();
	}

	@Bean
	public Validator createCustomerValidator() {
		return new joe.spring.springweb.mvc.validator.CreateCustomerRequestValidator();
	}

	@Bean
	public Validator deleteCustomerValidator() {
		return new joe.spring.springweb.mvc.validator.DeleteCustomerRequestValidator();
	}

	@Bean
	public ReloadableResourceBundleMessageSource messageSource() {
		ReloadableResourceBundleMessageSource src = new ReloadableResourceBundleMessageSource();
		src.setBasename("classpath:message");
		src.setDefaultEncoding("UTF-8");
		return src;
	}

	@Bean
	public ContentNegotiationManagerFactoryBean contentNegotiationManager() {
		ContentNegotiationManagerFactoryBean bean = new ContentNegotiationManagerFactoryBean();
		bean.setFavorPathExtension(true);
		bean.setFavorParameter(false);
		bean.setParameterName("mediaType");
		bean.setIgnoreAcceptHeader(true);
		bean.setUseJaf(false);
		bean.setDefaultContentType(MediaType.APPLICATION_JSON);

		Properties p = new Properties();
		p.setProperty("json", MediaType.APPLICATION_JSON.toString());
		p.setProperty("xml", MediaType.APPLICATION_XML.toString());
		bean.setMediaTypes(p);

		return bean;
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