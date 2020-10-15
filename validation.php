
<?php
$name = $_POST['uname'];
$pass = $_POST['psw'];

$conn = mysqli_connect('localhost',"root","");

$con = mysqli_select_db($conn, "login");

$reg = "insert into usertable(name, password) values ('$name','$pass')";
mysqli_query($conn ,$reg);
?>
</body>