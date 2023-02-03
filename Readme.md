# Pytorch Fundamentals


1. Tensor : 
A algebraic object that describes a multilinear relationship between sets of algebraic objects

2. Scalar : 
It is a algebraic object that has only magnitude. Scalar has 0 dimensions

3. Vetor : 
It has both magnitude and direction. Number of closing square bracket is 1 dimension.

4. Random tensors : 
torch.random()is used to generate random tensors. These are important because, most of the neural networks start with random numbers and adjust the numbers to better represent the data.
    -example: start with random numbers - > look at data - > update random numbers - > look at data -> update

5. Zeros and Ones : 
These tensors can be used for masks

6. Like : 
Sometimes there might be a need to make a new tensor of the shape as an existing tensor. for such scenerios like is used. There are a few different type of like. Zeros_lie, full_like are a few examples.

7. Dtypes : 
Even if the dtypes are given as none. The dtype of tensor will be float 32. 

8. While creating a tensor there are 3 different types of attributes. They are as follows
    -dtype : to mention the data type
    -device : It tells what device the tensor is on
    -requires_grad = True/False : used to tradck gradient decent. This helps to track the performance of the neural network.

9. **IMPORTANT** Tensor datatype errors are of 3 types. These are common big errors that arise in Pytorch and deep learning. They are as follows:
    Tensor not right data type.
    Tensor not right shape
    Tensor not on right device

10. Tensor Multiplication: Two types: 
Element wise muiltiplication, Matrix Multiplication (Dot product).
**TWO RULES**
    -THE **INNER DIMENSIONS** must match: (3,2) matmul (3,2) will not work. (3,2) matmul (2,3) will work.
    -The resulting matrix has the shape of **Outer Dimensions**
