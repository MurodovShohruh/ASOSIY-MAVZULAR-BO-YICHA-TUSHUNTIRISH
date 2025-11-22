# 1.append
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)

# 2.insert
nums = [1, 2, 4]
nums.insert(2, 3)
print(nums)

# 3.extend
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

# 4.remove
fruits = ["apple", "banana", "apple"]
fruits.remove("apple")
print(fruits)

# 5.pop
nums = [10, 20, 30]
nums.pop(1)
print(nums)

# 6. clear
a = [1, 2, 3]
a.clear()
print(a)

# 7. index
a = ["a", "b", "c"]
print(a.index("b"))

# 8. count
nums = [5, 1, 4, 2]
nums.sort()
print(nums)

# 9. sort
nums = [5, 1, 4, 2]
nums.sort()
print(nums)

# 10. reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)

# 11. copy
a = [1, 2, 3]
b = a.copy()
print(b)
