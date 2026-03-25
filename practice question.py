
"""Find the largest element in a list."""

lst = [10, 25, 5, 40]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i

print(largest)

"""Check if a number is even or odd."""

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

"""Reverse a string"""

s = "hello"
rev = ""
for ch in s:
    rev = ch + rev

print(rev)

"""Count vowels"""

s = "education"
count = 0
for ch in s:
    if ch.lower() in "aeiou":
        count += 1

print(count)

"""Sum of digits"""

num = 1234
sum = 0
while num > 0:
    sum += num % 10
    num //= 10

print(sum)

"""Palindrome string"""

s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

"""Fibonacci series"""

n = 5
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

"""Swap without third variable"""

a = 5
b = 10
a, b = b, a

print(a, b)

"""Count words"""

s = "Hello world python"
words = s.split()
print(len(words))

"""Min and Max in list"""

lst = [3, 8, 1, 6]
print(min(lst), max(lst))

"""Second largest"""

lst = [10, 20, 4, 45]
lst.sort()
print(lst[-2])

"""Remove duplicates"""

lst = [1, 2, 2, 3, 4, 4]
result = []
for i in lst:
    if i not in result:
        result.append(i)

print(result)

"""Frequency of elements"""

lst = [1, 2, 2, 3, 1]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(freq)

"""Merge two sorted lists"""

a = [1, 3, 5]
b = [2, 4, 6]

print(sorted(a + b))

"""Intersection of two lists"""

a = [1, 2, 3]
b = [2, 3, 4]

print([i for i in a if i in b])

"""Rotate list by k"""

lst = [1, 2, 3, 4, 5]
k = 2

print(lst[k:] + lst[:k])

"""First non-repeating character"""

s = "aabbcdde"

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

"""Flatten nested list"""

lst = [[1,2],[3,4],[5]]
flat = []
for sub in lst:
    for i in sub:
        flat.append(i)

print(flat)

"""Pairs with given sum"""

lst = [1, 2, 3, 4, 5]
target = 5

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])

"""Right triangle pattern"""

n = 5

for i in range(1, n+1):
    print("*" * i)

"""Pyramid pattern"""

n = 5

for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))

"""Prime numbers in range"""

start = 1
end = 20

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

"""Armstrong number"""

num = 153
temp = num
sum = 0
n = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")