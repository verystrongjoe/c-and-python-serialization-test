# c-and-python-serialization-example
It is a simple project for both python and c++ to communicate with serialized data and ddeserialized data to use it.

# Python side
here is to receive tcp packet from client as a server

you can run like below

```
python -m tcp-server.py
``` 

# C++ side
here is to send tcp packet as a client

you can import Project6 in here through visual studio 2013 or higher

## pre-requisites
1. you go to msgpack-c folder in this project or need to clone this repository [here](https://github.com/msgpack/msgpack-c)
  
2. check whether or not you have include directory in it then, you need it to be added into visual studio include directory items.
    * Configuration Properties > VC++ Directories > Include Directories
    * C/C++ > General > Additional Include Dicrectories


## Issue
int_array_msgpack_cpp11.cpp  have an error.. 
```
Error	2	error C2039: 'msgpack_unpack' : is not a member of 'std::array<int,5>'	
```