package joe.spring.springweb.security;

import javax.annotation.Resource;
import javax.sql.DataSource;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.jdbc.JdbcDaoImpl;

@EnableWebSecurity
@PropertySource({ "classpath:security_db.properties" })
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

	private static final String PROPERTY_NAME_DATABASE_DRIVER_CLASS = "db.driverClass";
	private static final String PROPERTY_NAME_DATABASE_URL = "db.url";
	private static final String PROPERTY_NAME_DATABASE_USERNAME = "db.username";
	private static final String PROPERTY_NAME_DATABASE_PASSWORD = "db.password";

	@Resource
	private Environment environment;

	protected final static Logger log = LoggerFactory.getLogger(WebSecurityConfig.class);

	@Autowired
	private DataSource securityDataSource;

	@Bean
	public DriverManagerDataSource securityDataSource() {

		DriverManagerDataSource ds = new DriverManagerDataSource();

		ds.setDriverClassName(environment.getRequiredProperty(PROPERTY_NAME_DATABASE_DRIVER_CLASS));
		ds.setUrl(environment.getRequiredProperty(PROPERTY_NAME_DATABASE_URL));
		ds.setUsername(environment.getRequiredProperty(PROPERTY_NAME_DATABASE_USERNAME));
		ds.setPassword(environment.getRequiredProperty(PROPERTY_NAME_DATABASE_PASSWORD));
		return ds;
	}

	@Bean
	public UserDetailsService userDetailsService() {
		JdbcDaoImpl dao = new JdbcDaoImpl();
		dao.setDataSource(securityDataSource);
		return dao;
	}

	@Override
	protected void configure(HttpSecurity http) throws Exception {
		http.authorizeRequests()
			.antMatchers("/", "/resources/**", "/welcome", "/login").permitAll()
			.antMatchers("/home").access("hasRole('ROLE_USER') or hasRole('ROLE_ADMIN')")
			.antMatchers("/admin").access("hasRole('ROLE_ADMIN')")
			.anyRequest().authenticated()
			.and()		
				.formLogin().loginPage("/login")
				.defaultSuccessUrl("/home")
				.failureUrl("/login?error")
				.usernameParameter("username").passwordParameter("password")				
			.and()
				.logout()
				.logoutSuccessUrl("/login?logout")
				.deleteCookies("JSESSIONID"); 
	}
}	
	