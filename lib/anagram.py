class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        anagrams = []
        for candidate in possible_anagrams:
            if sorted(candidate.lower()) == sorted(self.word.lower()) and candidate.lower() != self.word.lower():
                anagrams.append(candidate)
        return anagrams
