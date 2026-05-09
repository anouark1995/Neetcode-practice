def two_sum(nums: list, target: int) -> list:
    storage = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in storage:
            return [storage[diff], i]
        storage[n] = i
    return

result = two_sum([1,9,5,7],16)
print(result)