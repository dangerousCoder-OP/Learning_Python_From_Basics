# To convert to Uppercase
str = "Norman Kumar"
print(str.upper())
print("kkkkk".upper())
#-----------------------------------------------------------------------------------------

# To convert to Lowercase
print(str.lower())
print("KKKK".lower())
#-----------------------------------------------------------------------------------------

# To convert to first letter of the string to uppercase and remaining into lowercase
print(str.capitalize())
print("oOOOO oooo OOOOOO".capitalize())
#-----------------------------------------------------------------------------------------

# Casefold - is mainly used for case-insensitive comparisons between strings, especially when working with text that may include special or international characters.
# When you want to compare strings without worrying about case, especially for user input, searching, or sorting text in a way that ignores case differences. If the user enters "YES", "Yes", "yEs", or even "Yeß"
str = "Straße"
print(str.casefold())
#-----------------------------------------------------------------------------------------

# Center: method returns a new string of length width with the original string centered and padded with the specified fillchar
str = "Placed"
# width: Total length of the resulting string.
# fillchar: Character to pad on both sides (optional). If no fillchar is specified, it defaults to a space character.
print(str.center(11))
print(str.center(11, '#'))  # Center the string with '*' as fill character

# If width is less than or equal to the string length, it returns the original string.
print(str.center(5))  # Output: 'Placed' (no padding needed)
#-----------------------------------------------------------------------------------------

# Count: methods counts how many times a substring appears in a string.
str = "Banana"
# substring: The text to search for.
# start (optional): Start index. start does NOT mean “count from the end backward”
# end (optional): End index.
print(str.count("a"))  # Output: 3 (counts all occurrences of 'a')
print(str.count("an"))  # Output: 2 (counts all occurrences of 'an')
print(str.count("a", 2))  # Output: 2 (starts counting from index 2)
print(str.count("a", 2, 4))  # Output: 1 (counts occurrences of 'a' between index 2 and 4)

str = "aaaa"
print(str.count("aa"))  # Output: 2 It does not count overlapping substrings.