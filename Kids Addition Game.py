import random
  

def addition_game():
    correct_answers = 0
    wrong_answer = 0

    for i in range(10):
       num1 = random.randint(1, 10)
       num2 = random.randint(1, 10)
       correct_result = num1 + num2


       question = f"What is {num1} added with {num2} ? "
       user_answer = int(input(question))


       if user_answer == correct_result:
          print(correct_result,"is Correct!, Smart Kid.")
          correct_answers += 1
       else:
         print("Wrong! The correct answer is.", correct_result)
         wrong_answer += 1

         
    print("Game Over!")
    print("Total Score Win:", correct_answers )
    print("Total Score Failed,", wrong_answer)

addition_game()

