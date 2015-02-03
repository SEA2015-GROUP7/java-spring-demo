<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
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
	<p>The home page for the Spring / JQuery demo project.</p>	
	<p>This web application contains the following examples:</p>
	<ul>
		<li><a href="states">Simple AJAX Data Fetch with JQuery UI SelectMenu</a> - A simple example of a JQuery UI SelectMenu component that calls a web service to fetch data.</li>
	</ul>	
	
</body>
</html>