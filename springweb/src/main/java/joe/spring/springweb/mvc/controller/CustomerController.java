package joe.spring.springweb.mvc.controller;

import java.util.ArrayList;
import java.util.List;

import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.services.CustomerService;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * Handles requests for the form page examples.
 */
@Controller
public class CustomerController {
	@Autowired
	protected CustomerService customerService;

	protected final static Logger log = LoggerFactory
			.getLogger(CustomerController.class);

	public CustomerController() {

	}

	@RequestMapping(value = "/customers")
	public String home() {
		log.info("Displaying list of customers");

		return "customers";
	}

	@RequestMapping(value = "/getCustomers", method = RequestMethod.GET)
	public @ResponseBody
	List<Customer> getCustomers() {
		log.debug("Fetching a list of all customers");
		ArrayList<Customer> customerList = (ArrayList<Customer>) customerService.getAllCustomers();
		log.debug("CustomerService.getCustomers() returned " + customerList.size() + " customers.");		
		return customerList;
	}

	@RequestMapping(value = "/customerSearch", method = RequestMethod.GET)
	public String displayCustomerSearch() {
		log.info("Displaying customer search page");

		return "customerSearch";
	}

	
	@RequestMapping(value = "/searchCustomers", method = RequestMethod.POST)
	public @ResponseBody
	List<Customer> searchCustomers(@RequestParam(value = "searchTerm",required=false) String searchTerm) {
		log.debug("Searching for customers with searchTerm = " + searchTerm);
		ArrayList<Customer> customerList = (ArrayList<Customer>) customerService.searchCustomers(searchTerm);
		log.debug("CustomerService.searchCustomers() returned " + customerList.size() + " customers.");		
		return customerList;
	}
	
}