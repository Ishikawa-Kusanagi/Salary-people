import datetime
class People:
    def __init__(self, name):
        self.name = name
    @staticmethod
    def get_current_time():
        current_time = datetime.datetime.now()
        print(current_time)

