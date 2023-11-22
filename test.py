import re

pattern = re.compile(r'^(|\+?998)\s?\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$')

print(pattern.match("998 99 999 99 99"))
print(pattern.match("+996 999999999"))
print(pattern.match("970000000"))

