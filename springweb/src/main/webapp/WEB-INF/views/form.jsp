<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Spring Web App with JQuery</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.11.1/themes/smoothness/jquery-ui.css">
  <script src="//code.jquery.com/jquery-1.10.2.js"></script>
  <script src="//code.jquery.com/ui/1.11.1/jquery-ui.js"></script>
  <script>
  $(function() {
	    $( "#title" ).selectmenu();
	    $( "#country" ).selectmenu();
	    $( "#state" ).selectmenu();
	    $( "#submit" ).button();
	});

  $.getJSON('json/getTitles', function(data){
	    var html = '';
	    var len = data.length;
	    for (var i = 0; i< len; i++) {
	        html += '<option value="' + data[i].id + '">' + data[i].name + '</option>';
	    }
	    $('#title').append(html);
	});

  $.getJSON('json/getCountries', function(data){
	    var html = '';
	    var len = data.length;
	    for (var i = 0; i< len; i++) {
	        html += '<option value="' + data[i].id + '">' + data[i].name + '</option>';
	    }
	    $('#country').append(html);
	});
  
  $.getJSON('json/getStates', function(data){
	    var html = '';
	    var len = data.length;
	    for (var i = 0; i< len; i++) {
	        html += '<option value="' + data[i].id + '">' + data[i].name + '</option>';
	    }
	    $('#state').append(html);
	});
  </script>
  <style>
    fieldset {
      border: 0;
    }
    label {
      display: block;
      margin: 20px 0 0 0;
    }
    select {
      width: 300px;
    }
    .overflow {
      height: 100px;
    }
  </style>
</head>
<body>
 
<div class="formDemo">
 
<form action="#">
    <fieldset>
	  <label for="title">Title</label><select name="title" id="title"></select><br/>
	  <label for="country">Country</label><select name="country" id="country"></select><br/>
	  <label for="state">State</label><select name="state" id="state"></select><br/>
	  <button name="submit" id="submit">Submit</button> 
	</fieldset>
</form>
 
</div>
 
</body>
</html>