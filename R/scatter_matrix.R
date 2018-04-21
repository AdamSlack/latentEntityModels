library(readr)
library(lattice)
library(ggplot2)
library(GGally)
e_class = read_csv("~/github/latententitymodels/results/hp_summary_latent_entity_classification.csv")
e_class[1] = NULL

e_class[c("class")] <- lapply(e_class[c("class")], function(x) x+1)

pairs(e_class[1:10], pch=4, cex.labels=2, col=e_class$class)
#hp_etms_summary