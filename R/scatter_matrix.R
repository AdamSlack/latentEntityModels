library(readr)
library(lattice)

e_class = read_csv("~/github/latententitymodels/results/entity_classification.csv")
e_class[1] = NULL

e_class[c("class")] <- lapply(e_class[c("class")], function(x) x+1)
pairs(e_class[1:10], col=e_class$class)
