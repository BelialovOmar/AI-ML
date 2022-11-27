import random

# Python — язык с динамической типизацией
# Динамическая типизация позволяет сделать следующее:
# a = 10;
# a = "Hello";
# Т.е. благодаря этому мы можем поменять тип данных значения, которое хранится в переменной

# По сути, наша переменная "а" — это указатель, который указывает на объекты, что выделяются в куче и, по необходимости, указатель просто указывает на другие объекты другого типа

word_to_guess = "academy"
letters_used = ""
failed_attempts = 0

# Циклы 

while failed_attempts < 6: #начало цикла ":", круглые скобки для условия цикла не ставятся
    letter = input("Enter your letter: ") #часть цикла
    letters_used += letter
    
    if letter in word_to_guess:
        print(f"Well done! Letter {letter} is present in this word!")
    else:
        print("Sorry! You are wrong :(")
        failed_attempts += 1 #++ в Python не работает; мы пишем += или = failed_attempts + 1

    correct_letters = 0

    for ch in word_to_guess:
        if ch in letters_used: #для каждого символа в нашем слове мы делаем проверку
            print(f"{ch}", end = '') #если буква, которую мы ввели, есть в этом слове, то мы выводим эту букву
            correct_letters += 1
        else:
            print("_", end ='')
    print()

    if correct_letters == len(word_to_guess):
        print(f"Great! You won! The word is {word_to_guess}")
        break
else:
    print("Sorry, you lost!") 
