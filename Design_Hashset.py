class MyHashSet:

    def __init__(self):
        self.output_list = []

    def add(self, key: int) -> None:
        if key not in self.output_list:
            self.output_list.append(key)
        # print(self.output_list)


    def remove(self, key: int) -> None:
        if key in self.output_list:
            self.output_list.remove(key)
            # print(self.output_list)


    def contains(self, key: int) -> bool:
        if key in self.output_list:
            return True
        else:
            return False
                
                
obj = MyHashSet()
print(obj.add(3))
print(obj.add(4))
print(obj.contains(3))
print(obj.contains(4))
print(obj.remove(4))
print(obj.remove(3))
print(obj.contains(3))
print(obj.contains(4))
