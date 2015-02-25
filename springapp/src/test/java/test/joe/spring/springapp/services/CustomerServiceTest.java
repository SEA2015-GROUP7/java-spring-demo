package test.joe.spring.springapp.services;

import java.util.ArrayList;
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
public class CustomerServiceTest {

	protected final static Logger log = LoggerFactory
			.getLogger(CustomerServiceTest.class);

	private static CustomerService customerService;

	@BeforeClass
	public static void setup() {

		AbstractApplicationContext context = new AnnotationConfigApplicationContext(
				DbHibernateConfig.class);
		customerService = (CustomerService) context.getBean("customerService");

		customerService.removeAllCustomers();
	}

	@Test
	public void createCustomer() {

		String firstName = "John";
		String lastName = "Doe";
		String userName = "jdoe";
		Date birthDate = new Date();

		log.info(">> Entering createCustomer.");
		log.info("Creating a single customer.");
		Customer c = customerService.createCustomer(firstName, lastName,
				userName, birthDate);
		org.junit.Assert.assertNotNull(c);
		org.junit.Assert.assertNotNull(c.getId());

		Customer customerById = customerService.getCustomerById(c.getId());
		org.junit.Assert.assertNotNull(customerById);

		ArrayList<Customer> customerList = (ArrayList<Customer>) customerService
				.getCustomersByLastName(lastName);
		org.junit.Assert.assertNotNull(customerList);
		org.junit.Assert.assertNotEquals(customerList.size(), 0);

		customerService.removeCustomer(c.getId());

	}

	@Test
	public void testCustomerMethods() {

		log.info(">> Entering testCustomerMethods");

		String[][] customerNameArray = { { "John", "Doe", "jdoe" },
				{ "Jim", "Doe", "jdoe1" }, { "Jane", "Smith", "jsmith" },
				{ "Steve", "Jones", "sjones" } };

		log.info("Creating test customers.");
		for (int x = 0; x < customerNameArray.length; x++) {
			customerService.createCustomer(customerNameArray[x][0],
					customerNameArray[x][1], customerNameArray[x][2],
					new Date());
		}

		log.info("Testing getAllCustomers().");
		ArrayList<Customer> list = (ArrayList<Customer>) customerService
				.getAllCustomers();
		if (list == null || list.size() != customerNameArray.length) {
			org.junit.Assert.fail("Test of getAllCustomers() failed.");
		}

		log.info("Testing getCustomersByLastName().");
		list = (ArrayList<Customer>) customerService
				.getCustomersByLastName("Doe");
		if (list == null || list.size() != 2) {
			org.junit.Assert.fail("Test of getCustomersByLastName() failed.");
		}

		log.info("Testing getCustomersByLastName() (negative).");
		list = (ArrayList<Customer>) customerService
				.getCustomersByLastName("BAD_NAME");
		if (list == null || list.size() != 0) {
			org.junit.Assert
					.fail("Test of getCustomersByLastName(BAD_NAME) failed.");
		}

		log.info("Removing all customers.");
		customerService.removeAllCustomers();

		log.info("<< Leaving CustomerTest.");

	}

	
	@Test
	public void testGetCustomerByUserName() {

		log.info(">> Entering testGetCustomerByUserName");

		log.info("Creating test customer.");
		String firstName = "John";
		String lastName = "Doe";
		String userName = "jdoe";
		Date dob = new Date();
		Customer c = customerService.createCustomer(firstName,lastName,userName,dob);

		Customer result = customerService.getCustomerByUserName(userName);
		org.junit.Assert.assertNotNull(result);
		log.info("Found customer by userName (" + userName + "): " + result);
		
		log.info("Removing customer.");
		customerService.removeCustomer(c.getId());

		log.info("<< Leaving testGetCustomerByUserName");

	}
	
	
	@Test
	public void negativeCustomerTest() {

		log.info(">> Entering NegativeCustomerTest.");

		try {
			log.info("Testing createCustomer(null,\"Doe\").");
			customerService.createCustomer(null, "Doe", null, null);
			org.junit.Assert.fail("");
		} catch (IllegalStateException ise) {
			// Do nothing.
		}

		try {
			log.info("Testing createCustomer(\"\",\"Doe\").");
			customerService.createCustomer("", "Doe", null, null);
			org.junit.Assert.fail("");
		} catch (IllegalStateException ise) {
			// Do nothing.
		}

		try {
			log.info("Testing createCustomer(\"John\",null).");
			customerService.createCustomer("John", null, null, null);
			org.junit.Assert.fail("");
		} catch (IllegalStateException ise) {
			// Do nothing.
		}

		try {
			log.info("Testing createCustomer(\"John\",\"\").");
			customerService.createCustomer("John", "", null, null);
			org.junit.Assert.fail("");
		} catch (IllegalStateException ise) {
			// Do nothing.
		}
		log.info("<< Leaving NegativeCustomerTest.");

	}

	
	
	@AfterClass
	public static void after() {
		log.info("In after().");
		customerService.removeAllCustomers();
	}

}
