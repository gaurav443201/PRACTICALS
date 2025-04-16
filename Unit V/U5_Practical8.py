"""
Create class EMPLOYEE for storing details (Name, Designation, gender, Date of Joining and
Salary). Define function members to compute a)total number of employees in an organization
b) count of male and female employee c) Employee with salary more than 10,000 d) Employee
with designation “Asst Manager”
"""
class EMPLOYEE:
    # Class variable to keep track of all employee objects
    employee_list = []

    def __init__(self, name, designation, gender, date_of_joining, salary):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.date_of_joining = date_of_joining
        self.salary = salary

        # Add the new employee to the list
        EMPLOYEE.employee_list.append(self)

    @classmethod
    def total_employees(cls):
        return len(cls.employee_list)

    @classmethod
    def gender_count(cls):
        male = sum(1 for emp in cls.employee_list if emp.gender.lower() == "male")
        female = sum(1 for emp in cls.employee_list if emp.gender.lower() == "female")
        return male, female

    @classmethod
    def salary_above(cls, amount):
        return [emp.name for emp in cls.employee_list if emp.salary > amount]

    @classmethod
    def designation_filter(cls, designation):
        return [emp.name for emp in cls.employee_list if emp.designation.lower() == designation.lower()]


# Create some employees
e1 = EMPLOYEE("Alice", "Asst Manager", "Female", "2020-03-15", 12000)
e2 = EMPLOYEE("Bob", "Developer", "Male", "2019-07-22", 9500)
e3 = EMPLOYEE("Charlie", "Asst Manager", "Male", "2021-01-10", 15000)
e4 = EMPLOYEE("Diana", "HR", "Female", "2018-09-30", 8500)

# a) Total number of employees
print("Total employees:", EMPLOYEE.total_employees())

# b) Count of male and female employees
males, females = EMPLOYEE.gender_count()
print("Male employees:", males)
print("Female employees:", females)

# c) Employees with salary > 10,000
high_salary = EMPLOYEE.salary_above(10000)
print("Employees with salary > 10,000:", high_salary)

# d) Employees with designation "Asst Manager"
asst_managers = EMPLOYEE.designation_filter("Asst Manager")
print("Employees with designation 'Asst Manager':", asst_managers)





"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U5_Practical8.py
Total employees: 4
Male employees: 2
Female employees: 2
Employees with salary > 10,000: ['Alice', 'Charlie']
Employees with designation 'Asst Manager': ['Alice', 'Charlie']
"""