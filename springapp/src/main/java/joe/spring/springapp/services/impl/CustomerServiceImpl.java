package joe.spring.springapp.services.impl;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import joe.spring.springapp.data.domain.Credential;
import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.data.jpa.repository.CredentialRepository;
import joe.spring.springapp.data.jpa.repository.CustomerRepository;
import joe.spring.springapp.services.CustomerService;
import joe.spring.springapp.services.ServiceException;

@Service
public class CustomerServiceImpl implements CustomerService {

	@Autowired
	private CustomerRepository customerRepo;

	@Autowired
	private CredentialRepository credentialRepo;

	public CustomerServiceImpl() {
	}

	@Override
	public Customer createCustomer(String firstName, String lastName, String userName, Date birthDate,
			String password) throws ServiceException {
		Customer newCustomer = null;

		if (firstName != null && !firstName.isEmpty() && lastName != null
				&& !lastName.isEmpty()) {
			newCustomer = customerRepo.save(new Customer(firstName, lastName,
					userName, birthDate, null));
			if (newCustomer != null) {
				Credential cred = credentialRepo.save(new Credential(newCustomer.getId(), password));								
			}
			
		} else {
			throw new IllegalStateException("Missing method parameter.");
		}
		return newCustomer;
		
	}
	
	@Override
	public Customer updateCustomer(Customer c) throws ServiceException{
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Customer getCustomerById(Long customerId) throws ServiceException {

		Customer c = null;
		if (customerId != null) {
			c = customerRepo.findOne(customerId);
		} else {
			throw new IllegalStateException("Missing method parameter.");
		}
		return c;
	}

	@Override
	public Customer getCustomerByUserName(final String userName) throws ServiceException {
		Customer c = null;
		if (userName != null && !userName.trim().isEmpty()) {
			c = customerRepo.findByUserName(userName);
		} else {
			throw new IllegalStateException("Missing method parameter.");
		}
		return c;
	}

	@Override
	public List<Customer> getAllCustomers() throws ServiceException {
		List<Customer> customerList = customerRepo.findAll();
		return customerList;
	}

	@Override
	public List<Customer> getCustomersByLastName(String lastName) throws ServiceException {
		List<Customer> customerList = null;
		if (lastName != null && !lastName.isEmpty()) {
			customerList = customerRepo.findByLastName(lastName);
		} else {
			throw new IllegalStateException("Missing method parameter.");
		}
		return customerList;
	}

	@Override
	public List<Customer> searchCustomers(final String searchTerm) throws ServiceException {
		
		List<Customer> customerList = new ArrayList<Customer>();
		if (searchTerm != null && !searchTerm.trim().isEmpty()) {
			customerList = customerRepo.searchCustomers(searchTerm);
		} else {
			customerList = customerRepo.findAll();
		}

		return customerList;		
	}

	public Boolean validateCustomer(Long id, String password) throws ServiceException {
		
		Boolean result = false;
		
		if (id != null && password != null && !password.isEmpty()) {
			Customer c = null;
			c = customerRepo.findOne(id);
			
			if (c != null) {
				Credential cred = credentialRepo.findByIdAndPassword(id, password);
				if (cred != null) {
					result = true;
				}
			}			
		}
		
		return result;
	}
	
	@Override
	public void removeCustomer(Long customerId) throws ServiceException {

		if (customerId != null) {
			credentialRepo.delete(customerId);
			customerRepo.delete(customerId);
		} else {
			throw new IllegalStateException("Missing method parameter.");
		}

	}

	@Override
	public void removeAllCustomers() throws ServiceException {
		credentialRepo.deleteAll();
		customerRepo.deleteAll();
	}

}
