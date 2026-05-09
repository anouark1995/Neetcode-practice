def find_max(d: dict):
    return max(d, key = d.get)

result = find_max({"Anouar": 10, "Nizar": 20})
print(result)