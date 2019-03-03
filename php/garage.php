
<?php
	
	$date1 = $_POST['firstd'];
	$time1 = $_POST['secondt'];
	// $result = exec("python ../loadmodel.py '2019-03-20' 2");
	$result = exec("python ../python/1.py");
    echo json_encode($result);
 
?>
