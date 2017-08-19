# Cardiac Segmentation
Python code for segmentation of cardiac cavities.

The code will facilitate the parsing of Dicom files and contour files with
coordinates for ventricular segmentation.

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.  



## Prerequisites

-   python version 3.0, 3.5
-   numpy
-   pydicom
-   pandas
-   matplotlib
-   random
    The function *InvalidDicomError* on the file `parsing.py` works for python
    version 3.0 and above.
    
    To install those libraries consult python documentation; however; the most
    common way to install is the next command `pip install nameLibrary`


## Installing

Place **parsing.py**,  **art1.py** and the extracted dataset in the same directory. 

Be aware of a few changes in the **parsing.py** file.


## Running Test

On a shell(bash) write the following commands:

    python3
    import parsing
    exec(open("art1.py").read())

**PLEASE READ THIS**:
After the execution of the script, an image will show up. This image is a blend of
two images: the MRI and the Mask image. After you close this window, another four
images will be depicted showing more cases from the data.

Following the images, a sequence of numbers will be displayed in the console.
The tuples are the array shapes for the input(MRI images) and labels(Mask
Polygon). The next eight numbers displayed are from a cache
table. These numbers are not ordered and they point to a specific path.

## Play with the code.

You can change the values in line 130 of the **art1.py** file to display
others images. If no image is displayed, you must adjust the
values of the parameters.

If you increase the number of Epochs, you can visualize the
randomness of the cache table more clearly. 


## Built With

This code is run on a Ubuntu 14.04 box and bash console. Written in Emacs :)
