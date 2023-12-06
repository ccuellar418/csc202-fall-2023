
# Project 4

## Team Members

- Ronan Biggs
- Christian Cuellar
- Adan Silva

## Before Examining the Code

First looking into this project, it is very clear that it is very professionally done and organized. There is a README file present, talking about the code's functionality, maintainers, installation instructions, and other sort of useful information for anyone who is stumbling into this code repository for the first time. A very big part of project is source code, but other useful parts are included in as well. This includes CI implementation for building and running unit tests and tools for generating useful documentation. A good portion of the source code does lie within these unit tests, with their purpose to throughout verify functionality within their separate python source files, which are divided up the functions based on their supposed functionality.

## Initial Code Examination

Coverage.py is used to keep track of what lines of code have ran; Therefore the needed data structures will likely be for the purpose of keeping track of the lines run in the test suite. After discussing a binary tree or hash table were the most likely data structures we came up with. A self-balancing binary tree such as a red-black tree would be efficient for inserting which lines have run, and staying ordered to prevent duplicates. A hash table would also work well. After all, lookup is within the O(1) time, resulting in less use of lengthy searches to get our necessary data. It could quickly find if a line of code specified by the user ran and how many times. However, the maintainers need to keep in mind that hash tables are very prone to collisions. Despite this, good, efficient probing sequences can easily overcome that potential problem.

Report.py uses hash tables and dictionaries. The file is predominately important for its code, over its comments. The comments explain lines of code, but nothing more.

Files.py accesses raw data and turns it into usable files, predominantly either finding duplicate directories, if not the same one. It merges the files into the same directories. The code is the main function of this file.

Execfile.py uses lists, in order to simulate python functions, creating simulated files and running the code. It has a lot of exception marks to ensure the code runs as planned. So therefore the code is more important than the code

Collector.py is used as a prerequisite for Files.py, in order to obtain all of the raw data from files. This means the code is the important part of the file.

Disposition.py initializes variables to record stats about files, in order to figure out what to do with the file, with the code being more important.

Test_process.py checks all of the basic functions of the coverage package. Ensures the plugins and functions execute correctly. The main function is the code, but the comments explain the importance of the code, and what should be output.

Test_files.py tests files.py and ensures it creates a file with the correct names and placed in the correct directories.The code is important to simulate file creation, and then checking if the output is correct.


## Detailed Code Examination

_**Files.py **: 
_
_Variables_: 
**_ACTUAL_PATH_LIST_CACHE** is a dictionary with a string as a key, and the value of a list of strings. This is a dictionary that stores paths

**Canonical_filename_cache** is a dictionary with a key and value that are both strings. This variable holds the cache information from _ACTUAL_PATH_CACHE.

Another form of data structure that is used is in the prep_patterns. It intakes a string that is Iterable, and it returns a list of strings, which will be the letters used in the parameter, “patterns”. 

_Interesting Aspects of the Dictionaries_:
The interesting aspect about the _ACTUAL_PATH_CACHE variable and the _ACTUAL_PATH_CACHE variable is they are a centerpiece in this file. They have dedicated functions to obtain a filename for Canonical_filename_cachel file name cache. The same aspect is applied with the _ACTUAL_PATH_CACHE. It will do a search into the dictionary for the cache list to see if it can find the files. Once it finds the files, it then returns a string, which is the _ACTUAL_PATH_CACHE, opposed to the _ACTUAL_PATH_CACHE variable, which most likely has a bunch of unnecessary information that we do not need for certain functions, like establishing the path to a directory. 

They use dictionaries to separate the cache into key-value pairings, making it easier to slice out information inside of the cache, like alias files. 

_Dictionary use in code_:
The dictionaries are defined at the start of the code, specifically in the case if the computer is running on a windows environment. Then the path is used in many functions. A key function is the map function, which compares the Canonical_filename_cachel file and the actual path to the file. It then “maps” a clear path through the alias.


## Summary

Overall, the provided code-base has a lot more professional aspects to it.
Functions are named exactly to their function in the code, allowing the
developers to not have to write outrageous amounts of comments. Yes, the
repository itself is very big itself, but everything is very much organized with what each piece
does overall, allowing maintenance to be easier as maintainers only have to look in one
aspect of the repository rather than wasting time scanning through it entirely. The provided
code base is much more professionally done than my own code-bases currently. For example,
they have their files separated out into their categories while ours tend to be just crumpled together,
forcing us to go through all of them to see what I want to find, which can eat up time.
Their documentation tool is super interesting. We wonder if we are able to do something similar later on.
