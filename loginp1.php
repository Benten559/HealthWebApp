<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>wellness support center</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class ="top">
      <a href="#" class="w3-button w3-block w3-black">HOME</a>
      <a href="#about" class="w3-button w3-block w3-black">ABOUT</a>
      <a href="#menu" class="w3-button w3-block w3-black">MENU</a>
      <a href="#where" class="w3-button w3-block w3-black">WHERE</a>
  </div>
<ul class="nav">
  <li><a href="#home">Home</a></li>
  <li><a href="#about">About Us</a></li>
  <li><a href="#clients">Our Clients</a></li>  
  <li><a href="#contact">Contact Us</a></li>
</ul>

	<h1><center>WELLNESS SUPPORT CENTER</center></h1>
  <div class="imgcontainer">
    <img src="img_avatar2.png" alt="Avatar" class="avatar">
  </div>
  	<form action="validation.php" method="post">
  <div class="container">
    <label for="uname"><b><center>Username </center></b></label>
    <input type="text" placeholder="Enter Username" name="uname" size="4" required>

    <label for="psw"><b><center>Password</center></b></label>
    <input type="password" placeholder="Enter Password" name="psw" size="4" required>

    <button type="submit">Login</button>
    <label>
      <input type="checkbox" checked="checked" name="remember"> Remember me
    </label>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <button type="button" class="cancelbtn">Cancel</button>
    <span class="psw">Forgot <a href="#">password?</a></span>
  </div>
</form>
</body>
</html>
