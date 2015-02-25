package joe.spring.springweb.mvc.controller;

import java.util.Date;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * Handles requests for the form page examples.
 */
@Controller
public class NewCustomerFormController {
	protected final static Logger log = LoggerFactory
			.getLogger(FormController.class);

	public NewCustomerFormController() {

	}

	@RequestMapping(value = "/newCustomerForm")
	public String displayNewCustomerForm() {
		log.info("Displaying the new customer form");
		return "newCustomerForm";
	}

	@RequestMapping(value = "/createNewCustomer", method = RequestMethod.POST)
	public String createNewCustomer(
			@RequestParam(value = "titleId",required=false) Long titleId,
			@RequestParam(value = "firstName",required=false) String firstName,
			@RequestParam(value = "lastName",required=false) String lastName,
			@RequestParam(value = "userName",required=false) String userName,
			@RequestParam(value = "dob",required=false) Date dob
			) {
		log.info("Creating a new customer.");
		log.info("Title ID:" + titleId);
		log.info("FirstName:" + firstName);
		log.info("LastName:" + lastName);
		log.info("UserName:" + userName);
		log.info("DOB:" + dob);
		return "newCustomerThankYou";
	}

}