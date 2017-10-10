<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="sec" uri="http://www.springframework.org/security/tags" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<%@ page import="java.util.Date" %>    	
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>java-spring-demo: Customer Search</title>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/smoothness/jquery-ui.css">
<link rel="stylesheet" type="text/css" href="<%=request.getContextPath()%>/resources/css/site.css"/>	

<script
  src="https://code.jquery.com/jquery-3.2.1.js"
  integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE="
  crossorigin="anonymous"></script>
  
<script
  src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"
  integrity="sha256-T0Vest3yCU7pafRw9r+settMBX6JkKN06dqBnpQ8d30="
  crossorigin="anonymous"></script>
<sec:csrfMetaTags />
<script>

	var csrfParameter = $("meta[name='_csrf_parameter']").attr("content");
	var csrfHeader = $("meta[name='_csrf_header']").attr("content");
	var csrfToken = $("meta[name='_csrf']").attr("content");


	$(function() {
				var dialog, form,
				firstName = $( "#firstName" ),
				lastName = $( "#lastName" ),
				userName = $( "#userName" ),
				dob = $( "#dob" ),
			    allFields = $( [] ).add( firstName ).add( lastName ).add( userName ).add( dob );

				function searchCustomers() {
					var searchVal = $("#searchVal").val();
					var headers = {};
					headers[csrfHeader] = csrfToken;

					$('#customer_table').hide();
					$('#customer_table TBODY tr').remove();

					$.ajax({
						method: "POST",
						dataType : "json",
						url : "customerSearch",
						data : {
							searchTerm : searchVal
						},						
						success: function(data) {
							var html = '';
							var len = data.customers.length;
							if (len > 0) {
								for (var i = 0; i < len; i++) {
									html = "<tr id='" + data.customers[i].id + "'><td>" + data.customers[i].lastName 
										 + "</td><td>" + data.customers[i].firstName 
										 + "</td><td>" + data.customers[i].userName
										 + "</td><td>" + new Date(data.customers[i].birthDate).toString()
											+ "</td></tr>";
									$('#customer_table TBODY').append(html);		
								}			
							    
							} else {
								html="<tr><td colspan=\"4\">No results found.</td></tr>";
								$('#customer_table TBODY').html(html);						
							}
							$( "#customer_table tr:even" ).css( "background-color", "#bbbbff" );
							$( "#customer_table tr:odd" ).css( "background-color", "#ffeeee" );
							$('#customer_table').show();

						}
					});
				}

				
				searchCustomers();
	});								
</script>
</head>
<body>
<header>java-spring-demo: Customer Search</header>
<nav><a href="${pageContext.request.contextPath}/home">Return to Home</a></nav>
<p id="description">v1 - This page displays a list of customers in a table that is populated by an AJAX call to the getCustomers service.</p>	
<hr/>	
<div class="table-contain">
	<h1>Customers</h1>
	<form id="searchCustomerForm" method="POST">
	    <fieldset class="customer-fs">
	      <input type="text" name="searchVal" id="searchVal" class="text ui-widget-content ui-corner-all">
	  	  <button name="search_submit" id="search_submit">Search</button> 
	    </fieldset>
	  </form>

	<table id="customer_table">
		<thead>
			<tr>
				<th>Last&nbsp;Name</th>
				<th>First&nbsp;Name</th>
				<th>User&nbsp;Name</th>
				<th>Birth&nbsp;Date</th>
				<th>&nbsp;</th>
			</tr>
		</thead>
		<tbody>
		</tbody>
	</table>
<button class="ui-button" id="update-customer-table">Refresh Table</button>
</div>
<footer>Page Generated: <%= new Date() %></footer>
</body>
</html>