# file-hasher

A simple python algorithm that walks through a directory generating file hashes

The main motivation for me to do this algorithm is to help me managing my data backups, that often have a lot of duplicated files and even duplicated backups (as I prefer to save and after delete the duplicates than losing my data).

This first version is very simple and just needs two arguments, the root folder that you want to walk into and the output txt file name, and the result is an output file with all md5 hashes along with the full path of the files. Below is an example of the command that runs the algorithm:

`python main.py /home/some-root-folder /home/output-file.txt`
