# PythonMatrix
An all python implementation of a matrix.

# Usage

You create a matrix by specifying the dimensions.
```python
from mat import *

# create a 2x3 matrix
a = Mat(2,3)

# fill it
for i in range(a.size(0)):
  for j in range(a.size(1)):
    a[i,j] = i+j
```

You can also specify an initial value for each of the elements.
```python
# create a 3x4 matrix and fill it with -2s
b = Mat(3,4,-2)
```

Matrix-matrix multiplication is done using the `.dot()` method.
```python
# multiply
c = a.dot(b)
```

Alternatively, you can do elemntwise or scalar multiplication using the `*` operator.
```python
# scalar multiplication
a = 3*a
```

Here's a simple example showing the use of `Mat` to create a single layer neural network.
```python
# simple one layer neural network
# 5 inputs, 10 hidden layers, 1 output, no bias terms
from math import exp
import random
def sigmoid(x):
  return 1.0/(1.0+exp(x))

def sigmoidGrad(x):
  s = sigmoid(x)
  return s*(1.0-s)
  
class Layer:
  def __init__(self,num_in,num_out,activation=None):
    self.ni = num_in
    self.no = num_out

    W = Mat(num_out,num_in)
    for i in range(Wxh.size(0)):
      for j in range(Wxh.size(1)):
        W[i,j] = 2*random.rand()-1 # fill with weights from -1 to 1
    if activation==None:
      self.activation = lambda x: x
    else:
      self.activation = activation
  
  def forward(X):
    linear = self.W.dot(X)
    return linear.applyfn(self.activation)
    
ni = 5
nh = 10
no = 1
Lih = Layer(ni,nh,sigmoid)
Loh = Layer(nh,no)

# create an arbitrary input, fill with 2s
X = Mat(5,1,2)
hidden = Lih.forward(X)
output = Loh.forward(hidden)
```

