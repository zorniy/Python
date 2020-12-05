# python
<h1>K Nearest Neighbour Classifier Program: KNN3.py</h1>

This is a simple classifier based on the K Nearest Neighbour (KNN) algorithm. Now you can save the clusters as .npy and .jpg files.

https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm

It reads a RGB JPEG image, then uses the K Nearest Neighbour algorithm to cluster the image's colours around several centroids. The number of clusters can be set by the user, and the number of iterations to run the classifier. The output is several clusters in the form several two-dimensional arrays of RGB vectors, each array associated with a cluster centroid.

Saving will need to be done using the Python command line, or written into the program. A later version will include a GUI window to do this.

The KNN algorithm is very well known, and is even already implemented in the SciPy package. This program, on the other hand, was written for fun, performing KNN from first principles. It is <b>NOT</b> optimised for speed! Use for <b>FUN</b> and education!

<h2>Requirements:</h2>
The program requires the following Python libraries:

<ul>
<li>NumPy

<li>MatPlotLib

<li>tkinter

</ul>

If you install Python, <b>tkinter</b> will come as part of the standard Python installation. The other libaries should be installed before running the program. 

On Linux, the libraries can be installed from the command line using PIP. If you don't have PIP, you need to install that first. Python 3 users need to install PIP3. 

<h3>Installing PIP on Ubuntu/Linux Mint</h3>
To install PIP:

<code>sudo apt-get install pip</code>


If you are using Python 3:

<code>sudo apt-get install pip3</code>

<h3>Installing the Python libraries</h3>

On the command line, type:


<code>
pip install numpy

pip install matplotlib
</code>

If using Python 3:

<code>
pip3 install numpy

pip3 install matplotlib
</code>

<h3>Windows Users</h3>
Follow the instructions on the Matplotlib and NumPy websites to install the packages. 

