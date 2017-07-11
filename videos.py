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
  <title>Hen Music</title>
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
  <div align="center" class=col-md-4>
   <img src="images/music2.jpeg">
  </div>
  <div align="right" class=col-md-8>
   <img src="images/music_man.jpeg">
 </div>
</div>
  <hr>
<p>
<div align="left" class=col-md-4>
<video width="320" height="240" controls>
  <source src="videos/coldplay-hymn_for_the_weekend" type="video/mp4">
</video>
<p><strong>Coldplay-hymn for the weekend</strong></p>
</div>
  <div align="center" class=col-md-4>
    <video width="320" height="240" controls>
    <source src="videos/Coldplay-Fix_You.mp4" type="video/mp4">
    </video>
<p><strong>Coldplay-Fix you</strong></p>
  </div>
<div align="right" class=col-md-4>
<video width="320" height="240" controls>
  <source src="videos/Alicia-Keys-Fallin.mp4" type="video/mp4">
</video>
<p><strong>Alicia Keys-Fallin</strong></p>
</div>


<hr>


<div align="left" class=col-md-4>
<video width="320" height="240" controls>
  <source src="videos/RollingStones-Anybody_seen_my_babe.mp4" type="video/mp4">
</video>
<p><strong>Rolling Stones-Anybody seen my babe</strong></p>
</div>
<div align="center" class=col-md-4>
    <video width="320" height="240" controls>
    <source src="videos/GeorgeEzra-Dont_Matter_Now.mp4" type="video/mp4">
    </video>
<p><strong>George Ezra-Dont matter now</strong></p>
  </div>
<div align="right" class=col-md-4>
<video width="320" height="240" controls>
  <source src="videos/EdSheeran-Galway_Girl.mp4" type="video/mp4">
</video>
<p><strong>Ed Sheeran-Galway Girl</strong></p>
</div>

<hr>

<div align="left" class=col-md-4>
<video width="320" height="240" controls>
  <source src="videos/EdSheeran-Sing.mp4" type="video/mp4">
</video>
<p><strong>Ed Sheeran-Sing</strong></p>
</div>
<div align="center" class=col-md-4>
    <video width="320" height="240" controls>
    <source src="videos/LuisFonsi-Despacito.mp4" type="video/mp4">
    </video>
<p><strong>Luis Fonsi-Despacito</strong></p>
  </div>

</html>
"""
