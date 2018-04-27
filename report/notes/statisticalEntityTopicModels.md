# [Statistical Entity-Topic Models](https://dl.acm.org/citation.cfm?doid=1150402.1150487)

D.Newman, C Chemudugunta, P Smyth

## Abstract

The purpose of news articles are to convey info

Summarising relationships is hard

topic models are successful at what they do

topic models don't exlplicitly address issues

entity-topics are better at making predictions about relationships between entities

## Introduction

News articles convey info about who, what, when and where.

topic models can't distinguish between these

many applications require this distinction

Paper considers the problem of modelling text corpora

corpora contain classes of words: people, places, organisations

topic models use simple assumption that documents are distributions of topics

effective at expressing documents in terms of fixed topics

many applications of this.

increased interest in identifying and analysing entities in text

not focused on NER or Entity Resolution

focus on making predictions after their extraction from text

## Related Work

Blei et al.'s LDA has been taken in numerous diections
Griffiths and Steyvers used Gibbs Sampling
Steyvers et al.'s author-topic models
McCallum et al.'s author-topic-recipient model
Griffith et al.'s hidden-markov topic models for seperating semantic and syntactic topics
Blei's correlated topic model
Buntine's PCA Models

This paper focuses on the intersection of Entity Modelling and topic Modelling

Topic models have been extended to include additional information
- Steyvers et al.'s author topic model
- Blei and Jordan modelled images and captions

Entity Modelling related to this involve
- entity recognition
- entity resolution
- entity social networks
Work includes
- McCallum et al. use conditional random fields for noun co-references
- Zhu et al. use non-probabilistic latent semantic indexing for recognising and relating entities

This paper uses simple and effective NER techniques to extract entities (as pre-processing)

Primary goal is not that, its really the relating of entities, topics and words

## Data Sets

Text Data sets rich in entities

They felt News articles are ideal.

First data set is a collection of NY Times articles

Second data set is a collection of articles from Foreign Broadcast Information Service

Named entities are extracted from the data sets (nouns)

Two tools were considered - ANNIE and Coburn's Perl tagger (based on brill's HMM POS tagger)

NY times entities were extracted using Coburns tagger.

Some entities occurred frequently

FBIS 'PERSONS' entities were extracted using ANNIE, locations were omitted

Some entities occurred frequently

