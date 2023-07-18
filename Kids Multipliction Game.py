import random

#Kids Mulipication Game by Judith

def multiplication_game():
    correct_answers = 0
    wrong_answers = 0
    

    
    for i in range(1,11):
       num1 = random.randint(1, 10)
       num2 = random.randint(1, 10)
       correct_result = num1 * num2

      

       question = f"What is {num1} multiplied by {num2}?  "
       user_answer= int(input(question))



       if user_answer == correct_result:
          print(correct_result,"is Correct!, Smart Kid.")
          correct_answers += 1
       elif user_answer !=correct_result:
          print("Wrong Answers")   
          wrong_answers += 1
          print("the correct answer is ", correct_result)

         
          

    print("Game Over")
    print("Total Correct Answers is ", correct_answers)
    print("Total Wrong  Answers is ", wrong_answers)
    print(f"You got {correct_answers} correctly, failed {wrong_answers}.")
  
multiplication_game()

