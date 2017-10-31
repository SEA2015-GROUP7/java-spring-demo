package joe.spring.springservice;

import javax.annotation.Resource;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;
import org.springframework.validation.Validator;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

@Configuration
@EnableWebMvc
@ComponentScan(basePackages = { "joe.spring.springservice" })
@PropertySource({"classpath:swagger.properties"})
public class MvcWebConfig extends WebMvcConfigurerAdapter {

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

}