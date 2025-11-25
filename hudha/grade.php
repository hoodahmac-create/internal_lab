<html>
<body>
<h2>FORM CALCULATOR</h2>
<form method="post">
Enter Gade:<input type="number" name="grade" required>
<button type="submit">SUBmIT</button>
</form>
<?php
if(isset($_POST["grade"])){
	$grade=$_POST["grade"];
	if($grade<=50){
		echo "Failed";
	}elseif($grade<=60){
		echo "Grade is D";
	}elseif($grade<=70){
		echo "Grade is C";
	}elseif($grade<=80){
		echo "Grade is B";
	}elseif($grade<=90){
		echo "Grade is A";
	}elseif($grade<=100){
		echo "Grade is S";
	}
	else{
		echo "PLEASE enter a VALID mark";
	}
}
?>
</body>
</html>