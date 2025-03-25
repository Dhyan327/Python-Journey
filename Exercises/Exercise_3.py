# In this part I will do "Exercise 3 Solution"
# Exercise :->
'''Create a program capable of displaying questions to the user like KBC.
 Use List data type to store the questions and their correct answers. 
 Display the final amount the person is taking home after playing the game.'''

# Exercise Solution :~~>

print(''' Welcome to "Kon Banega Crorepati" Let's Begin \n\n''')

i = 0
money_won = 0
while i < 10:
  print("1st question on the screen \n ")
  print("What is the capital of France? \n A. London \n B. Paris \n C. Rome \n D. Madrid\n ")
  answer=input("Enter your choice : ")
  if(answer == "A" or answer == "a"):
    print("Sahi jawab \n")
    money_won += 10000
    i = i + 1
    print("AAP 10,000 RUPAI JEET CHUKE HAI.. \n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai London\n")
    print("Better luck next time! \n")
    break

  print("2nd question on the screen\n ")
  print("Which planet is known as the Red Planet? \n A. Venus \n B. Mars \n C. Jupiter \n D. Saturn\n ")
  answer=input("Enter your choice : ")
  if(answer == "B" or answer == "b"):
    print("Sahi jawab")
    money_won += 20000
    i = i + 1
    print("AAP 30,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("\n Sahi jawab hai Mars\n")
    print("\n Better luck next time! \n")
    break

  print("3rd question on the screen\n")
  print("What is the chemical symbol for the element oxygen? \n A. O2 \n B. Ox \n C. O \n D. OxN\n")
  answer=input("Enter your choice : ")
  if(answer == "C" or answer == "c"):
    print("Sahi jawab\n")
    money_won += 50000
    i = i + 1
    print("AAP 80,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai O\n")
    print("Better luck next time! \n")
    break

  print("4th question on the screen\n")
  print('''Which planet is known as the "Morning Star" or "Evening Star"? \n A. Mars \n B. Venus \n C. Jupitor \n D. Saturn\n''')
  answer=input("Enter your choice : ")
  if(answer == "B" or answer == "b"):
    print("Sahi jawab\n")
    money_won += 70000
    i = i + 1
    print("AAP 1,50,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai Venus\n")
    print("Better luck next time! \n")
    break

  print("5th question on the screen\n")
  print('''Who wrote the play "Romeo and Juliet"? \n A. William Wordsworth \n B. Mark Twain \n C. William Shakespeare \n D. Charles Dickens \n''')
  answer=input("Enter your choice : ")
  if(answer == "C" or answer == "c"):
    print("Sahi jawab\n")
    money_won += 210000
    i = i + 1
    print("AAP 3,60,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai William Shakespeare\n")
    print("Better luck next time! \n")
    break

  print("6th question on the screen\n")
  print("Which gas do plants use for photosynthesis? \n A. Carbon dioxide \n B. Oxygen \n C. Nitrogen \n D. Hydrogen\n")
  answer=input("Enter your choice : ")
  if(answer == "A" or answer == "a"):
    print("Sahi jawab\n")
    money_won += 280000
    i = i + 1
    print("AAP 6,40,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai Carbon dioxide\n")
    print("Better luck next time! \n")
    break

  print("7th question on the screen\n")
  print("What is the largest mammal on Earth? \n A. African elephant \n B. Blue whale \n C. Giraffe \n D. Polar bear\n")
  answer=input("Enter your choice : ")
  if(answer == "B" or answer == "b"):
    print("Sahi jawab\n")
    money_won += 610000
    i = i + 1
    print("AAP 12,50,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai Blue whale\n")
    print("Better luck next time! \n")
    break

  print("8th question on the screen\n")
  print("Which famous scientist formulated the theory of relativity? \n A. Isaac Newton \n B. Albert Einstein \n C. Galileo Galilei \n D. Nikola Tesla\n")
  answer=input("Enter your choice : ")
  if(answer == "B" or answer == "b"):
    print("Sahi jawab\n")
    money_won += 1250000
    i = i + 1
    print("AAP 25,00,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai Albert Einstein\n")
    print("Better luck next time!\n ")
    break

  print("9th question on the screen\n")
  print('''Which country is known as the "Land of the Rising Sun"? \n A. China \n B. South Korea \n C. Japan \n D. Vietnam\n''')
  answer=input("Enter your choice : ")
  if(answer == "C" or answer == "c"):
    print("Sahi jawab\n")
    money_won += 2500000
    i = i + 1
    print("AAP 50,00,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai Japan\n")
    print("Better luck next time! \n")
    break

  print("10th and last question on the screen\n")
  print("What is the name of the hypothetical small, dense celestial object with gravity so strong that not even light can escape from it? \n A. White Dwarf \n B. Neutron Star \n C. Pulsar \n D. Black Hole\n")
  answer=input("Enter your choice : ")
  if(answer == "D" or answer == "d"):
    print("Sahi jawab\n")
    money_won += 5000000
    i = i + 1
    print("AAP 1,00,00,000 RUPAI JEET CHUKE HAI..\n")
  else:
    print("Galat jawab\n")
    print("Sahi jawab hai Black Hole \n")
    print("Better luck next time! \n")
    break
print("Aaj yaha se aap leke jaa rahe hai", money_won, "rupay ki dhanrashi \n")
print("Dhanyawad")