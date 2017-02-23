<?php
include("mysql_connect.inc.php");

$sql = "SELECT * FROM `Corpus_I_document_feature`";
$sql_score = "SELECT score FROM `Corpus_I_document`";
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
	$table[$cname]["Quar3"] = ($column[$cname][floor($total_num*3/4)]);
	$table[$cname]["Quar2"] = ($column[$cname][floor($total_num*1/2)]);
	$table[$cname]["Quar1"] = ($column[$cname][floor($total_num*1/4)]);

	print "$cname ";
	if($cname == "document_id")
		print "pass ";
}
print "\n";
mysql_free_result($query);

$query = mysql_query($sql);
$query_score = mysql_query($sql_score);
while($row = mysql_fetch_assoc($query)){
		$row_score = mysql_fetch_assoc($query_score);
		foreach($row as $cname => $cvalue){
			if($cname == "document_id"){
				print("$cname=$cvalue ");
				foreach($row_score as $key => $value){
					if($value >= 4)
						print("pass=1 ");
					else
						print("pass=0 ");
				}
			}elseif($cvalue > $table[$cname]["Quar3"]){
				print "$cname=4 ";
			}elseif($cvalue > $table[$cname]["Quar2"]) {
				print "$cname=3 ";
			}elseif($cvalue > $table[$cname]["Quar1"]){
				print "$cname=2 ";
			}else{
				print "$cname=1 ";
			}
		}
		print "\n";
}
?>
