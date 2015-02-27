package joe.spring.springweb.mvc.controller;

import java.util.ArrayList;
import java.util.List;

import javax.validation.Valid;

import joe.spring.springapp.data.reference.Title;
import joe.spring.springapp.services.ReferenceService;
import joe.spring.springweb.mvc.data.DropDownData;
import joe.spring.springweb.mvc.data.FormFieldError;
import joe.spring.springweb.mvc.data.ValidationResponse;
import joe.spring.springweb.mvc.model.CustomerModel;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
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
public class CreateCustomerFormController {
	@Autowired
	protected ReferenceService refService;

	protected final static Logger log = LoggerFactory
			.getLogger(CreateCustomerFormController.class);

	public CreateCustomerFormController() {

	}

	@RequestMapping(value = "/createCustomer", method=RequestMethod.GET)
	public String displayNewCustomerForm(Model model) {
		
		model.addAttribute("titleList", getTitleList());
		model.addAttribute("customerModel", new CustomerModel());
		log.info("Displaying the create customer form");
		
		return "createCustomer";
	}

	@RequestMapping(value="/createCustomer", method=RequestMethod.POST)
    public String createNewCustomer(@Valid CustomerModel customerModel, BindingResult result, Model model) {

		String dest = "createCustomerThanks";
		log.info("CustomerModel:" + customerModel);					
		if (result.hasErrors()) {
			log.info("Form validation errors: " + result.getErrorCount());
			model.addAttribute("titleList", getTitleList());			
			dest="createCustomer";
		} else {
			log.info("NO form validation errors found. Creating a new customer!");
			model.addAttribute("firstName", customerModel.getFirstName());			
		}
        return dest;
    }	

	@RequestMapping(value="/newCustomerJson", method=RequestMethod.POST)
    public @ResponseBody ValidationResponse createNewCustomerJson(@Valid CustomerModel customerModel, BindingResult result, Model model) {

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
	
	private List<DropDownData> getTitleList() {
		List<Title> titleList = new ArrayList<Title>();
		List<DropDownData> titleDropDownList = new ArrayList<DropDownData>();
		titleList = refService.getAllTitles();
		for (Title t: titleList) {
			titleDropDownList.add(new DropDownData(t.id(), t.name()));
		}
		return titleDropDownList;
	}

}

