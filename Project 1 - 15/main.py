# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height ** 2)

if bmi < 18.5 :
    print(f"Your bmi is {bmi}, You Are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You Are normal")
elif bmi < 30:
    print(f"Your bmi is {bmi}, You Are overweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You Are obese")
else:
    print(f"Your bmi is {bmi}, You Are critically obese")