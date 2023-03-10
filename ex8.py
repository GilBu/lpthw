# assign 4 format to variable formatter
formatter = "{} {} {} {}"

# print int 1 to 4 using format
print(formatter.format(1, 2, 3, 4))
# print string numbers one to four with format
print(formatter.format("one", "two", "three", "four"))
# print booleans with formatted
print(formatter.format(True, False, False, True))
# format is print formatter as strings resulting 16 {}
print(formatter.format(formatter, formatter, formatter, formatter))
# print serveral strings
print(formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
    ))
