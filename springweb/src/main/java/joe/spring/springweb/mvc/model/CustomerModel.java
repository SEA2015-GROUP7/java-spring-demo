package joe.spring.springweb.mvc.model;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import javax.validation.constraints.Size;

public class CustomerModel {

	@NotNull(message="Please select a title.")
	private Long title;
	
	@Size(min=3, max=15, message="The first name must be between 3 and 15 characters.")
	private String firstName;

	@Size(min=5, max=20, message="The last name must be between 5 and 20 characters.")
	private String lastName;
	
	
	@Size(min=5, max=10, message="The user name must be between 5 and 10 characters.")
	private String userName;
	
	@NotNull(message="Please enter your date of birth.")
	@Pattern(regexp="^[0-1][0-9]/[0-3][0-9]/[1-2][0-9][0-9][0-9]$", message="Please use the format mm/dd/yyyy.")
	private String dob;

	public CustomerModel() {
		super();
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

	public String getDob() {
		return dob;
	}

	public void setDob(String dob) {
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
