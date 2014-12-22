package jot.projects.spring.springapp.data.jpa.repository;

import java.util.List;

import jot.projects.spring.springapp.data.domain.Account;
import jot.projects.spring.springapp.data.domain.Customer;
import jot.projects.spring.springapp.data.reference.Country;
import jot.projects.spring.springapp.data.reference.State;

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