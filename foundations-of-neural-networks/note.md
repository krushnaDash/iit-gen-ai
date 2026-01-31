What is a Neuron

-> A neuron is a basic processing unit of a neural network
-> Given serval inputs x1, x2, x3, ...xn, and corresponding weights w1, w2, w3, ...wn, the neuron computes the weighted sum of the inputs and passes it through an activation function to produce an output.
-> Mathematically, the output of a neuron can be expressed as:

    y = f(w1x1 + w2x2 + w3x3 + ... + wnxn + b)

    where y is the output of the neuron, f is the activation function, and b is the bias term.

-> The activation function is a non-linear function that introduces non-linearity into the model, allowing it to learn complex patterns in the data.

Activation functions:
    a. is a setp function or threshold function
    b. is a sigmoid function 1/(1+e^(-x)) (this one is used in binary classification)
    c. is a hyperbolic tangent function tanh(x)
    d. is a rectified linear unit (ReLU) function max(0,x)
    e. is a softmax function exp(x)/sum(exp(x)) (this one is used in multi-class classification)
    f. is a Leaky ReLU function max(0.01x,x)
    g. is a maxout function max(w1^Tx + b1, w2^Tx + b2)
    h. is a ELU function {x if x >= 0, alpha(e^x - 1) if x < 0}



-> The bias term is a constant term that is added to the weighted sum of the inputs to allow the model to learn an intercept.

-> The output of a neuron is then passed to the next layer of the network, where it is used as an input to another neuron.

-> The output of the final layer of the network is the final output of the model.

Preceptron : 1-layer neural network, not able to sove the XOR problem

Feed forward Neural Network
    Many neuran are organized into layers

Layer 0 -> Layer 1 .. Layer n


Compostion of Transformations:
    Representation Lerning:

How to train a Neural Network:
    1. Make prediction
    2. Compute loss
    3. Calculate gradient of the loss function w.r.t parameters
    4. Update the parameters by taking a step in opposite direction of gradient
    5. iterate

Gradient Descent:
    
How could you change the wegihts to make our Loss Functions lower ?
    Consider the Loss Function as a function of weights F: x -> Y
    