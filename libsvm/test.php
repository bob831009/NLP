<?php
include("mysql_connect.inc.php");

$word_table = "`Corpus_I_word`";
$sent_table = "`Corpus_I_sent`";
$doc_table = "`Corpus_I_document`";
$feature_table = "`Corpus_I_document_feature`" ;
$Word = "good" ;

$sql = "SELECT * FROM $word_table AS w 
		INNER JOIN $sent_table AS s ON w.`sid` = s.`id` 
		INNER JOIN $doc_table AS d ON s.`document_id` = d.`document_id`
		INNER JOIN $feature_table AS f ON d.`document_id` = f.`document_id`
		-- WHERE `word` = '$Word' 
		ORDER BY RAND()
		LIMIT 10000";

$query = mysql_query($sql);
// $i = 0;
while($row = mysql_fetch_assoc($query)){
	// $i = $i + 1;
	foreach($row as $cname => $cvalue){
		print "$cname=$cvalue ";
	}
	print "\n";
}
// print "$i";
?>
