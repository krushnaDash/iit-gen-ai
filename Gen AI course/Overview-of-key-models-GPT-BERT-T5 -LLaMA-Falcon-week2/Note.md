Transfer with 2 stacked encoder-decoder

decoder used for generation, token by token

Three architectures for LLMs

Pre trained on : Decoders (GPT, Claude, Llama, Falcon)
Pre trian on :Encoders (BERT family)
Pre trained on Both : Falcon T5 and BART



A model can learn from the pre training task and ready to be used for downstream task.
Cross entropy loss is used for classification tasks

Pre train Encoder : By using the masked language model (MLM) task, the model learns to predict the masked tokens in the input sequence. 
I went to the store -> I [mask] to the [mask] 
-> 15% token will be masked
Another solution can be used is by reodering the word, or replace it with a random word.

More details about BERT.

BERT base : 12 layers, 768 hidden dimension, 110M parameters
BERT large : 24 layers, 1024 hidden dimension, 340M parameters

BERT vocab size : 30,522


Trained On:
-> BookCorpus (800 Million words)
-> Wikipedia (2500 Million words)

Pretraing is expensive and impractical on a single GPU
-> BERT was pretrained on 64 TPUs chips for a total of 4 days
-> Finetune is practical on a single GPU
Pretrain once and finetune many times

-> CLS : token can be used in BERT like models for classification tasks

Text classification 3 class -> Positive, Negative, Neutral
number of extra parameters :  hidden dimension * number of classes + number of classes

Fine Tuning for sequence classification:
-> Add a classification head on top of the [CLS] token output
-> Classification head: Linear layer mapping hidden_dim → num_classes

T5: Text to text transfer
For T5 we don't need to add any additional parameters.




RoPE-> Rotary Positional Embeddings
Positional encoding is a way to encode the position of a token in a sequence.


Sinusoidal Positional Encoding: are based on hard-coded values of all dimension of an embedding vector.

ei=Xi+PE(i)
Rotary Positional Encoding: are based on rotations of query and key vectors.

ei=XiR(i)
Where R(i) is a rotation matrix that depends on the position i.

Ro(X, θ) =XR(θ)
Example of two dimensions token embedding: [x1,x2]= [cos(θ), sin(θ)]
                                                    [-sin(θ), cos(θ)] 
                                                    =[cos(θ).x1-sin(θ).x2, sin(θ).x1+cos(θ).x2] 

Every two dieminsion can be create an pair of rotation matrix and can be rotate by θ.

Given that the distance between cat and sleeping is same in both the sentence , the angle between the rotation matrix will be same.





Show that the self-attention score in the rotatory embeddings depends on the positional difference between the query and key.

