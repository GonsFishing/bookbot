    
def count_words(text):
    return len(text.split())

def get_chars_dict(text):
    char_dict = {}
    text = text.lower()

    for c in text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_dict(dict):
    dictionaries = []
    for key in dict.keys():
        dictionaries.append({"key": key, "count": dict[key]})
    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries

def sort_on(dict):
        return dict["count"]
        


# Add a new function to your stats.py file that takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the character and one for the count.
# Sort from greatest to least by the count.
# The .sort() method will be helpful here (see the hint).