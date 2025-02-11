# Write your code here :-)
#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
# Write your code here :-)
name = input("What is your name? ")
age = int(input("How old are you? "))
next_year_age = age + 1
print("Hello, " + name + "! You are " + str(age) + " years old. Next year, you will be " + str(next_year_age) + " years old.")
#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
# Write your code here :-)
word = input("Enter a word: ")
times = int(input("How many times would you like to repeat the word? "))
print(word * times)
#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
# Write your code here :-)
sentence = input("Enter a sentence: ")
search_word = input("Enter the word you want to find: ")
found = word_to_find in sentence
print(found)
# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.

# Write your code here :-)
strl = "Woof" + " " + "There is a puppy" + "!"
score = str(100)
text = "Your score is "
print(text + score)

print(strl * 5)
str2 = "Hahahaha"
print(str2 * 11)
strl3 = "oopsies"
print(strl3 * 2)
#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.

# Write your code here :-)
print("apple", "banana", "cherry", sep="|")
