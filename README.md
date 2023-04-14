# Images-Analysis
This practical was to gain brief knowledge about the mechanism of storing images in  computers, enhancing images in the intensity domain and extracting the spectral information out  of RGB images. 

# ABSTRACT
The main purpose of this practical was to analyze the images with using Python 03 and this 
practical was mainly based on the basic level of image processing therefore, the main objective 
of this practical was to gain brief knowledge about the mechanism of storing images in 
computers, enhancing images in the intensity domain and extracting the spectral information out 
of RGB images. In addition, this report consists of study and implementation of the representing
the image RGB image, Grayscale image, Binary image, converting and separating image from RGB 
to Gray scale, geometric operations such as rotate and flip to images, graphical representation of
basic intensity analysis on images, analyzing brightness and contrast adjustments to images, 
Calibrating dimensions of images to real-world values, and Segmenting images using 
thresholding. The Samsung galaxy s10+ phone camera was used to capture the photographs and 
the graphical representations were mainly obtained by using pixel intensity histograms.
Furthermore, this experiment can be improved by using a high-quality DSLR camera with
capturing photographs. In conclusion, Image analysis is given the extricate significant data which 
can be obtained using python and pixel intensity histogram

# 1 INTRODUCTION

In general idea of an image is a two dimensional intensity function of f(x,y) and which is an antique 
that portrays visual insight such as two-dimensional screen display, a photograph. And also 
analyzing image which examines the extraction of significant data. Therefore, it is called the
image processing. Currently one of fastest growing technologies are Image processing techniques 
which is used vital areas such as knowledge-based image analysis, image morphology, image data 
compression, image recognition, neural networks, edge identifiers and full-color image 
processing. In current world many fields of image processing are used digital image processing 
techniques and there are fundamental concepts of image processing are included with graphics 
applications. Therefore, it can be categorized as two method of principal application areas which 
are the scene data processing for autonomous machine perception and pictorial information 
improvement for human interpretation.
The fundamental steps in image processing are Image Acquisition, Image Enhancement, Image 
Restoration, Color Image Processing, Wavelets, Compression, Morphological Processing, Image 
Segmentation, Representation and Description, Recognition and Interpretation, and Knowledge 
Base. According to Image processing to computer vision has three levels that can be categorized
up into basic level, intermediate level and high-level processes.
In this report mainly based on the basic level of image processing using algorithms. And also the 
main objective of this practical was to gain brief knowledge about the mechanism of storing 
images in computers, enhancing images in the intensity domain and extracting the spectral 
information out of RGB images. Therefore, the main purpose of this practical was to process, 
analyze, Implement and visualize the images and intensity histograms by using the open software 
of high-level programming language of Python 03. 
Python 03 is an object-oriented scripting language, and it has been easy to understand therefore 
the prime benefits of learning python that has allowed debugging of snippets of code and 
interactive testing. Currently, python 03 is used in a lot of fields of image processing because
everyone can download freely and various fundamental standard image processing libraries and 
packages are available in python which can import and get the output easily such as Scikit-image,
Opencv, NumPy and matplotlib. Not only that it is it is utilized familiar English syntaxes which are 
easy to understand and learn.

# 2 THEORY

2.1 Pixel

The minimum unit of an image is called pixel and it usually has square shape or dots. Therefore, 
the digital images are construct by using this minimum unit. The high-quality image has large 
amount of very small size pixel and low-quality image has normal amount of pixel with normal 
size. Furthermore, millions of different colors can be visualized using red, blue, and green lighting 
pixel. And also the horizontal and vertical measurements of an image is represented using pixel 
dimensions.

2.2 RGB Image

The RGB image is created with the three-color combination of red, green, blue pixels and 8-bit
numbers of red, green, blue color value include the in an RGB image of pixel. It can be categorized 
as the three channels of red, green, blue and these colors are used in computer vision as human 
eye receptors.

2.3 Splitting Layers

Evidentially, the red, green, blue colors of three integers represent in the pixel of the image. 
Therefore, the idea of Splitting the Layers is separated to the three RGB channel layers of image 
with the image array.

2.4 Grey images

Using 2-Dimentional arrays, it can be stored the Black and white images which are mainly divided 
to the two types of Black and White images. They are Greyscale image that includes with Ranges 
of shades of grey 0 to 255 bit and Binary image which Pixel are either black or white (0 or 255
bits). Therefore the main idea of Grey scaling image is converting from a full color to shades of 
grey.

2.5 Histogram

The histogram is a statistical data graphical representation with the frequency of the dataset. 
Therefore, the distribution of pixels of an image can be visualized using histograms. Hence the 
histogram for an image always shows how frequently various color values distribute. This 
statistical method very useful for image processing such as Thresholding, Contrast, Exposure, 
Saturation and Dynamic Range.
n an image processing context, the histogram of an image normally refers to a histogram of the 
pixel intensity values. This histogram is a graph showing the number of pixels in an image at each 
different intensity value found in that image. For an 8-bit grayscale image there are 256 different 
possible intensities, and so the histogram will graphically display 256 numbers showing the 
distribution of pixels amongst those grayscale values. Histograms can also be taken of color 
images --- either individual histograms of red, green and blue channels can be taken, or a 3-D 
histogram can be produced, with the three axes representing the red, blue and green channels, 
and brightness at each point representing the pixel count. The exact output from the operation 
depends upon the implementation --- it may simply be a picture of the required histogram in a 
suitable image format, or it may be a data file of some sort representing the histogram statistics.

2.5.1 RGB histrgram and grey color histogram

The image can be separated as three layers for red, green and blue therefore, the histograms can 
be obtained for each color channel. This histogram is visualized with the pixel intensity count 
and pixel intensity value. And also 8 bit grayscale image has 256 different intensities. The grey 
color histogram is obtained using 8 bit grayscale image

2.6 Exposure triangle

The exposure triangle has three sides which are Aperture, shutter speed, and ISO. The good 
combination of these three elements are given the properly exposed photograph

2.6.1 ISO

ISO is the sensitivity of the digital sensor and high values of ISO of digital sensor does not need 
to lighter for quality exposure and also low value ISO digital sensor does need to more light for 
quality exposure.

2.6.2 shutter speed

The time period for hitting the sensor is call shutter speed. There are various shutter speeds are 
available in smart phone cameras that are 1/16000 s to 30s which are depend on the phone 
camera quality.

2.7 white balance 

Adjusting the color according to the color of the light source white object visualized white and 
using proper camera to balance the color temperature of light source is called white balance
that has relative warmth and coolness.

2.8 Raileygh Scattering

When particles that have a radius less than 1/10 the wavelength of the radiation that would be 
dispersion of electromagnetic radiation is called Rayleigh scattering

2.9 Global and Local thresholding

The Global thresholding is the degree of intensity separation with two intensity values in the 
image and local thresholding consider the intensity values for every pixel in the image withgray 
scale.
