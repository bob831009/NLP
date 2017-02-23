LTTC_analyze <- function(level)
{
	library(arules);
	# library(arulesViz);
	if(level == "I"){
		file_path = "./I.txt" ;
		output_path = "./result_I"
	}else if(level == "HI"){
		file_path = "./HI.txt" ;
		output_path = "./result_HI"
	}

	data = read.transactions(file_path, format = "basket", sep=" ", rm.duplicates=TRUE);
	rules = apriori(data, control=list(verbose=F) ,appearance=list(rhs=c("pass=1", "pass=0") , default="lhs"));
	quality(rules) <- cbind(quality(rules), Conviction = interestMeasure(rules, c("conviction"), data))
	# do the sort
	rules.sort = sort(rules, by="lift");

	# remove the redundant
	if(level == "HI"){
		subset.matrix = is.subset(rules.sort , rules.sort);
		subset.matrix[lower.tri(subset.matrix, diag = T)] = NA;
		redundant = colSums(subset.matrix, na.rm = T) >= 1;
		rules.pruned = rules.sort[!redundant];
	}

	# print the log result to file
	output_path = paste(output_path, "log", sep=".");
	sink(output_path);
	if(level == "HI"){
		inspect(rules.pruned);
	}else if(level == "I"){
		inspect(rules.sort);
	}
	sink();
}