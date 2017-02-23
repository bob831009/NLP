LTTC_analyze <- function()
{
	library(arules);

	file_path = "./input.txt";
	output_path = "./output";

	data = read.transactions(file_path, format = "basket", sep=" ", rm.duplicates=TRUE);
	rules = apriori(data, control=list(verbose=F) ,appearance=list(rhs=c("score=A", "score=B", "score=C", "score=D") , default="lhs"), parameter= list(supp=0.2, conf=0.2));
	quality(rules) <- cbind(quality(rules), Conviction = interestMeasure(rules, c("conviction"), data))
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
	inspect(rules.pruned);
	sink();
}