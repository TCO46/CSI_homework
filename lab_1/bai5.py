def find_substring(string, sub_string):
    if sub_string in string:
        return string.index(sub_string)
    else:
        return -1
