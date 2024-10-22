# PEMDAS
# ()
# **
# * OR /
# + OR -
from math import floor

from Day_02.Reverse_a_word_in_Sentence import result

'''
print("My Age" + str(12))
print(123 + 123)

bmi = 84 / 1.65 ** 2
print(round(bmi,2))

score = 0
height = 1.0
is_winning = True

print(f"Your score is - {score}\nYour height is - {height}\nYour Winning is - {is_winning}")

'''

print("Welocme to the tip calculator!")
print("What is your total bill? $")
total_bill = float(input())

print("How much tip would you like to give? 10, 12, 0r 15?")
tip = int(input())
print("How many people to split the bill?")
how_many_people_to_split_bill = int(input())

tip_as_percentage = tip / 100
total_tip_amount = total_bill * tip_as_percentage
total_bill = total_bill + total_tip_amount
bill_per_person = total_bill / how_many_people_to_split_bill
final_amount = round(bill_per_person,2)
print(f"Each person should pay: + ${final_amount} ")

