s="aaabbxxAxxaaxa"
b=""
for i in range(len(s)):
    if ( s[i] not in b):
        b+=s[i]
print(b)