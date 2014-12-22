package joe.spring.springapp.data.jpa.repository;

import java.util.List;

import joe.spring.springapp.data.domain.Account;
import joe.spring.springapp.data.domain.Customer;
import joe.spring.springapp.data.reference.Country;
import joe.spring.springapp.data.reference.State;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository to manage {@link Account} instances.
 * 
 */
@Repository
public interface StateRepository extends JpaRepository<State, Long> {

	/**
	 * Returns all accounts belonging to the given {@link Customer}.
	 * 
	 * @param customer
	 * @return
	 */	
	
	State findByCode(String code);

	List<State> findByCountry(Country country);	
	
}