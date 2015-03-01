<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<%@ page import="java.util.Date" %>    	
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Spring/JQuery Demo - Home</title>
<link rel="stylesheet"
	href="//code.jquery.com/ui/1.11.1/themes/smoothness/jquery-ui.css">
<link rel="stylesheet" type="text/css" href="<%=request.getContextPath()%>/resources/css/site.css"/>	
<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>
<script src="//code.jquery.com/ui/1.11.1/jquery-ui.js"></script>
<script>
	$(document).ready(
			function() {
			});

</script>
</head>
<body>
<header>Spring / JQuery Demo - Home</header>
<hr/>
<p>The home page for the Spring / JQuery demo project.</p>	
<p>This web application contains the following examples:</p>
<ul>
	<li><a href="states">Simple AJAX Data Fetch with JQuery UI SelectMenu</a> - A simple example of a JQuery UI SelectMenu component that calls a web service to fetch data.</li>
	<li><a href="customers">View Customers</a> - A tabular view of customers with JQuery modal dialogs.</li>
	<li><a href="createCustomer">Create a new Customer (Spring MVC)</a> - A simple form using Spring MVC to create a new customer. This example does not use JQuery.</li>
	<li><a href="customerSearch">Customer Search</a></li>
</ul>	
<hr/>
<footer>Page Generated: <%= new Date() %></footer>	
</body>
</html>