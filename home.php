<?php
session_start();

?>
<html>
<head><h1>My first php code</h1><head>

<body>
<h1>Welcome <?php echo $_SESSION['username']; ?></h1>
</body>
</html>
