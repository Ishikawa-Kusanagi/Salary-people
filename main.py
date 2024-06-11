from application.db.people import People
from application.salary import Salary

people = People('Dmitri')
salary = Salary('alex', 1234)
if __name__ == '__main__':
    People.get_current_time()
    Salary.calculate_salary()