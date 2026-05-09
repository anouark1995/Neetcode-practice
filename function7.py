def is_palindrome(s : str) -> bool:
    i = 0
    j = len(s)-1
    s = ("".join(c for c in s if c.isalnum())).lower()
    while i < j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

res = is_palindrome("XABBA")
print(res)
