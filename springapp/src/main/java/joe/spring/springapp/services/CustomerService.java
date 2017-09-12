package joe.spring.springapp.services;

import java.util.Date;
import java.util.HashSet;
import java.util.List;

import joe.spring.springapp.data.domain.Address;
import joe.spring.springapp.data.domain.Customer;

/**
 * An administrative service used to manage customers.
 * 
 * @author Joe Sicree
 * 
 */
public interface CustomerService {

	/**
	 * Create a new <code>Customer</code>.
	 * 
	 * @param firstName
	 * @param lastName
	 * @param userName
	 * @param birthDate
	 * @param password
	 * @return A new <code>Customer</code>
	 */
	public Customer createCustomer(String firstName, String lastName,
			String userName, Date birthDate, String password) throws ServiceException;

	/**
	 * Update the specified <code>Customer</code>.
	 * 
	 * @param c
	 * @return The updated <code>Customer</code>
	 */
	public Customer updateCustomer(Customer c) throws ServiceException;

	/**
	 * Look up a <code>Customer</code> by id.
	 *  
	 * @param customerId
	 * @return
	 */
	public Customer getCustomerById(final Long customerId) throws ServiceException;

	/**
	 * Returns a <code>Customer</code> object by user name.
	 * 
	 * @param userName
	 * @return
	 */
	public Customer getCustomerByUserName(final String userName) throws ServiceException; 

	/**
	 * Returns a list of all <code>Customer</code> objects.
	 * 
	 * @return
	 */
	public List<Customer> getAllCustomers() throws ServiceException;

	/**
	 * Returns a list of <code>Customer</code> objects by last name.
	 * 
	 * @param lastName
	 * @return
	 */
	public List<Customer> getCustomersByLastName(final String lastName) throws ServiceException;

	/**
	 * Search for <code>Customer</code> objects by partial first, last or user name.
	 * 
	 * @param searchTerm
	 * @return
	 */
	public List<Customer> searchCustomers(final String searchTerm) throws ServiceException;

	/**
	 * Validate a <code>Customer</code> objects by id and password.
	 * 
	 * @param id
	 * @param password
	 * @return
	 */
	public Boolean validateCustomer(final Long id, final String password) throws ServiceException;
	
	/**
	 * Delete the specified <code>Customer</code>.
	 * 
	 * @param customerId
	 */
	public void removeCustomer(final Long customerId) throws ServiceException;

	/**
	 * Delete all <code>Customer</code> objects.
	 * 
	 */  
	public void removeAllCustomers() throws ServiceException;

}
