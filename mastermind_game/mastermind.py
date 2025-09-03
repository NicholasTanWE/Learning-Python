@ -0,0 +1,48 @@
import random
#generate 4 digit code A to F
def generate_code():
    list_chr=[]
    for x in range(4):
        list_chr.append(chr(random.randrange(65,71)))
    random_code="".join(list_chr)
    return random_code
#logic for counting correct and incorret guesses
def count_exact_and_inexact_matches(guessed_code, secret_code):
#counting exact matches
    exact_matches=0
    remaining_guess=[]
    remaining_secretcode=[]
    for i in range(4):
        if guessed_code[i] is secret_code[i]:
            exact_matches+=1
        else:
#logic for populating wrong guesses into remaining to use for counting inexact matches
            remaining_guess.append(guessed_code[i])
            remaining_secretcode.append(secret_code[i])
#counting inexact matches
    inexact_matches=0
    for n in range(len(remaining_guess)):
        if remaining_guess[n] in remaining_secretcode:
            inexact_matches+=1
        else:
            continue
    #do not edit next line
    return (exact_matches, inexact_matches)
    
# Main game starts here...
secret_code=generate_code()
print("DEBUG MESSAGE: secret_code=",secret_code)
for tries in range(1,11):
    print("Attempt number:",tries)    
    guess=input("What is your guess? ")
    if len(guess)==4:
        if guess==secret_code:
            print("Feedback: Num correct exactly: 4.  Num correct inexactly: 0\nCongratulations. That took "+str(tries)+" tries.")    
            break
        else:
            exact_matches, inexact_matches = count_exact_and_inexact_matches(secret_code, guess)
            feedback="Num correct exactly: "+str(exact_matches)+".  Num correct inexactly: "+str(inexact_matches)
            print("Feedback:",feedback)
        
    else:
        print("Please enter a string of length 4.")
