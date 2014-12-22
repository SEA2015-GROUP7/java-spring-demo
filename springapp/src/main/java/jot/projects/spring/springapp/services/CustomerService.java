package jot.projects.spring.springapp.services;

import java.util.Date;
import java.util.HashSet;
import java.util.List;

import jot.projects.spring.springapp.data.domain.Address;
import jot.projects.spring.springapp.data.domain.Customer;

/**
 * An administrative service used to manage customers and accounts.
 * 
 * @author joeontech
 * 
 */
public interface CustomerService {

	public Customer createCustomer(String firstName, String lastName,
			String userName, Date birthDate);

	public Customer createCustomer(String firstName, String lastName,
			String userName, Date birthDate, HashSet<Address> addresses);

	public Customer updateCustomer(Customer c);

	public List<Customer> getCustomersByLastName(final String lastName);

	public List<Customer> getAllCustomers();

	public Customer getCustomerById(final Long customerId);

	public Customer getCustomerByUserName(final String userName);

	public void removeCustomer(final Long customerId);

	public void removeAllCustomers();

}
