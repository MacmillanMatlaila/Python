print("Welcome to my Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's Play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower()  == "central processing unit":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")


answer = input("What does PSU stand for? ")
if answer.lower()  == "power supply unit":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")


answer = input("What does GPU stand for? ")
if answer.lower()  == "graphics processing unit":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")


answer = input("What does RAM stand for? ")
if answer.lower()  == "random access memory":
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer")

print(f"You got " + str(score) + " questions correct")
print(f"You got " + str((score/4)*100) + "% " "of the questions correct")

