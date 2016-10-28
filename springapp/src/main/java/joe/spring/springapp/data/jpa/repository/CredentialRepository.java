package joe.spring.springapp.data.jpa.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import joe.spring.springapp.data.domain.Credential;

/**
 * 
 */
@Repository
public interface CredentialRepository extends JpaRepository<Credential, Long> {

	/**
	 * 
	 * @param id
	 * @return
	 */
	Credential findById(Long id);

	/**
	 * 
	 * @param id
	 * @param password
	 * @return
	 */
	Credential findByIdAndPassword(Long id, String password);

}