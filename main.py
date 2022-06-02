# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # assign words to lowercase
    word = word.lower()
    anagram = anagram.lower()
    
    # remove any whitespace
    word = word.replace(" ","")
    anagram = anagram.replace(" ", "")
    
    #sorted(word) == sorted(anagram) which returns either true or false
    return sorted(word) ==sorted (anagram)

print("find_anagrams 'hello' and 'check'", find_anagrams("hello", "check"))
print("find_anagrams 'hello' and 'check'", find_anagrams("below", "elbow"))

    return True

