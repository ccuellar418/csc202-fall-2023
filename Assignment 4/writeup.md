
# Project 4

## Team Members

- Ronan Biggs
- Christian Cuellar
- Adan Silva

## Before Examining the Code

A coverage tester not only needs to get it's job done, but also needs to be efficient as well. I can for see it using a dictionary to do this as the search time for dictionaries/hash tables is really good, allowing the program to be more efficient. This also allows the programs to easily map information to a non-mutable source to prevent unforeseen changes to it. Then it can take advantage of that search to get what it needs. A list and graphs could potentially work in this case as well, but some modifications may be needed to get the results that the maintainers want to see. Of course, these are only just some possible data structures I could see. Once we dig into the specific code itself, it is very easy for those hypothesis to either be confirmed or quickly denied.The choice really is up to these maintainers

## Initial Code Examination

First looking into this project, it is clear that it is professionally done and organized. A README file present, talking about the code's functionality, maintainers, installation steps, and other useful information for users. Other useful parts are present along with the main library. This includes CI implementation for building and running unit tests and documentation generation.Their purpose to verify functionality for each piece. Coverage.py first appears to using hash tables. Report.py utilizes dictionaries to generate reports, which is also a hash table. Files.py puts raw data into usable files into the same directories. Execfile.py uses lists to simulate Python functions and ensure proper execution. Collector.py is a prerequisite for Files.py. It serves to get that necessary raw data. Disposition.py initializes variables to obtain file stats on what to do with the file, with the code being priority. Test_process.py checks all of the basic functions of the coverage package to ensure the plugins and functions execute correctly. The main function is the code, but the comments enhance it as well. Test_files.py tests files.py and ensures a file is created with for correct names and correct directory placements. The code is important to in simulating real file creation to compare results accurately.

## Detailed Code Examination

_**Files.py **: _ Variables: _ACTUAL_PATH_LIST_CACHE is a dictionary with a string as a key, and the value of a list of strings. This is a dictionary that stores paths

Canonical_filename_cache is a dictionary with a key and value that are both strings. This variable holds the cache information from _ACTUAL_PATH_CACHE.

Another form of data structure that is used is in the prep_patterns. It intakes a string that is Iterable, and it returns a list of strings, which will be the letters used in the parameter, “patterns”.

Interesting Aspects of the Dictionaries: The interesting aspect about the _ACTUAL_PATH_CACHE variable and the _ACTUAL_PATH_CACHE variable is they are a centerpiece in this file. They have dedicated functions to obtain a filename for Canonical_filename_cachel file name cache. The same aspect is applied with the _ACTUAL_PATH_CACHE. It will do a search into the dictionary for the cache list to see if it can find the files. Once it finds the files, it then returns a string, which is the _ACTUAL_PATH_CACHE, opposed to the _ACTUAL_PATH_CACHE variable, which most likely has a bunch of unnecessary information that we do not need for certain functions, like establishing the path to a directory.

They use dictionaries to separate the cache into key-value pairings, making it easier to slice out information inside of the cache, like alias files.

Dictionary use in code: The dictionaries are defined at the start of the code, specifically in the case if the computer is running on a windows environment. Then the path is used in many functions. A key function is the map function, which compares the Canonical_filename_cachel file and the actual path to the file. It then “maps” a clear path through the alias.

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
