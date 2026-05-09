def reverseString(s : str) -> str:
    i=0
    j=len(s)-1
    s = list(s)
    while i<j:
        s[i],s[j] = s[j],s[i]
        i+=1
        j-=1
    return "".join(s)

result = reverseString('anouar')
print(result)
