'''Day 2,   
Challenge: Aisa Python program likhna hai jo user se ek sentence le ,
aur usme jitne words hain, count kare! 
'''
# Using input() to get the sentence from user
# Using split() to count words in a sentence
# Using len() to get the word count
sentence_Input=input("Enter any sentence: ")
sentence_list=sentence_Input.split()
sentence_count=len(sentence_list)
print("number of words in the sentence is:",sentence_count)