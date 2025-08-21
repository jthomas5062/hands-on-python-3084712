# Python quiz game

questions = ("How many elements are there in the Periodic Table?:", 
             "Which animal lays the largest eggs?:", 
             "What is the most abundant gas in the Earth's atmosphere?:", 
             "How many bones are there in the adult human body?:", 
             "Which planet in the solar system is the hottest?:")

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Ostrich", "B. Emu", "C. Kiwi", "D. Cassowary"), 
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Argon"), 
           ("A. 206", "B. 208", "C. 210", "D. 212"), 
           ("A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0 

for question in questions:
  print("-----------------------")
  print(question)
  for option in options[question_num]:
    print(option)

  guess = input("Enter A, B, C, or D: ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    print("Correct!")
    score += 1
  else:
    print("Incorrect.")
    print(f"{answers[question_num]} is the correct answer.")
  question_num += 1

print("-----------------------")
print("        Results        ")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
  print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
  print(guess, end=" ")
print()

score = score / len(questions) * 100
print(f"Your score is {score}%.")