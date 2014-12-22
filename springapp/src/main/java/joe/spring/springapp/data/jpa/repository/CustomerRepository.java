package jot.projects.spring.springapp.data.jpa.repository;

import java.util.List;

import jot.projects.spring.springapp.data.domain.Customer;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository to manage {@link Customer} instances.
 * 
 */
@Repository
public interface CustomerRepository extends JpaRepository<Customer, Long> {

	List<Customer> findByLastName(String lastName);
	Customer findByUserName(String userName);
}