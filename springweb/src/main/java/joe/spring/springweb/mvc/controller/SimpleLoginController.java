package joe.spring.springweb.mvc.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Handles requests for the form page examples.
 */
@Controller
public class SimpleLoginController {
	protected final static Logger log = LoggerFactory
			.getLogger(SimpleLoginController.class);

	public SimpleLoginController() {

	}

	@RequestMapping(value = "/simpleLogin")
	public String login() {
		log.info("Displaying simple login form");

		return "simpleLogin";
	}

	
}