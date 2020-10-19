s = "Are you afraid of ghosts?"
ret = "ghosts" in s

print(ret)
print("coffee" not in s)

'''
Methods
   match()      determines whether the RE matches at the beginning of the string.
   search()     scans the string and finds the location of this RE match
   findall()    finds all substrings that the RE matches and returns them as a list
   finditer()   finds all substrings that the RE matches and returns them as an iterator
'''
print('###-------------------------------------- re.match')
import re
txt = "Carl is a cat, he is smart, clever, and more.."
m = re.match(r"(\w+)\s", txt)
if m:
    print(m.group(0))
else:
    print('no match found')


import re
txt = "The number 123456 is my phone number"
result = re.match(r'^The number \d+\s*',txt)
print(result)
print(result.group(0))


import re
txt = "The number 123456 is my phone number"
result = re.match(r'^The.*?(\d+).*?',txt)
print(result)
print(result.group(0))
print(result.group(1))

print('###-------------------------------------- re.search')
import re
txt = "Sombrero in Spain for fun"
obj = re.search('Spain',txt)
print(obj)
print(obj.group(0))

print('###-------------------------------------- group')
import re
p = re.compile('(a(b)c)d')
m = p.match('abcd')
print(m.group(0))
print(m.group(1))
print(m.group(2))


print('###-------------------------------------- re.findall')
import re
txt = "Carl is a cool cat from a good family that and has a happy mood"
ret = re.findall(r'\w*oo\w*',txt)
print(ret)


print('###-------------------------------------- re.finditer')
import re
txt = "Blue blue sky"
pattern = "blue sky"
for match in re.finditer(pattern,txt):
   s = match.start()
   e = match.end()
   print(f'String match {pattern} at {s}:{e}')

'''
Grammar rules
\d	Matches a decimal digit; equivalent to the set [0-9].
\D	The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
\s	Matches any whitespace character; equivalent to [ \t\n\r\f\v].
\S	The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
\w	Matches any alphanumeric character; equivalent to [a-zA-Z0-9_].
\W	Matches the complement of \w.
\b	Matches the empty string, but only at the start or end of a word.
\B	Matches the empty string, but not at the start or end of a word.
\\	Matches a literal backslash.
Note that	Regular expression regex grammar can be a combination of all of the above
'''
