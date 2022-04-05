# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:36:10 2022

@author: dpdunn
"""

'''
Must open and close a file when using it in python
'''
f= open("olympics.txt", "r") # "r" is for read, so we are reading the file

#multiple ways to read a file or the information
# you can use read, which reads then entire file as a single string


entire_file = f.read()
print(entire_file)

# you can use readline, which will read one line at a time up to the new line symbol "\n" character

l= f.readline()
print(l)

# you can use readlines, each line is listed as a separate text

lines_list=f.readlines() # since it reads each line separately it is often used in a for loop
for line in lines_list:
    print("line read: " + line)

f.close() # we have to close the file

'''
you can streamline the reading and close using the "with" key word. Once you
exit code block, python automatically closes you file
'''
with open("olympics.txt","r") as f:
    lines_list=f.readlines() # since it reads each line separately it is often used in a for loop
    for line in lines_list:
        print("line read: " + line)
        

'''
Writing to a file, replace the "r" with "w". if file does not exist it will be
created. if it does exist, you will loose the existing data as it will be 
overwritten
'''
f= open("olympics.txt", "w") # "w" is for write, so we are writing to a file
f.write("my last line\n")
f.write("my new last line\n")
f.close()

'''
Using the file school_prompt2.txt, find the number of characters in the file
 and assign that value to the variable num_char.
 '''
num_char = 0
with open("school_prompt2.txt","r") as f:
    entire_file_schlprmt2=f.read()
    for char in entire_file_schlprmt2:
        num_char +=1
    print(num_char)
        
'''
Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
'''

num_lines = 0
with open("travel_plans2.txt","r") as f:
    line_list_trvl_plns2=f.readlines()
    for line in line_list_trvl_plns2:
        num_lines +=1
    print(num_lines)


'''
    Create a string called first_forty that is comprised of the first 40 
    characters of emotion_words2.txt.
'''

first_forty=[]
with open("emotion_words2.txt","r") as f:
    entire_file_emo_wrds2=f.read()
    for char in entire_file_emo_wrds2:
        first_forty.append(char)
first_forty=first_forty[0:40]
first_forty= "".join(first_forty)
print(first_forty)

'''

Method Name

Use

Explanation

write

filevar.write(astring)

Add a string to the end of the file. filevar must refer to a file that has 
been opened for writing.

read(n)

filevar.read()

Read and return a string of n characters, or the entire file as a single 
string if n is not provided.

readline(n)

filevar.readline()

Read and return the next line of the file with all text up to and including the
newline character. If n is provided as a parameter, then only n characters will
be returned if the line is longer than n. Note the parameter n is not supported
in the browser version of Python, and in fact is rarely used in practice, you 
can safely ignore it.

readlines(n)

filevar.readlines()

Returns a list of strings, each representing a single line of the file. If n 
is not provided then all lines of the file are returned. If n is provided then 
n characters are read but n is rounded up so that an entire line is returned. 
Note Like readline readlines ignores the parameter n in the browser.
'''
olypmicsfile = open("olympics.txt", "r")

for aline in olypmicsfile.readlines():
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olypmicsfile.close()

'''
To make the code a little simpler, and to allow for more efficient processing, 
Python provides a built-in way to iterate through the contents of a file one 
line at a time, without first reading them all into a list. Some students find 
this confusing initially, so we don’t recommend doing it this way, until you 
get a little more comfortable with Python. But this idiom is preferred by 
Python programmers, so you should be prepared to read it. And when you start 
dealing with big files, you may notice the efficiency gains of using it.
'''

olympicsfile = open("olympics.txt", "r")

for aline in olympicsfile:
    values = aline.split(",")
    print(values[0], "is from", values[3], "and is on the roster for", values[4])

olympicsfile.close()

'''
Write code to find out how many lines are in the file emotion_words.txt as 
shown above. Save this value to the variable num_lines. Do not use the len 
method.
'''

emo_wrds = open("emotion_words.txt", "r") #this works as the directory where the file is running also has this file in it
num_lines=0
for aline in emo_wrds:
    num_lines+=1
    
print(num_lines)

emo_wrds.close()

'''
In the examples we have provided, and in the simulated file system that we’ve 
built for this online textbook, all files sit in a single directory, and it’s 
the same directory where the Python program is stored. Thus, we can just write
open('myfile.txt', 'r').

If you have installed Python on your local computer and you are trying to get 
file reading and writing operations to work, there’s a little more that you may
need to understand. Computer operating systems (like Windows and the Mac OS) 
organize files into a hierarchy of folders, with some folders containing other 
folders.

../_images/ExampleFileHierarchy.png
If your file and your Python program are in the same directory you can simply 
use the filename. For example, with the file hierarchy in the diagram, the file
myPythonProgram.py could contain the code open('data1.txt', 'r').

If your file and your Python program are in different directories, however, 
then you need to specify a path. You can think of the filename as the short 
name for a file, and the path as the full name. Typically, you will specify a 
relative file path, which says where to find the file to open, relative to the 
directory where the code is running from. For example, the file 
myPythonProgram.py could contain the code open('../myData/data2.txt', 'r'). 
The ../ means to go up one level in the directory structure, to the containing 
folder (allProjects); myData/ says to descend into the myData subfolder.

There is also an option to use an absolute file path. For example, suppose the 
file structure in the figure is stored on a computer in the user’s home 
directory, /Users/joebob01/myFiles. Then code in any Python program running 
from any file folder could open data2.txt via 
open('/Users/joebob01/myFiles/allProjects/myData/data2.txt', 'r'). You can tell
an absolute file path because it begins with a /. If you will ever move your 
programs and data to another computer (e.g., to share them with someone else),
it will be much more convenient if your use relative file paths rather than 
absolute. That way, if you preserve the folder structure when moving 
everything, you won’t need to change your code. If you use absolute paths, then
the person you are sharing with probably not have the same home directory name,
/Users/joebob01/. Note that Python pathnames follow the UNIX conventions 
(Mac OS is a UNIX variant), rather than the Windows file pathnames that 
use : and \. The Python interpreter will translate to Windows pathnames when 
running on a Windows machine; you should be able to share your Python program 
between a Windows machine and a MAC without having to rewrite the file open 
commands.
'''

'''
This is equivalent to code that specifically closes the file at the end, 
but neatly marks the set of code that can make use of the open file as an 
indented block, and ensures that the programmer won’t forget to include 
the .close() invocation.
'''
#using with and letting python close the file
with open('mydata.txt', 'r') as md:
    for line in md:
        print(line)
#same code but without with and using .close() to close the file
md = open('mydata.txt', 'r')
for line in md:
    print(line)
md.close()


'''
Recipe for reading and processing a file.
#1. Open the file using with and open.

#2. Use .readlines() to get a list of the lines of text in the file.

#3. Use a for loop to iterate through the strings in the list, each being one 
line from the file. On each iteration, process that line of text

#4. When you are done extracting data from the file, continue writing your code
outside of the indentation. Using with will automatically close the file once 
the program exits the with block.

fname = "yourfile.txt"
with open(fname, 'r') as fileref:         # step 1
    lines = fileref.readlines()           # step 2
    for lin in lines:                     # step 3
        #some code that references the variable lin
#some other code not relying on fileref   # step 4

****NOTE THIS IS NOT GOOD FOR LARGE DATA*****
'''
# more efficient to interate of the file itself

with open(fname, 'r') as fileref:
    for lin in fileref:
     ## some code that uses line as the current line of the file
     ## some more code


### WRITING TO FILES
filename = "squared_numbers.txt"
outfile = open(filename, "w")

for number in range(1, 13):
    square = number * number
    outfile.write(str(square) + "\n")

outfile.close()

infile = open(filename, "r")
print(infile.read()[:10])
infile.close()

###READING CSV FILES
fileconnection = open("olympics.txt", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    vals = row.strip().split(',')
    if vals[5] != "NA":
        print("{}: {}; {}".format(
                vals[0],
                vals[4],
                vals[5]))
fileconnection.close()


###WRITING TO A CSV
n = [0] * 12
for i in range(1,13):
    n[i-1] = i *12
outfile = open("Multiples of 12.csv", "w")
for j in range(0, len(n)):
    outfile.write(str(j+1) + ',' + str(n[j]))
    # +1 to j since the array starts at 0 and we start counting at 1
    outfile.write('\n')
outfile.close()

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('Name,Age,Sport')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '{},{},{}'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics.csv", "w")
# output the header row
outfile.write('"Name","Age","Sport"')
outfile.write('\n')
# output each of the rows:
for olympian in olympians:
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()

#q1
'''Using the text file studentdata.txt write a program that prints out the 
names of students that have more than six quiz scores.
'''

# Hint: first see if you can write a program that just prints out the number of scores on each line
# Then, make it print the number only if the number is at least six
# Then, switch it to printing the name instead of the number

with open("studentdata.txt","r") as studentdata:
 
    for aline in studentdata:
        val= aline.split(" ")
        if len(val)>7:
            print(val[0])

#q2
'''
Create a list called destination using the data stored in travel_plans.txt. 
Each element of the list should contain a line from the file that lists a 
country and cities inside that country. Hint: each line that has this 
information also has a colon : in it.
'''
destination=[]
#other_info=[]
with open("travel_plans.txt","r") as travel_plans:
     
    for aline in travel_plans:
        if ":" in aline:
            destination.append(aline)
        #else:
         #   other_info.append(aline)
print(destination)            


#q3 
'''
Create a list called j_emotions that contains every word in emotion_words.txt 
that begins with the letter “j”.
'''
j_emotions=[]

with open("emotion_words.txt","r") as emo_wrds:


    for word in emo_wrds:
       wrd=word.strip()
       j_emotions.append(wrd)
           for x in j_emotions:
               x= " ".join(x)
       # #wrd= "".join(wrd)
               x= x.split()
               print(x)
       #  if "j" in wrd[]:
       #      j_emotions.append(wrd)
        
print(j_emotions)            
'''
    ??
'''

j_emo=[]





num=0
with open("travel_plans.txt") as tp:
    words=tp.read()
    for word in words:
         num +=1
print(num)

num_words=0
with open("emotion_words.txt","r") as f:
    emo_file=f.read()
    print(emo_file)
    emo_file=emo_file.split("\n")
    emo_file=emo_file
    for i in emo_file:
        emo_file=i.split()
    
    print(emo_file)
    words = emo_file.split()
    for i in range(len(emo_file)):
        emo_file=(emo_file[i].split(" "))
print(emo_file)
        num_words +=1
print(num_words)
words

print(emo_file[0].split(" "))
#num_lines=-1
three=[]
with open("school_prompt.txt","r") as f:
    
    emo_file=f.read()
    print(emo_file)
    #emo_file=emo_file.split(" ")
    print(emo_file)
    # print(len(emo_file))
    for aline in emo_file:
        three.append(aline)
        three="".join(three)
print(three)

p_words=[]
with open("school_prompt.txt","r") as f:
    schl_prompt=f.read()
   # print(schl_prompt)
    words = schl_prompt.split()
   # print(words)
    for word in words:
        if "p" in word.lower():
            p_words.append(word)
print(p_words)
           

    
first_chars=[]
with open("travel_plans.txt","r") as f:
    trvl_plans=f.read()
    for char in trvl_plans:
        first_chars.append(char)
first_chars=first_chars[0:33]
first_chars= "".join(first_chars)
print(first_chars)


three=[]
line_list=[]
with open("school_prompt.txt","r") as f:
    schl_prompt=f.read()
    schl_prompt=schl_prompt.split('\n')
    for i in range(len(schl_prompt)):
        line=schl_prompt[i].split()
        line_list.append(line)
#print(len(line_list))
    for i in range(len(line_list)-1):
        three.append(line_list[i][2])
print(three)
    
    print(schl_prompt)
    print(line_list)
    for aline in schl_prompt:
        line_list.append(aline)
    print(line_list)
    for word in words:
        if "p" in word.lower():
            p_words.append(word)
print(p_words)

emotions=[]
line_list=[]
with open("emotion_words.txt","r") as f:
    emo_words=f.read()
    emo_words=emo_words.split('\n')
    for i in range(len(emo_words)):
        line=emo_words[i].split()
        line_list.append(line)
#print(len(line_list))
    for i in range(len(line_list)-1):
        emotions.append(line_list[i][0])
print(emotions)