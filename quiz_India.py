print("Welcome to my India quiz!")

playing = input("Do you want to play?  :")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What Indian city is the capital of two states? options: 1.Kolkata 2.Chandigarh 3.Mumbai 4.Chennai  :")
if answer == "2":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many countries border India? options: 1.'12' 2.'7' 3.'6' 4.'9  :")
if answer == "3":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What, approximately, is the area of India, in square kilometers? options: 1.'3000000' 2.'1500000' 3.'4000000' 4.'2500000'  :")
if answer == "1":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is India’s smallest state by area? options: 1. 'Goa', 2.'Puducherry', 3.'Kerala', 4.'Manipur'  :")
if answer == "1":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("During what period does India’s wet season occur? options: 1.'mid june to early october', 2.'april and may ', 3.'november', 4.'december'  :")
if answer == "1":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("Which state in India do we find the wettest regions? options: 1.'Assam', 2.'Kerala ', 3.'Meghalaya, 4.'Nagaland'  :")
if answer == "3":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 6) * 100) + "%.")