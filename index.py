#!/usr/bin/python
import os
import cgi,cgitb,os,io

print "Content-type:text/html\r\n\r\n"
print
print """
<!DOCTYPE html>
<html lang="en">
<meta charset="ISO-8859-1">
<head>
    <meta charset="UTF-8">
  <title>Tax Adjustments</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://code.jquery.com/jquery-2.0.3.js"></script>
</head>
<body>
<div class="container">
  <div class="jumbotron">
    <center><h2>Good Morning my princess !</h2></center>
      <center><h2>Let's do some Tax Adjustments . . .</h2></center>
  </div>
  <hr>

    <form action="upload-manager.php" method="post" enctype="multipart/form-data">
        <h4><p class="bg-primary">Please browse for Excel file . . .</p></h4>
        <input type="file" name="photo" id="fileSelect">
        <input type="submit" name="submit" value="Upload">
    </form>

<hr>  
</body>
<form action="shell.php">
    <input type="submit" value="Compare">
</form>
<script>
 $("#button").click(function(){
        $.ajax({
                url:"compare.py",
                type:"POST"});
	}
</script>
</html>
"""
