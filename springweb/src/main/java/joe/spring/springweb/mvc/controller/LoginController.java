package joe.spring.springweb.mvc.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.Validator;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import joe.spring.springweb.mvc.model.LoginModel;

/**
 * 
 */
@Controller
public class LoginController {

//	@Autowired
//	@Qualifier("loginModelValidator")
//	private Validator validator;

//	@InitBinder
//	private void initBinder(WebDataBinder binder) {
//		binder.setValidator(validator);
//	}

	protected final static Logger log = LoggerFactory.getLogger(LoginController.class);

	public LoginController() {

	}

	
//    @RequestMapping(value = "/login", method = RequestMethod.GET)
//    public String init(Model model) {
//		log.info("Displaying the login page.");
//        model.addAttribute("msg", "Please Enter Your Login Details");
//        return "login";
//    }
// 
//    @RequestMapping(method = RequestMethod.POST)
//    public String submit(Model model, @ModelAttribute("loginBean") LoginModel loginModel) {
//		log.info("Processing the login page.");
//        if (loginModel != null && loginModel.getUserName() != null & loginModel.getPassword() != null) {
//        	
//        	
//            if (loginModel.getUserName().equals("joe") && loginModel.getPassword().equals("foo")) {
//                model.addAttribute("msg", "welcome" + loginModel.getUserName());
//                return "home";
//            } else {
//                model.addAttribute("error", "Invalid Details");
//                return "login";
//            }
//        } else {
//            model.addAttribute("error", "Please enter Details");
//            return "login";
//        }
//    }	
		
}