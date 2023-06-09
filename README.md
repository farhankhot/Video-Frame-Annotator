# Video-Frame-Annotator
This is a Python script that allows you to view images from a specified directory and save information about them to a text file. This is assuming your file structure is something like 
```
x/
├── y1/
│   ├── z1/
│   │   ├── frame1.jpg
│   │   ├── frame2.jpg
│   │   └── frame3.jpg
│   ├── z2/
│   │   ├── frame4.jpg
│   │   ├── frame5.jpg
│   │   └── frame6.jpg
│   └── z3/
│       ├── frame7.jpg
│       ├── frame8.jpg
│       └── frame9.jpg
└── y2/
    ├── z1/
    │   ├── frame10.jpg
    │   ├── frame11.jpg
    │   └── frame12.jpg
    ├── z2/
    │   ├── frame13.jpg
    │   ├── frame14.jpg
    │   └── frame15.jpg
    └── z3/
        ├── frame16.jpg
        ├── frame17.jpg
        └── frame18.jpg
```
You must edit the code to pass in your directories (both input in the format specified and the output where the resulting .txt file will be saved.

## Installation
To use this program, you will need to have Python 3 and the following libraries installed:

tkinter
PIL
You can install these libraries using pip:
```
pip install tkinter
pip install pillow
```
## Usage
Clone the repository to your local machine.
Navigate to the project directory in your terminal.
Run the following command to start the program: ```python annotate.py```

- The program will load the first image from the specified directory and display it on the screen.
- Use the right arrow key to move to the next image in the directory.
- Use the "s" key to move to the next subdirectory in the directory tree. This will move you to the next 'y' folder
- Type in a label and use the "Enter" key to save the label to a text file. NOTE: This will save one label for this particular 'z' directory in the resulting .txt file. This will also move you to the next 'z' folder in the subdirectory.
- To exit the program, close the window or press "Ctrl+C" in the terminal.

Note: Please make sure that you have the necessary permissions to read and write files in the specified directory before using this program.
