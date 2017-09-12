package joe.spring.springweb.mvc;

public enum ApiErrorCode {
	ACCESS_DENIED("AccessDenied"),
	SERVICE_EXCEPTION("ApiException"),
	NULL_OR_EMPTY_VALUE("NullOrEmptyValue"),
	INVALID_VALUE("InvalidValue"),
	UNKNOWN_COUNTRY_CODE("UnknownCountryCode"), 
	USERNAME_EXISTS("UserNameExists"), 
	CUSTOMER_DOES_NOT_EXIST("CustomerDoesNotExist");
	
	private String code;
	
	ApiErrorCode(String code) {
		this.code = code;
	}
	
	public String getCode() {
		return code;
	}
}
