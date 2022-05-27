# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagram(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.lower()
    if sorted(first_word) == sorted(second_word):

        return True
        
    return False

print(find_anagram("hello","Hello"))
