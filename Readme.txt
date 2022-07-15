Dataset from kaggle: https://www.kaggle.com/competitions/dogs-vs-cats/data
Image processing : https://theailearner.com

Important Notes:
Tranpose: Can be used to rotate the image but is less flexible

Flip: Used to flip the image

Affine Transofrmations: These are transformation where collinearity, parallelism and ratio of distances between points are preserved

Perspective transformations: Does not preserve collinearity, parallelism and ratio of distances between points. 

Image enhancement : Done either in Spatial domain or transformation domain. Spatial domain means all operations are performed on pixel.
Transformation domain involves, transforming the image into another domain to perform the transformation then an inverse transformation is applies
to get the image back to spatial domain. 
    some simple techniques are as follows:
    1. Image averaging
    2. Image subtraction
    3. Image multiplication