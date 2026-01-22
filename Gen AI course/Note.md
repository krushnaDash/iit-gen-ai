ANI : Artifical narraow intelligence (achived)
AGI : Artificial General Intelligence (middle)
ASI: Artificial Super Intelligence (future)


We foucused on ANI, artifical narraw intelligence

computer vision
natural language processing
speech recognition
machine learning
Planing


AI
    Machine Learning
    Deep Learning : ANN (artificial neural network)
    Generative AI

Brief History of AI

1950 : Can machine think
1956 : The dart mouht conference
1970 : AI winter, abrupt halt of AI research
1990 : AI SPring, AI Renaissance
2017 : RISE of LLM and Gen AI


Alant Turing
    Can machine Think ?, if so should you tell ?

Turing Test : A test to identify if a machine can think like a human.


ALPAC: autometic Language processing Advisory Committe, stop the funding as they not much growth

Why this happen ?
    -> Limitited computation
    -> Limitied information

Knowledge based system (1970 and 80), thses are rule based system example like below
MYCIN : Medical diagnosis
DENDRAL : Chemical analysis
XCON : Computer configuration

1943 : Intro to Neural Net
1969 : Perceptrons book showed that linear model could not solve XOR problem and killed nural nets research.

1985: Bayesian network
1995: Support vector machine
1999: Variational inference
2001: conditional random field
2003: Topic modeling
2006: Unsupervised layerwise pre-training of deep netowrks
2012: AlexNet obtains huge gains on Object recognition and transfer computer vision
2015: Attention mechanism is introduced in computer vision
2016: AlphaGo beats world champion in AI, uses deep reinforcement learning
2017: Transformer model, LLM and Generative AI

Rule-Based Expert system

Objective was to come of with some rules and that take automatically decsion for a particulae situation.
    ->it is a computer program with expert knowledge about a particular problem.
    ->in the form of a set of ruls, written with a set of if else statements.
    Its able to solve problems in that domain by applying the rules which is equivalent to human expert.

Objective
    -> To transfer the expertise from human expert to a computer system.
    -> Then on to non-expert, use the computer system to take decsion like human expertise
    
   Knowledge base -> interface -> inference engine -> output

   Rule represent a model of actual expert knowledge.

Chrastcis :
    Its prsever the expertise from human expert.
    It can be used by non-expert users.
    It can be updated with new knowledge and rules as the domain evolves.

 Limitation:   
    Knowledge is not readily avaliable
    Expertise can be hard to extract from humans
    Expert system work well in a narrow domain of knowledge
    Knowledge engineer are rare and expensive.
    
Machine Leraning
 Instead of if else, lets learn from the association of data. 
 
 classification, clustering and regression

 Deep learning
    -> Autometic Feture Generation
    -> Rrepresentation Learning

    Data, Large models, GPU needed for deep learning

    Feedforward Neural net FNN
    Convolutional Neural net - CNN
    Recurrent Neural net - RNN

Feedforward Neural net  
 Each layer is fully connected to the next layer.

RNN for sequence data

Generative AI
Supervise learning programs, they generate new stuffs.
Transfomer models, encoder and decoder architecture.

GPT : Generative Pre-trained Transformer

Agnetic AI:
 Agents: Preception and goals , agent monitor data and environment and take action to achieve goals.
 Intelligence : LLMs provide reasoning and planning capabilities to agents.
 Tools : Agents can use tools to interact with the environment.
 Actions : Agents take actions to achieve goals.



Why do modern generative models sometimes produce hallucinations?
Its hallccinate a particular thing and take decision based on that.
Some time it can generate a thing which is not possible or not exist.
This is because the models are not given the context of the data they are generating.


Transformer Model

-> Projection
-> Feed Forward Nerual network and its matrix from
-> soft max
-> Layer Normalization

Projection and Learning
  
What is Transformer ?

A nural network that processes sequnatial data, understand the context and perfroms a set of tasks

* classicfication
* Translation
* Language understanding

Transformer is Encoder and Decoder architecture.
Encoder: 

Embeding + Positional encoding -> Self-Attention -> Feed Forward -> Layer Normalization
raw vector then and multiple layer for tranformation

Encoder consist of 6 identical blocks, like the same layer repeated 6 times.

Ve0->E1->E2->E3->E4->E5->E6 -> Ve6
     Ve1->Ve2->Ve3->Ve4->Ve5->Ve6


The encoder in transformer is made up of 6 identical blocks, like the same layer repeated 6 times as per the original paper.
Each block has three main components excluding embedding: Multi-head attention, Feed forward network and  Add and normalize.

Embedding: 
-> Converts the input tokens to dense vector representation
-> Maps the discrete token to continuous vector
-> Enables modles to work with numerical representation of text

Multi-head attention: 
->It is the application of self attention mechanism on the input token multiple time 
to generate various kind of representation.
->Each self attention produce the output vector
-> For each vector the self attention generte the Queries, Key and Value vector
-> Then compute the attention(Q,K,V)= softmax(QK^T/SQRT(dk))V, which is nothing 
but to contextual dependencies and relationships between all tokens regardless of distance


 
Feed forward network: 
-> Each layer is fully connected to the next layer

Add and normalize
   -> It takes the embedding vector and add it to the output of the feed forward network 
    Then it normalizes the result
    -> It adds the original data along with fine tune vector to reduce the noise
So the Add operation is for adding the original data and normalize os for normalize data.


Decoder: 
Embeding + Positional encoding -> Self-Attention -> Feed Forward -> Layer Normalization
It has Masked multi-head Self-Attention
Multi-head cross-attention

Masked self attention: 

Multi-head cross-attention
    -> Interplay between encoder and decoder
    -> Quires come from the previous decoder layer
    -> Key and Value come from the encoder



Positional encoding
->Postion will be a vector
