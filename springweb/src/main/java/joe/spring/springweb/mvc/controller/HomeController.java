package joe.spring.springweb.mvc.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Handles requests for the application home page.
 */
@Controller
public class HomeController {
	protected final static Logger log = LoggerFactory
			.getLogger(HomeController.class);

	public HomeController() {

	}

	@RequestMapping(value = "/home")
	public String home() {
		log.info("Passing through...");

//		log.info("AccountService.getAllAccounts().size(): "
//				+ accountService.getAllAccounts().size());
//		log.info("CustomerService.getAllCustomers().size(): "
//				+ customerService.getAllCustomers().size());

		return "home";
	}

	@RequestMapping(value = "/add")
	public String add() {
		log.info("Adding...");

//		Customer c = customerService.createCustomer("Joe", "Sicree");
//		log.info("Added customer: " + c);
//
//		Account a = accountService.createAccount(c, AccountType.FREE, new Date());
//		log.info("Added account: " + a);
		return "home";
	}

	@RequestMapping(value = "/remove")
	public String remove() {
		log.info("Removing accounts and customers...");

//		accountService.removeAllAccounts();
//		log.info("Removed all accounts...");
//		
//		customerService.removeAllCustomers();
		log.info("Removed all customers...");

		return "home";
	}

	@RequestMapping(value = "/hello")
	public String hello() {
		log.info("Saying hello...");

		return "home";
	}

	@RequestMapping(value = "/goodbye")
	public String goodbye() {
		log.info("Saying goodbye...");

		return "home";
	}

}