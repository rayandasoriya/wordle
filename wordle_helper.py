"""
WordleHelper list of words and returns highly possible characters,
ideal start words and find word which contains a substring.
"""
import collections
import sys
import requests
from bs4 import BeautifulSoup

URL = "https://eslforums.com/5-letter-words/"
header = {'User-Agent': 'Mozilla/5.0'}

class WordleHelper:
    """Returns list of words and highly possible characters."""
    def __init__(self):
        self.words = []

    @classmethod
    def _fetch_from_site(cls):
        """Returns a list of li element from site."""
        response = requests.get(URL, headers=header)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.findAll('li', {"class": ""})

    @classmethod
    def _words_cleaner(cls, words_with_tag):
        """Returns a list of words with no html tags."""
        words = set()
        for word in words_with_tag:
            words.add(word.string)
        return list(words)

    @classmethod
    def _char_frequency(cls, words):
        """Returns the character frequency of a list of words."""
        char_freq = collections.defaultdict(int)
        for word in words:
            for char in word:
                char_freq[char] +=1
        return char_freq

    def create_list_of_words(self):
        """Returns list of words by pulling from site."""
        words_with_tag = self._fetch_from_site()
        clean_words = self._words_cleaner(words_with_tag)
        self.words = clean_words

    def ideal_start_word(self):
        """Returns a list of top 10 ideal start words."""

        words_with_no_repetition = [word for word in self.words if len(set(word)) == len(word)]
        # Design a character frequency map using non-repeating words
        char_freq = self._char_frequency(words_with_no_repetition)
        word_score = {}

        # Find all words on the basis of highest score.
        # Score is being calculated by adding up the frequency of all characters in the word.
        for word in words_with_no_repetition:
            word_sum = 0
            for char in word:
                word_sum += char_freq[char]
            word_score[word] = word_sum
        all_words_in_order = [k for k, v in sorted(word_score.items(), key=lambda item: -item[1])]
        result = []

        # Find words where the next word differ by at least 2 chars
        for word in all_words_in_order:
            if not result:
                result.append(word)
                continue
            if len(result)>10:
                break
            last_word_in_result = result[-1]
            if len(''.join(set(last_word_in_result).intersection(word))) <3:
                result.append(word)
        return result

    def highly_probable_letters(self):
        """ Returns a list of highly probable letters."""
        char_freq = self._char_frequency(self.words)
        return [k for k, v in sorted(char_freq.items(), key=lambda item: -item[1])]

    def find_word_with_a_substring(self, substring=None):
        """Returns a list of words when we have a substring."""
        if len(substring) > 5:
            print("Substring too long!")
            return
        if not substring:
            print("Substring cannot be empty.")
            return
        result = []
        counter_substring = collections.Counter(substring)
        for word in self.words:
            add_key = True
            counter_current_word = collections.Counter(word)
            for char, char_count in counter_substring.items():
                if char in counter_current_word and counter_current_word[char] == char_count:
                    continue
                add_key = False
                break
            if add_key:
                result.append(word)
        print("Substring matches for %s: %s" % (substring, sorted(result)))

def main():
    if len(sys.argv) > 3:
        print('Usage: python3 wordle_helper.py high_probable/ideal_start/substring_match')
        sys.exit()

    wordle = WordleHelper()
    wordle.create_list_of_words()

    if sys.argv[1] == "high_probable":
        if len(sys.argv) == 3:
            print('Usage: python3 wordle_helper.py high_probable')
            sys.exit()
        print("List of highly probable letters:", wordle.highly_probable_letters())

    elif sys.argv[1] == "ideal_start":
        if len(sys.argv) == 3:
            print('Usage: python3 wordle_helper.py ideal_start')
            sys.exit()
        print("List of ideal start word:", wordle.ideal_start_word())

    elif sys.argv[1] == "substring_match":
        if len(sys.argv) <3:
            print('Usage: python3 wordle_helper.py substring_match <substring>')
            sys.exit()
        wordle.find_word_with_a_substring(sys.argv[2])

    else:
        print('Usage: python3 wordle_helper.py high_probable/ideal_start/substring_match')
        sys.exit()

if __name__ == "__main__":
    main()
