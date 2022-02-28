var_secret_word = "giraffe"
guess = ""
guess_cnt = 0
guess_limit = 3
out_of_guess = False

while var_secret_word != guess and not out_of_guess:
    if guess_cnt < guess_limit:
        guess = input("Enter guess : ")
        guess_cnt += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You Lose !")
else:
    print("You win !")
