<?php

if (isset($_POST['detectbtn']))
{
	exec("cutsTest.py");
	exec("testLogs.py");
}

header('Location:../pages/charts/flot.html');

?>
