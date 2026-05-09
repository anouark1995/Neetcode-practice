def merge_list_alternating(a: list, b:list) -> list:
    i= 0
    j=0
    final_list = []
    while i< len(a) and j<len(b):
        final_list.append(a[i])
        final_list.append(b[j])
        i += 1
        j += 1
    while i< len(a):
        final_list.append(a[i])
        i += 1
    while j< len(b):
        final_list.append(b[j])
        j += 1
    return final_list

result = merge_list_alternating(['a','b','c'],[1,2,3,4,5,6,7])
print(result)