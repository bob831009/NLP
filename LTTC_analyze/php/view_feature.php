<?php
include("mysql_connect.inc.php");

$sql = "SELECT * FROM `LTTC_feature`";
$query = mysql_query($sql);
$row = mysql_fetch_assoc($query);
foreach ($row as $cname => $cvalue) {
	print "$cname ";
}
print "\n";
mysql_free_result($query);

$query = mysql_query($sql);
while($row = mysql_fetch_assoc($query)){
	if($row["level"] == "HI"){
		foreach($row as $cname => $cvalue){
			print "$cname=$cvalue ";
		}
		print "\n";
	}
}
?>
