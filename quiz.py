print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

name = input('Type your name ').upper()

print("Okay! Lets play " + str(name) + " :) ")
score = 0

#Question one

answer = input("HTML is a language? ")
if answer.lower() == "yes":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#Question Two

answer = input("Java and Javascript is the same thing? ")
if answer.lower() == "no":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#Question Three

answer = input("What is a Fullstack? ")
if answer.lower() == "a multi task developer":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#Question Four

answer = input("What is Browsers? ")
if answer.lower() == "a search place":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

#Question Five

answer = input("Bootstrap is a...? ")
if answer.lower() == "framework":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Congrats " + str(name) + "! You got " + str(score) + " questions correct!" )

print("You got " + str((score / 5) * 100)  + "%." )
