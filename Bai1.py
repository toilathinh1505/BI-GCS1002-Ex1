CURRENT_YEAR = 2023

firstname = input("Please enter your first name :")
lastname = input("Please enter your last name : ")
date_of_birth = input("Enter your Date of Birth :")
phone_number = input("Enter your phone number :")
born = input("Enter where you born :")
year_born = int(input("When were you born:"))
career = input("Enter Career :")
school = input("Enter where you study : ")
height_meter = input("Enter your height : ")
entrance_year = int(input("Enter year entrance in University : "))

height_meter = float(height_meter)
height_feet = height_meter * 3.281
height_feet = round(height_feet,1)
age = CURRENT_YEAR - year_born
year_in_university = CURRENT_YEAR - entrance_year



print("\n -------- ")
print("{2} : {0}{1}".format(firstname,lastname,"Fullname"))
print("Date of Birth " + date_of_birth)
print("Phone number " + phone_number)
print("Born at " + born)
print("Your age is : " + str(age))
print("Your height is : " + str(height_feet))
print("Career : " + career)
print("Study at : " + school)
print("Study at University in " + str(year_in_university) + "years")




