<?php

if (isset($_POST['detectbtn']))
{
	exec("cutsTest.py");
}

header('Location:../pages/charts/flot.html');

?>
