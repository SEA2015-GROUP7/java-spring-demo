<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!doctype html>
<html lang="en">
<head>
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.11.1/jquery-ui.js"></script>
<script>
$(document).ready(function() {
 
    // Check if JavaScript is enabled
    $('body').addClass('js');
 
    $( "submit" ).click(function( event ) {
   	 
        alert( "Clicked on the submit button" );
 
        event.preventDefault();    
	});    
});
</script>
</head>
<body>
<div class="login-form"> 
    <h1>Login Form</h1>
    <form action="#">
        <input type="text" name="username" placeholder="username">
        <input type="password" name="password" placeholder="password">
        <input type="submit" value="log in">
    </form>
</div>
</body>
</html>