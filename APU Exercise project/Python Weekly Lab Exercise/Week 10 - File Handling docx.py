#1.	Create a file using mode ‘x’
'''
with open("Week 10.txt", "x") as file:
    file.write("Hello")
'''

#2.	File handling
'''
with open("Week 10 file1.txt", "rt") as file1:
    print(file1)
'''

#3.	Insert multiple lines into a file
'''
with open("Week 10 file2.txt", "w") as file1:
    file1.writelines(["Hello world\n", "I'm Python\n", "Don't afraid to use me"])
'''

#4.	Reads all the lines in file.
'''
with open("Week 10 file3.txt", "r") as file3:
    print(file3.readlines())
'''

#5.	Read from a file line by line
'''
file4 = open('Week 10 file4.txt', 'w')
file4.writelines("Hi!\nWelcome to the python programming\nLet's continue exploring")
file4 = open('Week 10 file4.txt', 'r')

for python in file4:
    print(python)

file4.close()
'''

#6.	Count the lines in text file
'''
file5 = open('Week 10 file5.txt', 'w')
file5.writelines("Hi!\nWelcome to the python programming\nLet's continue exploring")
file5 = open('Week 10 file5.txt', 'r')
count = 0
for line in file5:
    count = count + 1

print('Line Count:', count)
'''

#7.	Read length of the text in a file and display string using slice.
'''
file6 = open("Week 10 file6.txt", "rt")

inp = file6.read()
print(inp[0:20])
'''


#8.	Read the text file line by line and remove any whitespace using strip()
'''
while True:
    line = file6.readline()
    if not line:
        break

    print(line.strip())
file6.close()
'''

#9.	Read UTF-8 text files
'''
with open('practice.txt', encoding='utf8') as f:
    for line in f:
        print(line.strip())
'''

#Part B
#1.	Write a program that opens an output file with the filename “my.txt”,
#   writes the name of animal, some fruit, and your country to the file on separate lines,
#   then close the file.
'''
animal = "Cat"  
fruit = "Apple"  
country = "Malaysia" 

with open("my.txt", "w") as my_file:
  my_file.write(f"{animal}\n")
  my_file.write(f"{fruit}\n")
  my_file.write(f"{country}\n")


print(my_file)
'''

#2.	Write a function in python to read the content from a text file "python.txt" line by line and display the same on screen.
'''
with open("python.txt", "w") as my_file1:
  my_file1.write("In this tutorial, you'll learn file handling in Python, file operation such as opening a file,\nreading from it, writing into it, closing it, renaming a file, deleting a file, and various file methods.\n\nTo store data temporarily and permanently, we use files.\nA file is the collection of data stored on a dick in one unit identified by filename.")
'''

#3
'''
def count_non_t_lines(filename):

  count = 0
  try:
    with open(filename, encoding="utf-8") as f:
      for line in f:
        if not line.strip().startswith('T'):
          count += 1
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  return count


storyfile = "story.txt"
num_lines = count_non_t_lines(storyfile)
print(f"Number of lines not starting with 'T' in '{storyfile}': {num_lines}")
'''

#4
#a

def remove_duplicates(filename1):
  seen_lines = set()
  with open(filename1, 'r') as f_in, open('newRevision.txt', 'w') as f_out:
    for line in f_in:
      if line.strip() not in seen_lines:
        seen_lines.add(line.strip())
        f_out.write(line)

#b

filename1 = ("Revision.txt")
remove_duplicates(filename1)
print(f"Duplicates removed from '{filename1} file'. New file: 'newRevision.txt'")
filename1 = open("newRevision.txt", "rt")
print(filename1.read())
filename1.close()

#c

unique_lines = []
with open('newRevision.txt', 'r') as f_out:
  unique_line = [line.rstrip() for line in f_out]
print(unique_line)





































