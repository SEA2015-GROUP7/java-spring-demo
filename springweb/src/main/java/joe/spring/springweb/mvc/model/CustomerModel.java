package joe.spring.springweb.mvc.model;

import java.util.Date;

import javax.validation.constraints.Max;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;


public class CustomerModel {

	@NotNull
	private Long title;
	
	@Size(min=3, max=15)
	private String firstName;

	@Size(min=5, max=20)
	private String lastName;
	
	
	@Size(min=5, max=10)
	private String userName;
	
	@NotNull
	private Date dob;

	public CustomerModel() {
		super();
		// TODO Auto-generated constructor stub
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public Date getDob() {
		return dob;
	}

	public void setDob(Date dob) {
		this.dob = dob;
	}

	public Long getTitle() {
		return title;
	}

	public void setTitle(Long title) {
		this.title = title;
	}

	@Override
	public String toString() {
		return "CustomerModel [title=" + title + ", firstName=" + firstName
				+ ", lastName=" + lastName + ", userName=" + userName
				+ ", dob=" + dob + "]";
	}

	
}
