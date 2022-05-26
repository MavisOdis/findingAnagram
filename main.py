# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagram(first_word, second_word):
    
    if sorted(first_word) == sorted(second_word):

        return True
        
    return False

print(find_anagram("hello","fellow"))
