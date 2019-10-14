# Installation Instructions
## Downloading Anaconda
### Windows and Mac
Anaconda is a distribution of Python, and can be downloaded [here](https:www.anaconda.com/distribution/) for Windows and Mac users.

### Linux
Linux users can follow the simple instructions given [here](https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart) to install Anaconda from the terminal.


Once you have installed Anaconda, you can proceed to install the TelloPy library in two ways:
### From source code
```
$ git clone https://github.com/hanyazou/TelloPy 
$ cd TelloPy
$ python setup.py bdist_wheel
$ pip install dist/tellopy-*.dev*.whl --upgrade
```

### From the Anaconda prompt in Windows/regular terminal in Mac and Linux
```
pip install tellopy
```
