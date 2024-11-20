class Employee:
    def __init__(self, name, job_title, salary, years_of_experience):
        self.name = name
        self.title = job_title
        self.salary = salary
        self.exp = years_of_experience

    def change_job_title(self, new_title):
        print(f"{self.name} has changed from {self.title} to {new_title}")
        self.title = new_title

    def increase_salary(self, percentage):
        print(f"{self.name}'s salary increased from {self.salary} to {round(self.salary * (percentage/100),2)}")
        self.salary *= (percentage/100)

    def increase_exp(self):
        print(f"{self.name} has gained 1 year of experience")
        self.exp += 1

    def calculate_hourly_rate(self, hours):
        print(f"{self.name}'s hourly rate is {self.salary/hours}")

class Manager(Employee):
    def __init__(self, name, job_title, salary, years_of_experience, bonus):
        super().__init__(name, job_title, salary, years_of_experience)
        self.bonus = bonus

    def calculate_bonus(self):
        self.bonus = round(self.exp*0.8 * self.salary, 2)
        print(f"{self.name}'s bonus is {self.bonus}")


manager = Manager("Bob", "Manager", 50000, 5, 1000)
employee = Employee("John", "Window Cleaner", 20000, 2)