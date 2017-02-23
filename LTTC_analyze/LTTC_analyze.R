LTTC_analyze <- function(level, score)
{
	library(arules);
	# library(arulesViz);
	if(level == "I"){
		file_path = "./LTTC_level=I_quar.txt" ;
		output_path = "./result_I"
	}else if(level == "HI"){
		file_path = "./LTTC_level=HI_quar.txt" ;
		output_path = "./result_HI"
	}

	if(score == "high"){
		tmp_c = c("score=4", "score=4.5", "score=5");
		output_path = paste(output_path, "high", sep="_");
	}else if(score == "low"){
		tmp_c = c("score=1", "score=1.5", "score=2", "score=2.5", "score=3", "score=3.5");
		output_path = paste(output_path, "low", sep="_");
	}

	data = read.transactions(file_path, format = "basket", sep=" ", rm.duplicates=TRUE);
	rules = apriori(data, control=list(verbose=F) ,appearance=list(rhs=tmp_c, default="lhs"));
	# quality(rules) <- cbind(quality(rules), Conviction = interestMeasure(rules, c("conviction"), data))
	# do the sort
	rules.sort = sort(rules, by="lift");

	# remove the redundant
	subset.matrix = is.subset(rules.sort , rules.sort);
	subset.matrix[lower.tri(subset.matrix, diag = T)] = NA;
	redundant = colSums(subset.matrix, na.rm = T) >= 1;
	rules.pruned = rules.sort[!redundant];

	# print the log result to file
	output_path = paste(output_path, "log", sep=".");
	sink(output_path);
	inspect(rules.sort);
	sink();
}