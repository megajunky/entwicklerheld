import numpy as np

def find_all_words(letter_array, word_dictionary_array):
    #convert letter_array to dict of occurences
    unique, counts = np.unique(letter_array, return_counts=True)
    #zip conpresses to list of same length to list of tuples
    #e.g. zip(['a', 'b'], [2, 3]) => [('a', 2), ('b', 3)]
    letter_dict = dict(zip(unique, counts))

    #check if there are enough letter in the letter_dict to
    #construct the word
    def check_word(word):
            uni, cou = np.unique(list(word), return_counts=True)
            #iterate over all unique letter in the word with their count
            for l, c in zip(uni, cou):
                if l not in letter_dict or letter_dict[l] < c:
                    return False
            return True

    #filter all words for which the check_word fuction returns True
    return list(filter(check_word, word_dictionary_array))
    

if __name__ == "__main__":
    letters = ['h', 'a', 'l', 'l', 'o']
    words = ["hallo"]
    print(find_all_words(letters, words))

