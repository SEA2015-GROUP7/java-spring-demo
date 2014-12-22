package jot.projects.spring.springweb.mvc.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Handles requests for the form page examples.
 */
@Controller
public class LoginController {
	protected final static Logger log = LoggerFactory
			.getLogger(LoginController.class);

	public LoginController() {

	}

	@RequestMapping(value = "/login")
	public String login() {
		log.info("Displaying login form");

		return "login";
	}

//	@RequestMapping(value = "/logout")
//	public String logout() {
//		log.info("Logging out.");
//
//		return "form";
//	}
	
	
}