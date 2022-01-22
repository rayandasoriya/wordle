# Wordle Helper

This is a wordle helper application which can be used while playing wordle(https://www.powerlanguage.co.uk/wordle/).

Currently, three features are being implemented:
1. Find high probable characters: This will return a list of alphabets which are highly probable.

    Usage: `python3 wordle_helper.py high_probable`
2. Find an ideal start for the game: This will give you a list of top 10 ideal starts of the game.

    Usage: `python3 wordle_helper.py ideal_start`
3. Find a word from a substring: When you have identified some letters, pass it as a substring and the function will return a list of words which contain those characters.
    
    Usage: `python3 wordle_helper.py substring_match <substring>`


Any new recommendations are welcome! I'd also like to thank https://eslforums.com/5-letter-words/ for the database of 5 letter words.

PS: This program does not use any machine learning capabilities.
