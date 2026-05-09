def sum_list(numbers : list) -> float:
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

total = sum_list([1,2,7000])
print(total)