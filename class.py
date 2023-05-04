#  Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
    #          - show_full_name
    #          - year_of_birth
    #          - show_initials
class Student:
    first_name="orishaba"
    last_name="mercy"
    age=30
    country="Kenya"

def __init__(self,full_name,year_of_birth,show_inituals):
    self.First_name=full_name
    self.year_of_birth=year_of_birth
    self.show_inituals=show_inituals
student=Student()
print(f"Student:{student.first_name} {student.last_name}")



def year_of_birth(self):
    current_year = 2023
    current_year-30
    print(current_year-age_years)


def show_inituals(full_name):
    if(len(full_name)==0):
        return
    show_inituals= ''.join([name[0].upper()+"." for name in full_name.split(' ')])
    return show_inituals
full_name="Orishaba Mercy"
print(f"show_inituals:{show_inituals(full_name)}")


# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

