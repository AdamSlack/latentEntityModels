# Automatic Labelling of Topic Models (2011)
J.H.Lau, K.Grieser, D.Newmann, T.Baldwin

## Introduction

What is topic Modelling?
- Topic Models are popular
- Soft Clustering terms
- Form multinominal distributions
- Useful in document sumarisation tasks
- Useful in other NLP tasks

Generating Labels
- Common way involves use of 10 words with highest probability of association
- This paper follows a 3 step generation process
  1: Source candidate label set from wikipedia by querying with topic terms
  2: Identify top ranked document titles
  3: Process document titles to extract sub-strings
- Each topic label is translated into extracted wikipedia features
- Lexical association with topic terms in Wikipedia documents are generated
- lexical features for component terms are generated
- the outputs are used in a SVM to rank topic label candidates

paper contributions
- Novel evaluation framework and dataset for topic label evaluations
- methods for scoring and evaluating candidate topic labels
- positive results...

## Related Works

	
