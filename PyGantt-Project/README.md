<img src="./assets/icon.ico" alt="drawing" width="200"/>


# PyGantt

This application is used to create and manage projects using different graphs. Those different graphs include:

- Gantt diagram
- Pessimistic Gantt diagram
- PERT Chart

With this application you can **add**, **delete**, **edit** different tasks of the project. 

## Building the application :hammer:
1. ### Building the `.dll` / `.so` file (optional)
This step is not mandatory because I have provided a `.dll` file with the application. If it works for you, you can just use it and go to the next step. If it doesn't, then come back here.
#### Building the `.dll` file (Windows)
To build the `.dll` file on Windows, you will need a compiler such as MinGW which was used here. I would recommended using MSYS2 (build platform) to get the right compiler for you. Here is the link to the MSYS2 site: https://www.msys2.org/
Also, you need to keep in mind that if you have installed the 32 bit version of python you will need to install the 32 bit C compiler. And for the 64 bit version of python, the 64 bit version of the compiler.
```
gcc -s -shared -o src/C_lib.dll -fPIC src/C_lib.c
```
#### Building the `.so` file (Linux)
If you are on linux the steps are pretty much the same; you first want to install a compiler:
```bash
sudo apt install gcc-mingw-w64 # Or any othercompiler according to your OS
```
Then you will want to compiler the `C_lib.c` file:
```
gcc -s -shared -o src/C_lib.so -fPIC src/C_lib.c
```

2. ### Building the `.exe`
To build the  application you will need to run the following commands:

```bash
cd ./PyGantt-Project/ # If you are not already in the directory
pyinstaller --hidden-import "babel.numbers" src/main.py
copy src/C_lib.dll dist/main
copy -r assets dist
```
or on Linux:
```bash
cd ./PyGantt-Project/ #If you are not already in the directory
pyinstaller --hidden-import "babel.numbers" src/main.py
cp src/C_lib.dll dist/main
cp -r assets dist
```
You should now be able to run the application with the `main.exe` file located in the `dist/main` folder.

## Running the application with python :snake:
You first need to make sure you have all the dependencies installed. If some of the dependencies are missing you can install them using `pip` and commands such as:

`pip install networkx`

## Documentation :notebook:
The project is documented using [Doxygen](https://www.doxygen.nl/). There are a couple of comments that are not present in the Doxygen documentation that can still be found in the code.

### Building the documentation
To build the documentation yourself you will first need to install doxygen on your machine. I advise looking into their website and following the instructions [here](https://www.doxygen.nl/manual/install.html)

Once you have installed doxygen on your system you can run the following commands:

```bash
cd ./PyGantt-Project/ #If you are not already in the directory
doxygen
```


made by Pulps with :heart:

License GNU GPL v3.0