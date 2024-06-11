salary_list = ['Igor', 'Alex', 'Dmitrii', 'Vitalyi']
class Salary:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @staticmethod
    def calculate_salary():
        print(len(salary_list))