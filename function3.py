def count_vowels(s : str) -> int:
    vowels = ['a','e','i','o','u','y']
    count = 0
    s = s.lower()
    for i in s:
        if i in vowels:
            count += 1
    return count

count = count_vowels('LahbIba')
print(count)