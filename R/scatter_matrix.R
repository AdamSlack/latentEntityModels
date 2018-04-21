library(readr)
library(lattice)
library(ggplot2)
library(GGally)
e_class = read_csv("~/github/latententitymodels/results/hp_full_latent_entity_classification.csv")
e_class[1] = NULL

e_class[c("class")] <- lapply(e_class[c("class")], function(x) x+1)

pairs(e_class[1:10], pch=4, cex.labels=2, col=e_class$class, oma=c(4,4,20,20))
par(xpd = TRUE)
legend( "topright", fill = unique(c("1","2","3","4","5")), 
                       legend = c( unique(e_class$class) ) )