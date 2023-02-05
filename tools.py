class MyCounter():
    def __init__(self):
        self.count = 0
    def get_count(self):
        return self.count-1
    def get_count_and_add_one(self):
        self.count += 1
        return self.count-1