''' A program using functions for text analysis.
October 7, 2014
Lab 06
@authors Ethan Clark (elc3)
'''
#The huge list of green eggs and ham.
green_eggs_and_ham = [ "i", "am", "sam", "sam", "i", "am", "that",
            "sam-i-am", "that", "sam-i-am", "i", "do", "not", "like", "that", "sam-i-am", "do",
            "you", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them",
            "sam-i-am", "i", "do", "not", "like", "green", "eggs", "and", "ham", "would", "you",
            "like", "them", "here", "or", "there", "i", "would", "not", "like", "them", "here",
            "or", "there", "i", "would", "not", "like", "them", "anywhere", "i", "do", "not",
            "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am",
            "would", "you", "like", "them", "in", "a", "house", "would", "you", "like", "them",
            "with", "a", "mouse", "i", "do", "not", "like", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would",
            "you", "eat", "them", "in", "a", "box", "would", "you", "eat", "them", "with", "a",
            "fox", "not", "in", "a", "box", "not", "with", "a", "fox", "not", "in", "a", "house",
            "not", "with", "a", "mouse", "i", "would", "not", "eat", "them", "here", "or", "there",
            "i", "would", "not", "eat", "them", "anywhere", "i", "would", "not", "eat", "green",
            "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would", "you",
            "could", "you", "in", "a", "car", "eat", "them", "eat", "them", "here", "they", "are",
            "i", "would", "not", "could", "not", "in", "a", "car", "you", "may", "like", "them",
            "you", "will", "see", "you", "may", "like", "them", "in", "a", "tree", "not", "in",
            "a", "tree", "i", "would", "not", "could", "not", "in", "a", "tree", "not", "in", "a",
            "car", "you", "let", "me", "be", "i", "do", "not", "like", "them", "in", "a", "box",
            "i", "do", "not", "like", "them", "with", "a", "fox", "i", "do", "not", "like", "them",
            "in", "a", "house", "i", "do", "not", "like", "them", "with", "a", "mouse", "i", "do",
            "not", "like", "them", "here", "or", "there", "i", "do", "not", "like", "them",
            "anywhere", "i", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not",
            "like", "them", "sam-i-am", "a", "train", "a", "train", "a", "train", "a", "train",
            "could", "you", "would", "you", "on", "a", "train", "not", "on", "a", "train", "not",
            "in", "a", "tree", "not", "in", "a", "car", "sam", "let", "me", "be", "i", "would",
            "not", "could", "not", "in", "a", "box", "i", "could", "not", "would", "not", "with",
            "a", "fox", "i", "will", "not", "eat", "them", "with", "a", "mouse", "i", "will",
            "not", "eat", "them", "in", "a", "house", "i", "will", "not", "eat", "them", "here",
            "or", "there", "i", "will", "not", "eat", "them", "anywhere", "i", "do", "not", "like",
            "them", "sam-i-am", "say", "in", "the", "dark", "here", "in", "the", "dark", "would",
            "you", "could", "you", "in", "the", "dark", "i", "would", "not", "could", "not", "in",
            "the", "dark", "would", "you", "could", "you", "in", "the", "rain", "i", "would",
            "not", "could", "not", "in", "the", "rain", "not", "in", "the", "dark", "not", "on",
            "a", "train", "not", "in", "a", "car", "not", "in", "a", "tree", "i", "do", "not",
            "like", "them", "sam", "you", "see", "not", "in", "a", "house", "not", "in", "a",
            "box", "not", "with", "a", "mouse", "not", "with", "a", "fox", "i", "will", "not",
            "eat", "them", "here", "or", "there", "i", "do", "not", "like", "them", "anywhere",
            "you", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like",
            "them", "sam-i-am", "could", "you", "would", "you", "with", "a", "goat", "i", "would",
            "not", "could", "not", "with", "a", "goat", "would", "you", "could", "you", "on", "a",
            "boat", "i", "could", "not", "would", "not", "on", "a", "boat", "i", "will", "not",
            "will", "not", "with", "a", "goat", "i", "will", "not", "eat", "them", "in", "the",
            "rain", "i", "will", "not", "eat", "them", "on", "a", "train", "not", "in", "the",
            "dark", "not", "in", "a", "tree", "not", "in", "a", "car", "you", "let", "me", "be",
            "i", "do", "not", "like", "them", "in", "a", "box", "i", "do", "not", "like", "them",
            "with", "a", "fox", "i", "will", "not", "eat", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "you",
            "do", "not", "like", "them", "so", "you", "say", "try", "them", "try", "them", "and",
            "you", "may", "try", "them", "and", "you", "may", "i", "say", "sam", "if", "you",
            "will", "let", "me", "be", "i", "will", "try", "them", "you", "will", "see", "say",
            "i", "like", "green", "eggs", "and", "ham", "i", "do", "i", "like", "them", "sam-i-am",
            "and", "i", "would", "eat", "them", "in", "a", "boat", "and", "i", "would", "eat",
            "them", "with", "a", "goat", "and", "i", "will", "eat", "them", "in", "the", "rain",
            "and", "in", "the", "dark", "and", "on", "a", "train", "and", "in", "a", "car", "and",
            "in", "a", "tree", "they", "are", "so", "good", "so", "good", "you", "see", "so", "i",
            "will", "eat", "them", "in", "a", "box", "and", "i", "will", "eat", "them", "with",
            "a", "fox", "and", "i", "will", "eat", "them", "in", "a", "house", "and", "i", "will",
            "eat", "them", "with", "a", "mouse", "and", "i", "will", "eat", "them", "here", "and",
            "there", "say", "i", "will", "eat", "them", "anywhere", "i", "do", "so", "like",
            "green", "eggs", "and", "ham", "thank", "you", "thank", "you", "sam-i-am"]

