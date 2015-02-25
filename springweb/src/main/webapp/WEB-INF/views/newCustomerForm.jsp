<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>States</title>
<link rel="stylesheet"
	href="//code.jquery.com/ui/1.11.1/themes/smoothness/jquery-ui.css">
<link rel="stylesheet" type="text/css" href="<%=request.getContextPath()%>/resources/css/site.css"/>	
<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>
<script src="//code.jquery.com/ui/1.11.1/jquery-ui.js"></script>
<script>
	$(document).ready(
			function() {
			    $( "#title" ).selectmenu();
				$( "#dob" ).datepicker({
				      changeMonth: true,
				      changeYear: true,
				      yearRange : '-99:+0'
				    });
			    $( "#submit" ).button();

			    $.getJSON('getTitlesDropDownData', function(data){
				    var html = '';
				    var len = data.length;
				    for (var i = 0; i< len; i++) {
				        html += '<option value="' + data[i].id + '">' + data[i].name + '</option>';
				    }
				    $('#title').append(html);
				});			    
			    
			});
	
	function createNewCustomer() {
		titleId = $("#title option:selected").val();
		firstName = $("#firstName").val();
		lastName = $("#lastName").val();
		userName = $("#userName").val();
		dob = $("#dob").val();

		$.ajax({
					method: "POST",
					dataType : "json",
					url : "createNewCustomer",
					data : {
						titleId : titleId,
						firstName : firstName,
						lastName : lastName,
						userName : userName,
						dob : dob
					}
				});
		event.preventDefault();
	}
	
</script>
</head>
<body>
<header>New Customer</header>
 
<form id="newCustomerForm">
    <fieldset>
	  <label for="title">Title</label><select name="title" id="title"></select><br/>
	  <label for="firstName">First Name</label><input type="text" id="firstName"></input><br/>
	  <label for="lastName">Last Name</label><input type="text" id="lastName"></input><br/>
	  <label for="userName">User Name</label><input type="text" id="userName"></input><br/>
	  <label for="dob">Birth Date</label><input type="text" id="dob"/><br/>	  
	  <button name="submit" id="submit" onClick="createNewCustomer()">Submit</button> 
	</fieldset>
</form>
</body>
</html>