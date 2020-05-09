import random, re
print("H A N G M A N")
while True:
	menu = input('Type "play" to play the game, "exit" to quit: ')
	if menu == "play":
		choisen_word = input("Enter your word: ")
		choisen_word_list = [i  for i in choisen_word]
		letters_guessed_set = set()
		lives = 8
		word =["-" for i in  range(len(choisen_word_list))]
		while True:
		    print('\n')
		    print(''.join(word))
		    guessed_letter = input("Input a letter: ")
		    if len(guessed_letter)!=1:
		        print("You should print a single letter")
		        continue
		    checker = re.search("[a-z]", guessed_letter)
		    if checker == None:
		        print("It is not an ASCII lowercase letter")
		        continue
		    if guessed_letter in choisen_word_list and guessed_letter not in letters_guessed_set:
		        while True:
		            word[choisen_word_list.index(guessed_letter)]=guessed_letter
		            choisen_word_list[choisen_word_list.index(guessed_letter)] = '-'
		            if guessed_letter not in choisen_word_list:
		                break
		        letters_guessed_set.add(guessed_letter)
		    elif guessed_letter in letters_guessed_set:
		        print("You already typed this letter")        
		    elif guessed_letter not in choisen_word_list:
		        print("No such letter in the word")
		        letters_guessed_set.add(guessed_letter)
		        lives-=1
		    if lives==0:
		        print("You are hanged!")
		        break
		    if ''.join(word)==choisen_word_list:
		        print(
		                """You guessed the word!
		                    You survived!""")
		        break
	elif menu == "exit":
		break
	else:
		continue
	               
