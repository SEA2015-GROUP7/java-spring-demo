package joe.spring.springweb.mvc.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Handles requests for the form page examples.
 */
@Controller
public class FormController {
	protected final static Logger log = LoggerFactory
			.getLogger(FormController.class);

	public FormController() {

	}

	@RequestMapping(value = "/form")
	public String home() {
		log.info("Displaying sample form");

		return "form";
	}

}