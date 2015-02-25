package test.joe.spring.springapp.services;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.data.jpa.DbHibernateConfig;
import joe.spring.springapp.services.CustomerService;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.AbstractApplicationContext;

/**
 * A simple test class.
 * 
 * @author jsicree
 * 
 */
@RunWith(JUnit4.class)
public class CreateCustomerData {

	protected final static Logger log = LoggerFactory
			.getLogger(CreateCustomerData.class);

	private static CustomerService customerService;

	@BeforeClass
	public static void setup() {

		AbstractApplicationContext context = new AnnotationConfigApplicationContext(
				DbHibernateConfig.class);
		customerService = (CustomerService) context.getBean("customerService");

		customerService.removeAllCustomers();
	}

	@Test
	public void createCustomers() {

		log.info(">> Entering createCustomers.");

		log.debug("Removing existing customers.");
		customerService.removeAllCustomers();
		
		DateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy");
		try {
			log.debug("Adding test customers.");
			customerService.createCustomer("John", "Smith","jsmith01", dateFormat.parse("08/21/1971"));
			customerService.createCustomer("Jane", "Riggs","jriggs01", dateFormat.parse("10/15/1980"));
			customerService.createCustomer("Bill", "Nye","sciguy01", dateFormat.parse("03/25/1962"));
			customerService.createCustomer("Alex", "Lifeson","lerxst", dateFormat.parse("08/27/1953"));
			customerService.createCustomer("Geddy", "Lee","dirk", dateFormat.parse("07/29/1953"));
			customerService.createCustomer("Neil", "Peart","pratt", dateFormat.parse("09/12/1952"));
		} catch (ParseException pe) {
			// Do nothing. :)
		}
	}

	@Test
	public void removeCustomers() {

		log.info(">> Entering removeCustomers.");
		customerService.removeAllCustomers();
	}

	@AfterClass
	public static void after() {
		log.info("In after().");
		//customerService.removeAllCustomers();
	}

}
