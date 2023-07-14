'''This program is use to check for the highest, lowest, 
second_highest,second_lowest and third_lowest in the loop
It also calculate the  total sum / average of the scores
'''
# Score Analysis and Ranking 

print("Enter (10) test score: ")

highest = float("-inf")
second_highest = float("-inf")

lowest = float("inf")
second_lowest =float("inf")
third_lowest = float("inf")

scores = []

for _ in range(10):
    score = int(input("Enter a score:"))
    
    #Use in adding score in the scores = [] variables
    scores.append(score)
     
     # use to find the total sum scores and average score
    average = sum(scores) / len(scores)
    score_total = sum(scores)

    # checking if scores(Highest or Lowest is out of range in the loop)

    if score > 100 or score < 1:
        print("Enter score within 1 _ 100, Score is out of range")
        continue
    
    # use to check for Highest score/second highest score
    if score > highest:
        second_highest = highest
        highest = score
    elif score > second_highest:
        second_highest = score

    
     # use to check for Lowest/second/third lowest score
    if score < lowest:
        third_lowest = second_lowest
        second_lowest = lowest
        lowest= score
    elif score < second_lowest:
        third_lowest = second_lowest
        second_lowest = score
    elif score < third_lowest:
        third_lowest = score


    
#I use print function to print out the output/result
print(f"Highest score is {highest}, Second highest is {second_highest}.")
print(f"Lowest score is {lowest}, second lowest is {second_lowest}.")
print(f"The Total Average of Scores is {average}.")
print(f"The Third lowest is {third_lowest}")
print(f"The Second and Third lowest: Second_lowest is {second_lowest}, and Third_lowest is {third_lowest}")
print(f"Here are your score:  {scores}.")
print(f"Total Score: {score_total}")
    
