# Even Odd
num = int(input("provide num: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")


# Reverse
def reverse_method(string):
    reversed = ""
    for i in range(len(string) - 1, -1, -1):
        reversed += string[i]
    return reversed


x = input("String to reverse: ")
print(reverse_method(x))

# Right Triangle
rows = int(input("enter: "))
for i in range(rows):
    for j in range(i + 1):
        print("*", end="")
    print()

# Print num in right triangle pattern instead of asterisk
rows = int(input("enter: "))
for i in range(rows):
    for j in range(i + 1):
        print((i + 1) * 1, end="")
    print()

# Most frequent char in String
def most_frequent_char(word):
    # Create a dictionary to count the frequency of each character
    frequency = {}

    # Count the frequency of each character in the word
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find the character with the maximum frequency
    most_frequent = max(frequency, key=frequency.get)
    max_count = frequency[most_frequent]

    return most_frequent, max_count