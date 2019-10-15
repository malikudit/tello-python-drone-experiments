# TelloPy DJI Drone
![A simple visual of a Tello DJI drone](tello-img.jpg)

## Installation Instructions
### Downloading Anaconda
#### Windows and Mac
Anaconda is a distribution of Python, and can be downloaded [here](https:www.anaconda.com/distribution/) for Windows and Mac users.

#### Linux
Linux users can follow the simple instructions given [here](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart) to install Anaconda from the terminal.

### Intalling the TelloPy library
Once you have installed Anaconda, you can proceed to install the TelloPy library in two ways:
#### From source code
```
$ git clone https://github.com/hanyazou/TelloPy 
$ cd TelloPy
$ python setup.py bdist_wheel
$ pip install dist/tellopy-*.dev*.whl --upgrade
```

#### From the Anaconda prompt in Windows/regular terminal in Mac and Linux
```
pip install tellopy
```

### Testing
Type the following in the terminal or Anaconda prompt to perform a simple takeoff procedure with the drone:
```
python -m tellopy.examples.simple_takeoff
```

### Setting up the Tello drone video capture function
Type the following sequentially into the terminal or Anaconda prompt:
```
conda install -c conda-forge av
pip install open-cv python
pip install image
pip install msgpack
```

To test the video capture function, type:
```
python -m tellopy.examples.video_effect
```

## Running Python scripts for the drone
Navigate to the folder where the Python file exists on your computer, and simply type:
```
python2 filename.py
```
where filename is the name of your file.
