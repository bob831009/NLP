<?php

include("mysql_connect.inc.php");

session_start();
$Level = $_POST['database'];
$Score = $_POST['score_kind'];
$speech = $_POST['speech'];
$subject = $_POST['subject'];

$filename = "./input.txt";
$file = fopen( $filename, "w" );
if( $file == false ){
   	echo ( "Error in opening file" );
   	exit();
}

if(count($_POST) > 0){
	$Word = $_POST['word'];
	$n = str_word_count($word);
	if($n > 1){
		$speech = "All";
	}
	$Level_trans = Input_to_Array($Level);
	$count_output = 0; 
	$score_cnt = array("A"=>0, "B"=>0, "C"=>0, "D"=>0);
	foreach($Level_trans as $Database){
		$DataLevel = database_to_table($Database);
		list($count_output, $score_cnt)= Query_function($file, $Score, $Database, $Word, $count_output, $score_cnt, $DataLevel, $subject, $speech);
	}

	echo "A 4~5: ${score_cnt['A']} occurrences(conditional probability: " . ($score_cnt['A']/$count_output) . ")<br>";
	echo "B 3~3.9: ${score_cnt['B']} occurrences(conditional probability: " . ($score_cnt['B']/$count_output) . ")<br>";
	echo "C 2~2.9: ${score_cnt['C']} occurrences(conditional probability: " . ($score_cnt['C']/$count_output) . ")<br>";
	echo "D 0~1.9: ${score_cnt['D']} occurrences(conditional probability: " . ($score_cnt['D']/$count_output) . ")<br>";
	echo ("<a href=\"http://nlp.csie.org/~bob831009/tag-project/input.txt\">input.txt</a>");
}

fclose($file);

function Query_function($file, $Score, $Database, $Word, $count_output, $score_cnt, $DataLevel, $subject, $speech){
	// print "Hi\n";
	// fwrite($file, "$Score");
	list( $Low , $High ) = Score_to_Bound($Score);
	if($Database == "Intermediate"){
		$word_table = "`Corpus_I_word`";
		$sent_table = "`Corpus_I_sent`";
		$doc_table = "`Corpus_I_document`";
		$feature_table = "`Corpus_I_document_feature`" ;
	}
	else if($Database == "High-Intermediate"){	
		$word_table = "`Corpus_HI_word`";
		$sent_table = "`Corpus_HI_sent`";
		$doc_table = "`Corpus_HI_document`";
		$feature_table = "`Corpus_HI_document_feature`" ;
	}
	else
		die("invalid databasse");

	$sql = "SELECT * FROM $word_table AS w 
			INNER JOIN $sent_table AS s ON w.`sid` = s.`id` 
			INNER JOIN $doc_table AS d ON s.`document_id` = d.`document_id`
			INNER JOIN $feature_table AS f ON d.`document_id` = f.`document_id`
			WHERE `word` = '$Word' 
			AND `score` BETWEEN $Low AND $High";

	if($subject != "All"){
		$sql .= "AND `subject`='$subject'";
	}
	$query = mysql_query($sql);
	$row = mysql_fetch_assoc($query);
	// echo "64";
	if($row == false){
		return array($count_output, $score_cnt);
	}
	fwrite($file, "Level ");
	foreach ($row as $cname => $cvalue) {
		if(check($cname)){
			continue ;
		}
		fwrite($file, "$cname ");
	}
	fwrite($file, "\n");
	mysql_free_result($query);

	// echo "78";
	$query = mysql_query($sql);
	while($row = mysql_fetch_assoc($query)){
		$tag = $row["tag"];

		$speech_array = speech_to_array($speech);
		foreach ($speech_array as $key => $speech) {
			if($speech == "All" || $tag == $speech){
				$count_output++;
				fwrite($file, "Level=$DataLevel ");
				foreach($row as $cname => $cvalue){
					if(check($cname)){
						continue ;
					}
					if($cname == "score"){
						$cvalue = ScoreToLetter($cvalue);
						$score_cnt[$cvalue]++ ;
					}
					fwrite($file, "$cname=$cvalue ");
				}
				fwrite($file, "\n");
			}
		}
	}
	return array($count_output, $score_cnt);
}

