import re

mess = open('randommess')

print("".join(re.findall('[A-Za-a]', mess.read())))
