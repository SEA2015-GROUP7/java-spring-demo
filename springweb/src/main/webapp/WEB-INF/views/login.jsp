<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!doctype html>
<html lang="en">
<head>
<link rel="stylesheet" type="text/css" href="..//WEB-INF/login.css">
<style>body{
	background: eeeeee;
	margin: 0 auto;
	width: 960px;
	padding-top: 50px}
	.footer{
		margin-top:50px;
		text-align:center;
		color:#666;
		font:bold 14px Arial}
		.footer a{
			color:#999;
			text-decoration:none}
				.login-form{margin: 50px auto;}  
  
</style>
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.11.1/jquery-ui.js"></script>
<script>
$(document).ready(function() {
 
    // Check if JavaScript is enabled
    $('body').addClass('js');
 
    // Make the checkbox checked on load
    $('.login-form span').addClass('checked').children('input').attr('checked', true);
 
    // Click function
    $('.login-form span').on('click', function() {
 
        if ($(this).children('input').attr('checked')) {
            $(this).children('input').attr('checked', false);
            $(this).removeClass('checked');
        }
 
        else {
            $(this).children('input').attr('checked', true);
            $(this).addClass('checked');
        }
 
    });
 
});
</script>
</head>
<body bgcolor="gray">
<div class="login-form"> 
    <h1>Login Form</h1>
    <form action="#">
        <input type="text" name="username" placeholder="username">
        <input type="password" name="password" placeholder="password">
        <span>
            <input type="checkbox" name="checkbox">
            <label for="checkbox">remember</label>
        </span>
        <input type="submit" value="log in">
    </form>
</div>
</body>
</html>