function speech_to_array($speech){
		switch ($speech) {
			case '$':
				$array = array("$");
			break;
			case '-LRB-':
				$array = array("-LRB-");
			break;
			case '-RRB-':
				$array = array("-RRB-");
			break;
			case 'CC (Coordinating conjunction)':
				$array = array("CC");
			break;
			case 'CD (Cardinal number)':
				$array = array("CD");
			break;
			case '\'CC\',\'CD\'':
				$array = array("CC","CD");
			break;
			case 'DT (Determiner)':
				$array = array("DT");
				break;
			case 'EX (Existential there)':
				$array = array("EX");
				break;
			case 'FW (Foreign word)':
				$array = array("FW");
				break;
			case 'IN (Preposition or subordinating conjunction)':
				$array = array("IN");
				break;
			case 'JJ (Adjective)':
				$array = array("JJ");
			break;
			case 'JJR (Adjective, comparative)':
				$array = array("JJR");
			break;
			case 'JJS (Adjective, superlative)':
				$array = array("JJS");
			break;
			case '\'JJ\',\'JJR\',\'JJS\'':
				$array = array("JJ","JJR","JJS");
				break;
			case 'LS (List item marker)':
				$array = array("LS");
				break;
			case 'MD (Modal)':
				$array = array("MD");
				break;
			case 'NN (Noun, singular or mass)':
				$array = array("NN");
			break;
			case 'NNP (Proper noun, singular)':
				$array = array("NNP");
			break;
			case 'NNPS (Proper noun, plural)':
				$array = array("NNPS");
			break;
			case 'NNS (Noun, plural)':
				$array = array("NNS");
			break;
			case '\'NN\',\'NNP\',\'NNPS\',\'NNS\'':
				$array = array("NN","NNP","NNPS","NNS");
				break;
			case 'PDT (Predeterminer)':
				$array = array("PDT");
			break;
			case 'POS (Possessive ending)':
				$array = array("POS");
			break;
			case 'PRP (Personal pronoun)':
				$array = array("PRP");
			break;
			case 'PRP$ (Possessive pronoun)':
				$array = array("PRP$");
			break;
			case '\'PDT\',\'POS\',\'PRP\',\'PRP$\'':
				$array = array("PDT","POS","PRP","PRP$");
				break;
			case 'RB (Adverb)':
				$array = array("RB");
			break;
			case 'RBR (Adverb, comparative)':
				$array = array("RBR");
			break;
			case 'RBS (Adverb, superlative)':
				$array = array("RBS");
			break;
			case 'RP (Particle)':
				$array = array("RP");
			break;
			case '\'RB\',\'RBR\',\'RBS\',\'RP\'':
				$array = array("RB","RBR","RBS","RP");
				break;
			case 'SYM (Symbol)':
				$array = array("SYM");
				break;
			case 'TO (to)':
				$array = array("TO");
				break;
			case 'UH (Interjection)':
				$array = array("UH");
				break;
			case 'VB (Verb, base form)':
				$array = array("VB");
			break;
			case 'VBD (Verb, past tense)':
				$array = array("VBD");
			break;
			case 'VBG (Verb, gerund or present participle)':
				$array = array("VBG");
			break;
			case 'VBN (Verb, past participle)':
				$array = array("VBN");
			break;
			case 'VBP (Verb, non-3rd person singular present)':
				$array = array("VBP");
			break;
			case 'VBZ (Verb, 3rd person singular present)':
				$array = array("VBZ");
			break;
			case '\'VB\',\'VBD\',\'VBG\',\'VBN\',\'VBP\',\'VBZ\'':
				$array = array("VB","VBD","VBG","VBN","VBP","VBZ");
				break;
			case 'WDT (Wh-determiner)':
				$array = array("WDT");
			break;
			case 'WP (Wh-pronoun)':
				$array = array("WP");
			break;
			case 'WP$ (Possessive wh-pronoun)':
				$array = array("WP$");
			break;
			case 'WRB (Wh-adverb)':
				$array = array("WRB");
			break;
			case '\'WDT\',\'WP\',\'WP$\',\'WRB\'':
				$array = array("WDT","WP","WP$","WRB");
				break;
			case 'All':
				$array = array("All");
			break;
		}
		return $array;
	}

function check($name){
	$arr = array("content", "sent", "parse_result_stanford");
	foreach ($arr as $remove_name){
		if($name == $remove_name)
			return 1;
	}
	return  ;
}

function ScoreToLetter($value){
	if($value <= 1.5) $Letter = "D";
	elseif($value <= 2.5) $Letter = "C";
	elseif($value <= 3.5) $Letter = "B";
	else $Letter = "A";

	return $Letter;
}

function database_to_table($value){
	switch($value){
		case "Intermediate":
			$table = "I";
			//$table = "IW";
		break;
		case "High-Intermediate":
			$table = "HI";
			//$table = "HIW";
		break;		
	}
	return $table;
}

function Input_to_Array($database){
	switch($database){
		case "Intermediate":
			$database_trans = array("Intermediate");
		break;
		case "High-Intermediate":
			$database_trans = array("High-Intermediate");
		break;
		case "All":
			$database_trans = array("Intermediate","High-Intermediate");
		break;	
	}
	return $database_trans;
}

function Score_to_Bound($score_kind){
	switch($score_kind){
		case "A":
			$Low = "4";
			$High = "5";
		break;
		case "B":
			$Low = "3";
			$High = "3.5";
		break;
		case "C":
			$Low = "2";
			$High = "2.5";
		break;
		case "D":
			$Low = "0";
			$High = "1.5";
		break;
		case "All":
			$Low = "0";
			$High = "5";
		break;
	}
	return array($Low,$High);
}