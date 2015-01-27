package joe.spring.springapp.data.jpa.repository;

import joe.spring.springapp.data.domain.Account;
import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.data.reference.Country;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository to manage {@link Account} instances.
 * 
 */
@Repository
public interface CountryRepository extends JpaRepository<Country, Long> {

	/**
	 * Returns all accounts belonging to the given {@link Customer}.
	 * 
	 * @param customer
	 * @return
	 */	
	
	Country findByCode(String code);
	
}