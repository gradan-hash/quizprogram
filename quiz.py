

quiz = {
  "question1": {
    "question":"What is the capital of france?" ,
    "answer": "paris"
  },
  "question2": {
    "question":"Capital city of kenya? ",
    "answer": "Nairobi"
  },
  "question3":{
    "question":"Whats your hobby?",
  "answer":"coding"
  },
   "question4":{
    "question":"Whats your laptop type?",
  "answer":"hp"
  },
    "question5":{
    "question":"Do you have a girlfriend",
  "answer":"No"
  }
  

  }
while True:
  score= 0
  for key,value in quiz.items():
    print(value["question"])
    answer = input("Answer: ")
    
    if answer.lower() == value['answer'].lower():#converts input to lower and converts value of answer to lower case 
      print("Correct")
      score = score + 1
      print(f"Your score is {(score /5) *100}%")
      print("")
      
    else:
      print("Wrong! ")
      print(f"The answer is {value['answer']}")
      print(f"Your score is : {(score /5) *100}%")
      print("")
      
  print(f"You got {score} out of 5 questions ")
  print(f"Your percentage is {(score /5) *100}%")


  if score > 90:
    print("congratulation you have passed")
    print("")
  else:
    print("Good trial")
    print("")
    
    exit = input("Continue testing yourself? input yes or no: ")
    if exit =="no" or exit== "No":
      print("Thanks for your participation")
      quit()
   
    else:
      print("Start Again")
      print("")
      
   