#Definition of stop words.
stop_words = [ "a", "able", "about", "across", "after", "all",
            "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be",
            "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does",
            "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have",
            "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is",
            "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most",
            "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or",
            "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so",
            "some", "than", "that", "the", "their", "them", "then", "there", "these", "they",
            "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when",
            "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you",
            "your" ]

#Test lists for all exercises
list_one = []
list_two = ['Ethan']
list_three = ['Jaymes', 'Mark', 'Emily', 'Halley']
list_four = ['Detroit', 'Chicago', 'Boston']

#Function to search for a target_word in a list, exercise 6.3
def search(str_list, target_word):
    pos_indicator = 0
    if str_list == []:
        return -1
    for c in str_list:
        if c == target_word:
            return pos_indicator
        pos_indicator += 1
            
#Function to test the search function, exercise 6.3    
def test_search():
    print(search(list_one, 'programming'))
    print(search(list_two, 'Ethan'))
    print(search(list_three, 'Emily'))
    print(search(list_four, 'Chicago'))

'''Algorithm for exercise 6.4.
Define a function that has one parameter of a list.
Create a variable for each longest word and shortest word.
Initialize the longest word variable to have length of 0.
Initialize the shortest word variable to have a length of a huge number (1000).
Write a for loop that goes through each element in a list.
Compare each word with the previous one to see which is longer in length.
Write a for loop that goes through each element in a list.
Compare each word with the previous one to see which is shorter in length.
Print each the longest word and the shortest word in the list.
'''    
#Function to print the shortest and longest lengths of words of a list, exercise 6.4
def longest_and_shortest(list_words):
    longest_word_length = 0
    shortest_word_length = 1000
    if list_words == []:
        print('The given list was empty!')
    else:
        for c in list_words:
            if len(c) > longest_word_length:
                longest_word_length = len(c)
        print('The length of the longest word is', longest_word_length)
        for c in list_words:
            if len(c) < shortest_word_length:
                shortest_word_length = len(c)
        print('The length of the shortest word is', shortest_word_length)

#Test function to test the longest and shortest function, exercise 6.4    
def test_length():
    print(longest_and_shortest(list_one))
    print(longest_and_shortest(list_two))
    print(longest_and_shortest(list_three))
    print(longest_and_shortest(list_four))

'''Algorithm for exercise 6.5
Define a function that has parameters of two lists.
Set a counter equal to 0.
Write a loop that uses the word of one function and uses the search function
to see if that word does not appear in the second list.
Increase the counter by 1 if the stop word does not appear in the list.
Return counter.
'''

def count_words_not_present(one_list, two_list):
    counter = 0
    for c in one_list:
        if search(two_list, c) == -1:
            counter += 1
        return counter
        

#Function to analyze green eggs and ham, exercises 6.3, 6.4, and 6.5.
def green_eggs_and_ham_analysis():
    print(search(green_eggs_and_ham, 'i'))
    print(search(green_eggs_and_ham, 'boat'))
    print(search(green_eggs_and_ham, 'fox'))
    print(search(green_eggs_and_ham, 'thank'))
    print(search(green_eggs_and_ham, 'book'))
    print(longest_and_shortest(green_eggs_and_ham))
    
#Exercise 6.1
#print(len(green_eggs_and_ham))

#test_search()
#test_length()

#Call the function to analyze green eggs and ham, exercises 6.3, 6.4, and 6.5
green_eggs_and_ham_analysis()