package jot.projects.spring.springapp.services;

import java.util.List;

import jot.projects.spring.springapp.data.domain.Address;
import jot.projects.spring.springapp.data.domain.Address.AddressType;
import jot.projects.spring.springapp.data.domain.Customer;
import jot.projects.spring.springapp.data.reference.State;

/**
 * An service used to manage addresses.
 * 
 * @author joeontech
 * 
 */
public interface AddressService {

	public Address createAddress(final String primaryAddressLine,
			final String secondaryAddressLine, final String cityName,
			final State state, final String zipCode,
			final AddressType addressType);

	public Address createAddress(final String primaryAddressLine,
			final String secondaryAddressLine, final String cityName,
			final State state, final String zipCode,
			final Customer customer,
			final AddressType addressType);

	public Address getAddressById(final Long addressId);

	public List<Address> getAllAddresses();

	public void removeAllAddresses();

//	public List<Address> getAddressesByType(AddressType at);

}
