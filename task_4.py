class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, rest_days, hours=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, employee):
        if employee.hours is None:
            employee.hours = (7 - employee.rest_days) * 8
        return employee.hours

    @classmethod
    def get_email(cls, employee):
        if employee.email is None:
            employee.email = f"{employee.name}@email.com"
        return employee.email

    @classmethod
    def set_hourly_payment(cls, new_payment=None):
        cls.hourly_payment = new_payment
        return cls.hourly_payment

    def salary(self):
        salary = self.get_hours(self) * self.hourly_payment
        return salary
