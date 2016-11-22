package joe.spring.springweb.security;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;

@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {
	
	protected final static Logger log = LoggerFactory
			.getLogger(WebSecurityConfig.class);

	@Bean
	public UserDetailsService userDetailsService() {
		InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
		manager.createUser(User.withUsername("user").password("password").roles("USER").build());
		return manager;
	}	

	@Override
	protected void configure(HttpSecurity http) throws Exception {
		log.info("In WebSecurityConfig.configure(HttpSecurity)");

		log.warn("Disabling CSRF protection for now.");
		http.csrf().disable();
		super.configure(http);
	}

}
