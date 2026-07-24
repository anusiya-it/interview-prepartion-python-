english = int(input("Enter marks in english: "))
science = int(input("Enter marks in science: "))
Social = int(input("Enter marks in social: "))
total = english + science + Social
if total >90:
    print ("Grade A")
elif total >70:
    print("Grade B")
else:
    print("Grade C")