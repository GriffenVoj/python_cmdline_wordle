import random
from colorama import init, Fore, Style
init()
import collections 
#open data
words=open("words.txt").read().splitlines()

#generate starting case
sub_word=random.choice(words)
hidden_word=[t for t in sub_word]
count=collections.Counter()
accepted_guesses=open("guesses.txt").read().splitlines()
correct=True
guesses=0
used=set()
did_it=False
alphabet=[["q","w","e","r","t","y","u","i","o","p"],["a","s","d","f","g","h","j","k","l"],["z","x","c","v","b","n","m"]]
#start
print("good luck! (due to limitations with colorama, only your last guess will be displayed)")
print("Note: the key board will show letters not yet used, but will only remove lower case letters")


#the game
while correct and guesses!=6:  
    r=collections.Counter()
    difference=collections.Counter()
    letter=dict()
    green_index=[]
    yellow_index=[]
    correct_input=True
    sub=""
    x=input("please enter word")
    guess=[i for i in x]
    if len(guess)!=5 or (x not in accepted_guesses and x not in words):
        if len(guess)!=5:
            print("try again")
        if x not in accepted_guesses and x not in words:
            print("word not in wordlist")
        correct_input=False
    if correct_input:
        for item in guess:
            if item in alphabet[0]:
                alphabet[0].remove(item)
            if item in alphabet[1]:
                alphabet[1].remove(item)
            if item in alphabet[2]:
                alphabet[2].remove(item)
    if guess==hidden_word:
        correct=False
        guesses=6
        did_it=True
        print("good job!")
    for i in range(len(hidden_word)):
        count[hidden_word[i]]+=1
    for i in range(len(guess)):
        r[guess[i]]+=1
        letter[i]=guess[i]
    for key in count:
        if key in count and key in r:
            difference[key]=r[key]-count[key]
    for i in range(len(guess)):
        if not correct_input: break
        if guess[i] in hidden_word:
           if guess[i]==hidden_word[i]:
               green_index.append(i)
               if difference[guess[i]]==1:
                   remove_letter=hidden_word.index(guess[i])
                   yellow_index.remove(remove_letter)
               difference[guess[i]]-=1
        if r[guess[i]]<=count[guess[i]]:
            if difference[guess[i]]>-1:
                yellow_index.append(i)
                difference[guess[i]]-=1
            
        if r[guess[i]]>count[guess[i]]:
            if difference[guess[i]]>=1:
                yellow_index.append(i)
            difference[guess[i]]-=1
    if yellow_index or green_index:
        for x in range(5):
            if x in green_index:
                sub+=f"{Fore.GREEN}{guess[x]}"
            elif x in yellow_index:
                sub+=f"{Fore.YELLOW}{guess[x]}"
            else:
                sub+=f"{Style.RESET_ALL}{guess[x]}"
            
    print(f"{Style.RESET_ALL}{sub}")
    if correct_input:
        guesses+=1
    print(f"{Style.RESET_ALL} \t")
    print(alphabet)
if not did_it:
    print(f"try again! the word was:{hidden_word}")
   



