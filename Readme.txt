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


Blurring and Convolutions:
    1. Filter2d - It is used to chnage the pixel intensity value based on surrounding values. It uses kernels and convolutes the 2d matrix
        a. Identity kernel
        b. Edge Detection kernel
        c. Sharpening kernel - np.array([[-1,-1,-1],
                                         [-1,9,-1],
                                         [-1,-1,-1]]) use this kenel with cv2.Filter2d(image,kernel)
        d. Blurring kernels
            d.1. regular Blurring uses cv2.blur()
            d.2. gaussian Blurring uses cv2.gGaussianBlur()
            d.3. Median blurring  uses cv2.medianBlur()
            d.4. kernel = np.ones((size,size),np.float32) / size**size use this kernel with cv2.Filter2d(image,kernel)


Thresholding:
Used to select areas of interest by differentiating dark and light parts of the image. It can help seperate dark and light side of a colourful image.
Achieve this using : cv2.threshold().  
IMPORTANT: Why blurring is important before thresholding? Answer: To remove Noise


Dilation, Erosion and Edge detection:
    1. Dilation: It adds pixels to the boundaries of objects of an image use cv2.dilate(image, kernel, iterations).
    2. Erosion: removes pixels from the boundaries of objects of an image use cv2.erode(image, kernel ,iterations).
    3. Opening: Dilation and then Erosion
    4. Closing: Erosion and then Dilation
    5. Edge detection : Can use cv2.Canny(). This function takes the first derivative (gradient) to find the edges of the image. The function takes 2 values 
                        thresh 1 and threh 2. Any gradient value greater than thres 2 is considered to be an edge. Any value lesser than thres 1 is not an edge. 
                        values in betweenn thresh1 and 2 are either classified as edges or non edges. 


