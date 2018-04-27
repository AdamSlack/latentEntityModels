library(readr)
library(lattice)
library(ggplot2)
library(GGally)
e_class = read_csv("~/github/latententitymodels/results/test/full_entities_50_classification.csv")
e_class[1] = NULL

e_class[c("class")] <- lapply(e_class[c("Class")], function(x) x+1)

pairs(e_class[1:10], pch=4, cex.labels=2, col=e_class$Class)
#hp_etms_summary