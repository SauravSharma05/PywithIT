class DaySwitcher:
    def day(self, dayOfWeek):
        method_name = f'case_{dayOfWeek}'
        method = getattr(self, method_name, self.default)
        return method()

    def case_1(self):
        return "Monday"

    def case_2(self):
        return "Tuesday"

    def case_3(self):
        return "Wednesday"

    def case_4(self):
        return "Thursday"

    def case_5(self):
        return "Friday"

    def default(self):
        return "Invalid day"

switcher = DaySwitcher()
print(switcher.day(1))  
print(switcher.day(4))  