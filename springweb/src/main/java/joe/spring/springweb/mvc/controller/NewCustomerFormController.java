package joe.spring.springweb.mvc.controller;

import javax.validation.Valid;

import joe.spring.springweb.mvc.model.CustomerModel;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * Handles requests for the form page examples.
 */
@Controller
public class NewCustomerFormController {
	protected final static Logger log = LoggerFactory
			.getLogger(FormController.class);

	public NewCustomerFormController() {

	}

	@RequestMapping(value = "/createNewCustomer", method=RequestMethod.GET)
	public String displayNewCustomerForm() {
		log.info("Displaying the new customer form");
		return "newCustomerForm";
	}

//	@RequestMapping(value = "/createNewCustomer", method = RequestMethod.POST)
//	public String createNewCustomer(
//			@RequestParam(value = "title",required=false) Long title,
//			@RequestParam(value = "firstName",required=false) String firstName,
//			@RequestParam(value = "lastName",required=false) String lastName,
//			@RequestParam(value = "userName",required=false) String userName,
//			@RequestParam(value = "dob",required=false) Date dob
//			) {
//		log.info("Creating a new customer.");
//		log.info("Title:" + title);
//		log.info("FirstName:" + firstName);
//		log.info("LastName:" + lastName);
//		log.info("UserName:" + userName);
//		log.info("DOB:" + dob);
//		return "newCustomerThankYou";
//	}

	
	@RequestMapping(value="/createNewCustomer", method=RequestMethod.POST)
    public String createNewCustomer(@Valid CustomerModel customerModel, BindingResult result, Model model) {

		log.info("CustomerModel:" + customerModel);			
		if (result.hasErrors()) {
			log.info("Form validation errors: " + result.getErrorCount());
			for (ObjectError oe: result.getAllErrors() ) {
				log.info(oe.toString());
			}
		} else {
			log.info("NO form validation errors found.");
		}
		
		//model.addAttribute("customer", customerModel);
        return "createCustomerThankYou";
    }	
}