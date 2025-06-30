
#Q1 Write a Python program to calculate the length of a string entered.

#Sample input/output:
#Enter a string:Hai good morning
#The strings entered is Hai good morning
#The length of the strings is: 16
'''
def main():
  str1 = input("Enter a string e.g 'Hai Good morning': ")

  str_length1 = len(str1)

  print(f"The strings entered is: {str1}")
  print(f"The length of the strings is: {str_length1}")

if __name__ == "__main__":
  main()
'''


#Q2 Write a Python program to get the first two and the last two characters
#from a string entered.
#Display as per the sample input/output below.

#Sample input/output:
#Enter a string:Hai, my name is Mary
#The strings entered is Hai, my name is Mary
#The first two string are: Ha
#The last two strings are: ry
'''
def get_first_last_char(str2):

  if len(str2) < 4:
    return str2, str2

  char1 = str2[:2]
  char2 = str2[-2:]

  return char1, char2


str2 = input("Enter a string e.g Hai, my name is Mary: ")

first_two, last_two = get_first_last_char(str2)

print(f"First two characters: {first_two}")
print(f"Last two characters: {last_two}")
'''


#Q3 Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
'''
def swap_and_combine(str3, str4):
  swapped_str1 = str4[:2] + str3[2:]
  swapped_str2 = str3[:2] + str4[2:]

  combined_str = swapped_str1 + " " + swapped_str2

  return combined_str


str1, str2= input("Enter the string e.g 'abc,xyz': ").split(',')

result1 = swap_and_combine(str1, str2)
print(f"Combined string with swapped first two characters: {result1}")
'''


#Q4 Write a Python program to add 'ing' at the end of a given string (length
#should be at least 3). If the given string already ends with 'ing', add 'ly'
#instead. If the string length of the given string is less than 3, leave it
#unchanged.

#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'
'''
def ing(sample):
    if len(sample) < 3:
        return sample
    elif sample[-3:] == "ing":
        return sample + "ly"
    else:
        return sample + "ing"

Sample_str = input("Insert a string with more than 3 words e.g 'abc': ")
print(f"Sample string: {Sample_str}\nExpected Result:{ing(Sample_str)}")
'''


#Q5 Write a Phyton program to display letters at odd index

#Sample string: ‘I like Phyton’
#Expected result: Ilk htn
'''
def odd(str5):
  result2 = str5[::2]
  return result2

str5 = ("I like Python")
result2 = odd(str5)

print("Characters show by odd: ", result2)
'''


#Q6 Prompt user for a string. Display the last two characters twice.

#Sample string: Python
#Expected result: onon
'''
str6 = input("Enter a string e.g 'Python': ")

if len(str6) < 2:
  print("String is less than 2 characters. No last characters to display.")
  print("Please restart the program... ")
else:
  last_2_chars = str6[-2:]
  result3 = (last_2_chars * 2)

print("The last two characters displaying twice is: ", result3)
'''


#Q7 Prompt user for a string. Display the string with reverse order.

#Enter string:python
#Reverse the string: nohtyp
'''
str7 = input("Enter a string e.g 'python': ")

if len(str7) < 2:
  print("String cannot be nothing. No characters to display.")
  print("Please restart the program... ")
else:
  reverse_chars = str7[::-1]
  result4 = (reverse_chars)

print("The last two characters displaying twice is: ", result4)
'''


#Q8 Prompt user for a string. Check the string if it is start with “Py”

#Enter string:python
#True
#Enter string:rabbit
#False
'''
str8 = input("Enter a string/word to check if it starts with 'Py': ")

while True:
  result5 = str8.startswith("py")
  print(f"'{str8}' does start with 'Py' therefore, {result5}")
  break
'''


#Q9 Write a Python script that takes input from the user and displays that
#input back in upper, lower and capitalize cases.

#Enter string:hai gOOd MornIng
#String convert to upper case: HAI GOOD MORNING
#String convert to lower case: hai good morning
#String convert to capitalize case: Hai good morning
'''
str9 = input("Enter a string/word e.g 'hai gOOd Morning': ")

upper_case = str9.upper()
lower_case = str9.lower()
cap_case = str9.title()

print(f"Convert to upper case: {upper_case}")
print(f"Convert to lower case: {lower_case}")
print(f"Convert to capitalize case: {cap_case}")
'''





















