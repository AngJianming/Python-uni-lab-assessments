"""
 Write a Python program in your IDE to perform the following tasks:

a.      Display ‘ I am a good boy/girl but my parents always scold me’.

b.      Count the length of this string.

c.      Slice this string up to ’Í am a good boy/girl’

d.      Find the word ‘parents ‘and replace with ‘lecturers’

e.      Concatenate ‘because I just pretend to be good, HAHAHA’

f.        Display ‘good’ in upper case

g.       Display “HAHAHA’ in lower case
"""

s = "I am a good boy/girl but my parents always scold me"

print(s)
print(len(s))
print(s[0:21])
print(s.replace('parents','lecturers'))
a = " because I just pretend to be good, HAHAHA"
z = s + a
print(z)
print(z.replace('good',"good".upper()))
print(z.replace('HAHAHA','HAHAHA'.lower()))
