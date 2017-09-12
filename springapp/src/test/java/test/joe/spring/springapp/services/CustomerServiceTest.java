package test.joe.spring.springapp.services;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.data.jpa.DbHibernateConfig;
import joe.spring.springapp.services.CustomerService;
import joe.spring.springapp.services.ServiceException;

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
	private static AbstractApplicationContext context;
	@BeforeClass
	public static void setup() {

		context = new AnnotationConfigApplicationContext(
				DbHibernateConfig.class);
		customerService = (CustomerService) context.getBean("customerService");

		try {
			customerService.removeAllCustomers();
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Test
	public void createCustomer() {

		String firstName = "John";
		String lastName = "Doe";
		String userName = "jdoe";
		Date birthDate = new Date();
		String password = "password";

		log.info(">> Entering createCustomer.");
		log.info("Creating a single customer.");
		Customer c = null;
		try {
			c = customerService.createCustomer(firstName, lastName,
					userName, birthDate,password);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		org.junit.Assert.assertNotNull(c);
		org.junit.Assert.assertNotNull(c.getId());

		Customer customerById = null;
		try {
			customerById = customerService.getCustomerById(c.getId());
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		org.junit.Assert.assertNotNull(customerById);

		ArrayList<Customer> customerList = null;
		try {
			customerList = (ArrayList<Customer>) customerService
					.getCustomersByLastName(lastName);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		org.junit.Assert.assertNotNull(customerList);
		org.junit.Assert.assertNotEquals(customerList.size(), 0);

		log.info("Removing the customer.");
		try {
			customerService.removeCustomer(c.getId());
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	@Test
	public void testCustomerMethods() {

		log.info(">> Entering testCustomerMethods");

		String[][] customerNameArray = { { "John", "Doe", "jdoe", "password" },
				{ "Jim", "Doe", "jdoe1", "password" }, { "Jane", "Smith", "jsmith", "password" },
				{ "Steve", "Jones", "sjones", "password" } };

		log.info("Creating test customers.");
		for (int x = 0; x < customerNameArray.length; x++) {
			try {
				customerService.createCustomer(customerNameArray[x][0],
						customerNameArray[x][1], customerNameArray[x][2],
						new Date(), customerNameArray[x][3]);
			} catch (ServiceException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

		log.info("Testing getAllCustomers().");
		ArrayList<Customer> list = null;
		try {
			list = (ArrayList<Customer>) customerService
					.getAllCustomers();
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (list == null || list.size() != customerNameArray.length) {
			org.junit.Assert.fail("Test of getAllCustomers() failed.");
		}

		log.info("Testing getCustomersByLastName().");
		try {
			list = (ArrayList<Customer>) customerService
					.getCustomersByLastName("Doe");
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (list == null || list.size() != 2) {
			org.junit.Assert.fail("Test of getCustomersByLastName() failed.");
		}

		log.info("Testing getCustomersByLastName() (negative).");
		try {
			list = (ArrayList<Customer>) customerService
					.getCustomersByLastName("BAD_NAME");
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (list == null || list.size() != 0) {
			org.junit.Assert
					.fail("Test of getCustomersByLastName(BAD_NAME) failed.");
		}

		log.info("Removing all customers.");
		try {
			customerService.removeAllCustomers();
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		log.info("<< Leaving CustomerTest.");

	}

	
	@Test
	public void testGetCustomerByUserName() {

		log.info(">> Entering testGetCustomerByUserName");

		log.info("Creating test customer.");
		String firstName = "John";
		String lastName = "Doe";
		String userName = "jdoe";
		String password = "password";

		Date dob = new Date();
		Customer c = null;
		try {
			c = customerService.createCustomer(firstName,lastName,userName,dob, password);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		Customer result = null;
		try {
			result = customerService.getCustomerByUserName(userName);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		org.junit.Assert.assertNotNull(result);
		log.info("Found customer by userName (" + userName + "): " + result);
		
		log.info("Removing customer.");
		try {
			customerService.removeCustomer(c.getId());
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		log.info("<< Leaving testGetCustomerByUserName");

	}
	
	/**
	 * Tests the searchCustomers method, which will do a partial match on either
	 * the first name, last name or user name. If the search term in null, then
	 * all records are returned.
	 */
	@Test
	public void testSearchCustomers() {

		log.info(">> Entering testSearchCustomers");

		log.info("Creating test customer.");
		String firstName = "John";
		String lastName = "Doe";
		String userName = "jdoe";
		Date dob = new Date();
		String password = "password";

		Customer c = null;
		try {
			c = customerService.createCustomer(firstName,lastName,userName,dob,password);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		List<Customer> customerList = null;
		try {
			customerList = customerService.searchCustomers(firstName);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + firstName  + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + firstName +")");
		}

		try {
			customerList = customerService.searchCustomers(firstName.substring(0,1));
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + firstName.substring(0,1)  + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + firstName.substring(0,1) +")");
		}

		try {
			customerList = customerService.searchCustomers(firstName.substring(firstName.length() - 2));
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + firstName.substring(firstName.length() - 2)  + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + firstName.substring(firstName.length() - 2) +")");
		}

		try {
			customerList = customerService.searchCustomers(lastName);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + lastName  + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + lastName +")");
		}

		try {
			customerList = customerService.searchCustomers(lastName.substring(0,1));
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + lastName.substring(0,1)  + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + lastName.substring(0,1) +")");
		}

		try {
			customerList = customerService.searchCustomers(firstName.substring(lastName.length() - 2));
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + firstName.substring(lastName.length() - 2)  + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + lastName.substring(firstName.length() - 2) +")");
		}

		try {
			customerList = customerService.searchCustomers(userName);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + userName + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + userName +")");
		}

		try {
			customerList = customerService.searchCustomers(userName.substring(0,1));
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + userName.substring(0,1)  + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + userName.substring(0,1) +")");
		}

		try {
			customerList = customerService.searchCustomers(firstName.substring(userName.length() - 2));
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(" + firstName.substring(userName.length() - 2)  + ") failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(" + userName.substring(firstName.length() - 2) +")");
		}

		String badString = "XXX";
		try {
			customerList = customerService.searchCustomers(badString);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			log.info("Found no customers as expected using searchCustomers(" + badString + ")");
		} else {
			org.junit.Assert.fail("searchCustomers(" + badString + ") failed by returning records.");
		}
		
		try {
			customerList = customerService.searchCustomers(null);
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if (customerList == null || customerList.size() == 0) {
			org.junit.Assert.fail("searchCustomers(null) failed.");
		} else {
			log.info("Found " + customerList.size() + " customers using searchCustomers(null)");
		}
		
		log.info("Removing customer.");
		try {
			customerService.removeCustomer(c.getId());
		} catch (ServiceException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		log.info("<< Leaving testLookupCustomers");

	}
	
	@Test
	public void negativeCustomerTest() {

		log.info(">> Entering NegativeCustomerTest.");

		try {
			log.info("Testing createCustomer(null,\"Doe\").");
			try {
				customerService.createCustomer(null, "Doe", null, null, null);
			} catch (ServiceException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			org.junit.Assert.fail("");
		} catch (IllegalStateException ise) {
			// Do nothing.
		}

		try {
			log.info("Testing createCustomer(\"\",\"Doe\").");
			try {
				customerService.createCustomer("", "Doe", null, null, null);
			} catch (ServiceException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			org.junit.Assert.fail("");
		} catch (IllegalStateException ise) {
			// Do nothing.
		}

		try {
			log.info("Testing createCustomer(\"John\",null).");
			try {
				customerService.createCustomer("John", null, null, null, null);
			} catch (ServiceException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			org.junit.Assert.fail("");
		} catch (IllegalStateException ise) {
			// Do nothing.
		}

		try {
			log.info("Testing createCustomer(\"John\",\"\").");
			try {
				customerService.createCustomer("John", "", null, null, null);
			} catch (ServiceException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			org.junit.Assert.fail("");
		} catch (IllegalStateException ise) {
			// Do nothing.
		}
		log.info("<< Leaving NegativeCustomerTest.");

	}

	
	
	@AfterClass
	public static void after() {
		log.info("In after().");
		//customerService.removeAllCustomers();
		if (context != null) {
			context.close();
		}

	}

}
