<?php
include("mysql_connect.inc.php");

$sql = "SELECT * FROM `LTTC_feature`";

$info = mysql_query($sql);
$column = array();
while($row = mysql_fetch_array($info)){
	foreach ($row as $cname => $cvalue) {
    	$column[$cname][] = $row[$cname];
    }
}
mysql_free_result($info);

$query = mysql_query($sql);
$row = mysql_fetch_assoc($query);
foreach ($row as $cname => $cvalue) {
	sort($column[$cname]);
	$total_num = count($column[$cname]);
	$table[$cname]["Quar1"] = ($column[$cname][floor($total_num*3/4)]);
	$table[$cname]["Quar2"] = ($column[$cname][floor($total_num*1/2)]);
	$table[$cname]["Quar3"] = ($column[$cname][floor($total_num*1/4)]);

	print "$cname ";
}
print "\n";
mysql_free_result($query);

$query = mysql_query($sql);
while($row = mysql_fetch_assoc($query)){
	if($row["level"] == "I"){
		foreach($row as $cname => $cvalue){
			if($cname == "document_id" || $cname == "score"){
				print("$cname=$cvalue ");
			}elseif($cvalue > $table[$cname]["Quar1"]){
				print "$cname=1 ";
			}elseif($cvalue > $table[$cname]["Quar2"]) {
				print "$cname=2 ";
			}elseif($cvalue > $table[$cname]["Quar3"]){
				print "$cname=3 ";
			}else{
				print "$cname=4 ";
			}
		}
		print "\n";
	}
}
?>