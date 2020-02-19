print("Risky Business Day \nby LD '23)

score=0
my_list=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
import random
def checkAnswer(question,corr,score):
  ans=input(question)
  if ans in corr:
    print ("Correct answer! Good Job.")
    score=score+1
    print ("your total amount of correct answers is:") 
    print (score)
    print ("\n")
  else:
    print ("Sorry, that was incorrect.")
    print ("your total amount of correct answers is:") 
    print (score)
    print ("\n")
  return score

question=''
for x in range(5):
  while question not in my_list:
        length=len(my_list)
        num=random.randrange(length)
        question=my_list[num]
  my_list.remove(question)
  if question=="a":
        score=checkAnswer("who is the richest man on Earth currently? a. Warren Buffet b. Jeff Bezos c. Bill Gates d. Steve Jobs",['b','Jeff Bezos'],score)

  if question=="b":
        score=checkAnswer("Who is currently the richest woman on Earth? a. Bettencourt Meyers b. MacKenzie Bezos c. Kim Kardashian d. Kylie Jenner",['a','Bettencourt Meyers'],score)

  if question=="c":
        score=checkAnswer("What is the largest company currently?",['Apple'],score)

  if question=="d":
        score=checkAnswer("What is the second largest company currently?",['Alphabet'],score)

  if question=="e":
        score=checkAnswer("What is the third largest company currently?",['Microsoft'],score)  

  if question=="f":
        score=checkAnswer("what is the oldest company still operating today?",['Kongo Gumi'],score)
        
  if question=="g":
        score=checkAnswer("When was the oldest company created established? a. 578 b. 452 c. 1023 d. 1430",['a','578'],score)

  if question=="h":
        score=checkAnswer("When was the first bank ever, Banca Monte dei Paschi di Siena, established a. 1580 b. 1472 c. 1396 d. 1623",['b','1472'],score)

  if question=="i":
        score=checkAnswer("Which car company has produced the most cars: Honda, GM, Toyota, or Nissan?",['Toyota'],score)

  if question=="j":
        score=checkAnswer("True or False: Toyota has produced over 20 million cars.",['True'],score)

  if question=="k":
        score=checkAnswer("True or False: Bill Gates is the richest man to have ever lived.",['False'],score)

  if question=="l":
        score=checkAnswer("True or False: Andrew Carnegie made his money from trains and cars",['False'],score)

  if question=="m":
        score=checkAnswer("How did John Rockefeller primarily make his money? a. Steel b. Railroads c. Oil d. Coal",['c','Oil'],score)

  if question=="n":
        score=checkAnswer("What was the first company to go public? a. General Electric b. Sothebys c. Hersheys d. Dutch East India Company",['d','Dutch East India Company'],score)

  if question=="o":
        score=checkAnswer("How many businesses close each year? A. 595,000 b. 330,000 c. 725,000 d. 96,000",['a','595,000'],score)

  if question=="p":
        score=checkAnswer("True or false: Revenue is a companies loss of money",['False'],score)

  if question=="q":
        score=checkAnswer("True or False: Profit is a companies net gain in money",['True'],score)

  if question=="r":
        score=checkAnswer("Is Athenian for profit or non-profit?",['non-profit','non profit'],score)

  if question=="s":
        score=checkAnswer("What is it called when a business buys another one?",['acquisition',score])
