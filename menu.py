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
  <title>Hen's Menu</title>
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

<style>
.img {
    float: left;
    width: 150px;
    height: 75px;
    margin: 10px;
    border: 3px solid #73AD21;  
}
</style>
</head>
<body>
<div>
<a href="http://54.72.48.152/index.py" target="_blank">
  <img width="420" height="250" border="0" align="right"  src="images/bookkeeping.jpeg"/>
</a>

<a href="http://54.72.48.152/videos.py" target="_blank">
  <img width="420" height="250" border="0" align="left"  src="images/music_menu.jpeg"/>
</a>
</div>
<hr>
</body>
</html>
"""
