def reverse_string(original):
    new=original.split()
    # splits thee strings based on spaces into a list of strings

    return ' '.join(new[::-1])
    # returns the list of string in reverse order by joining them with spaces

original_string='this is monday'
print(reverse_string(original_string))