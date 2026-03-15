class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, rest_days, hours=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            self.hours = (7 - self.rest_days) * 8
        return self.hours

    def get_email(self):
        if self.email is None:
            self.email = f"{self.name}@email.com"
        return self.email

    @classmethod
    def set_hourly_payment(cls, new_payment=None):
        cls.hourly_payment = new_payment
        return cls.hourly_payment

    def salary(self):
        salary = self.get_hours() * EmployeeSalary.hourly_payment
        return salary
