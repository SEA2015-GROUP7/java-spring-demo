package joe.spring.springweb.mvc.controller;

import java.util.ArrayList;
import java.util.List;

import javax.validation.Valid;

import joe.spring.springweb.mvc.data.FormFieldError;
import joe.spring.springweb.mvc.data.ValidationResponse;
import joe.spring.springweb.mvc.model.CustomerModel;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * Handles requests for the form page examples.
 */
@Controller
public class NewCustomerFormController {
	protected final static Logger log = LoggerFactory
			.getLogger(FormController.class);

	public NewCustomerFormController() {

	}

	@RequestMapping(value = "/newCustomer", method=RequestMethod.GET)
	public String displayNewCustomerForm() {
		log.info("Displaying the new customer form");
		return "newCustomerForm";
	}
	
	@RequestMapping(value="/newCustomer", method=RequestMethod.POST)
    public @ResponseBody ValidationResponse createNewCustomer(@Valid CustomerModel customerModel, BindingResult result, Model model) {

		ValidationResponse response = new ValidationResponse();
		log.info("CustomerModel:" + customerModel);					
		if (result.hasErrors()) {
			response.setStatus("ERROR");
			List<FormFieldError> errorList = new ArrayList<FormFieldError>();
			log.info("Form validation errors: " + result.getErrorCount());
			for (ObjectError oe: result.getAllErrors() ) {
				errorList.add(new FormFieldError(((FieldError)oe).getField() , ((FieldError)oe).getDefaultMessage()));
				log.info(oe.toString());
			}
			response.setErrorMessageList(errorList);
		} else {
			response.setStatus("OK");
			log.info("NO form validation errors found.");
			//TODO: With no validation errors, time to create a new customer.

		}
        return response;
    }	
}