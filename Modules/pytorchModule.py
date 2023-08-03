import torch
import numpy as np


x = torch.empty(1)  # tensor of 1x1
x = torch.empty(3)  # tensor of 1x3
x = torch.empty(3, 3)  # tensor of 3x3 and so on

x = torch.rand(2, 2)   # tensor of 2x2 with random values
x = torch.ones(2, 2)   # tensor of 2x2 with ones
x = torch.zeros(2, 2)   # tensor of 2x2 with zeros

print(x.dtype)
print(x.size())

x = torch.ones(3, 3 , dtype=torch.float64)   # tensor of 2x2 with ones having float64 as datatype

# tensors from python datatypes 

y = torch.tensor([2.5, 0.1])

# operations bw tensors: elements wise not matrix
y = torch.ones(3, 3)
z = x + y #or
z = torch.add(x, y)  #or

print(z)

y.add_(y)  # updating y to y+y

# similarly we also have sub for substract, mul for multiply, div for division

# slicing is as per regular python syntex

print(x[1, 1].item())  # .item() fetches the value of the item 

# reshaping

y = x.view(9, 1)  # reshaping 3x3 to 9x1
y = x.view(-1, 3) # reshaping a tensor when we know one dimension as per need other is decided by torch

x = torch.ones(5)

y = x.numpy()
print(type(y))

x = torch.from_numpy(y)  # numpy to tensor

# autograd
x = torch.rand(3, requires_grad=True)

y = x + 2  # if we provide require_grad=True we will get a backward function 

print(y)

# grad can be implicitly created only for a scaler outputs
# to calculate grad for a vector we have to pass the vector to backward function
"""
how to stop pytorch to create a backward function for a tensor 
 1. x.requires_grad_(False)
 2. x.detach()   # creating a copy of x with grad = False
 3. with torch.no_grad() """

