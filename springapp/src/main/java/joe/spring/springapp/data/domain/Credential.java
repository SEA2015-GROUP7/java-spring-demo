package joe.spring.springapp.data.domain;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;

@Entity(name="CREDENTIAL")
public class Credential {

	@Id	
	private Long id;
	
	@Column(name="PASSWORD")
	private String password;

	public Credential() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Credential(Long id, String password) {
		super();
		this.id =id;
		this.password = password;
	}

	public Long getCustomerId() {
		return id;
	}

	public void setCustomerId(Long customerId) {
		this.id = customerId;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	@Override
	public String toString() {
		return "Credential [customerId=" + id + ", password=" + password + "]";
	}

}
