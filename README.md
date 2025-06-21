## Two-Layer Convolutional Neural Network (CNN) Implementation

I developed a two-layer CNN in Python with:
- 5 input nodes, 4 hidden nodes and 1 output node,
- with fixed weights ( $w_1 = 1.2$, $w_2 = -0.2$, $v_1 = -0.3$, $v_2 = 0.6$, $v_3 = 1.3$, and $v_4 = -1.5$)
- and ReLU activation at each layer. 


The function `convnet(x)` implements forward propagation to perform automatic differentiation with respect to one of the weights $w_1$:
It will take in a 5-dimensional input vector $x$ and return all ordered pairs $(u,u')$ at all hidden and output nodes.



<img src="https://github.com/user-attachments/assets/a7f38744-33fe-40aa-82dd-a9fcbab37f6a" width="300">


### Skills demonstrated
- a mathematical understanding of CNNs and automatic differentiation
- a modular implementation of an algorithm as a single Python function
- application of object oriented programming
