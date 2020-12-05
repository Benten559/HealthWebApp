<?php
//session_start();

$conn = mysqli_connect('localhost',"root","");

$con = mysqli_select_db($conn, "login");
if($con == true){echo"TRUE";}
else{ echo"False";}

$name = $_POST['uname'];
$pass = $_POST['psw'];

$s = " select * from usertable where name = '$name'";

$result = mysqli_query($con, $s);

$num = mysqli_num_rows($result);
echo '<script>alert($name)</script>';
/*
if($num == 1){
echo" Username Already Taken";
}else{
$reg = "insert into usertable(name, password) values ('$name', $pass')";
mysqli_query($con, $reg);
echo"Registration Successful";
}
*/
?>
