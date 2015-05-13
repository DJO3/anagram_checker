#Given a list of words L, find all the anagrams in L in the order in which they appear in L.
L = ["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]

def anagram_checker(anagrams):
    anagrams_sorted = ["".join(sorted(x)) for x in anagrams]
    words = []
    for word in anagrams:
        sorted_word = "".join(sorted(word))
        if anagrams_sorted.count(sorted_word) > 1 and word not in words:
            words.append(word)
    return words

if __name__ == '__main__':
    print(anagram_checker(L))
    
