# Random-Photo-Downloader
This python script can download a given number of random photos from the internet to a designated folder
--------------------------------------------------------------------------------------------------------
The two files represent the same code.
- "random_picture.py" is a python file that can directly executed with a python IDE or a python interpreter in a command prompt or terminal.
- "random_picture.ipynb" is a notebook file that can be open using Jupyter Notebook.
--------------------------------------------------------------------------------------------------------
HOW IT WORKS ?

the script uses "unsplash.com" website as a source for photos to download, 
and then it attempts to download photos using randomly generated photo UUIDs.
Whenever the dowload fails the script will display an error message and continue to work with no problem.
The number of photos to be downloaded (must be a positive integer) and the name of the output file (string and respects the standard naming format used in computers) 
is given by the user at the start of the script.

PS: - There is no input validation so using weird input might cause the script to behave differently.
    - In theory there is no maximum number of photos that can be inputed. this script is only tested with 500 photos.
