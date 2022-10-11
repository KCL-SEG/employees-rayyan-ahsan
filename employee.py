"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    def __init__(self, name, salarypay):
        self.salarypay = salarypay
        super().__init__(name)
    
    def get_pay(self):
        return self.salarypay
    
    def __str__(self):
        return self.name + ' works on a monthly salary of ' + str(self.salarypay) + '.  Their total pay is ' + str(self.get_pay()) + '.'

class HourlyEmployee(Employee):
    def __init__(self, name, hours, rate):
        self.hours = hours
        self.rate = rate
        super().__init__(name)

    def get_pay(self):
        return self.hours * self.rate
    
    def __str__(self):
        return self.name + ' works on a contract of ' + str(self.hours) + ' hours at ' + str(self.rate) + '/hour.  Their total pay is ' + str(self.get_pay()) + '.'

class SalaryCommissionEmployee(SalaryEmployee):
    def __init__(self, name, salarypay, contracts, commission):
        self.contracts = contracts
        self.commission = commission
        super().__init__(name, salarypay)

    def get_pay(self):
        pay = self.salarypay + (self.contracts * self.commission)
        return pay
    
    def __str__(self):
        return self.name + ' works on a monthly salary of ' + str(self.salarypay) + ' and receives a commission for ' + str(self.contracts) + ' contract(s) at ' + str(self.commission) + '/contract.  Their total pay is ' + str(self.get_pay()) + '.'

class HourlyCommissionEmployee(HourlyEmployee):
    def __init__(self, name, hours, rate, contracts, commission):
        self.contracts = contracts
        self.commission = commission
        super().__init__(name, hours, rate)

    def get_pay(self):
        pay = (self.hours * self.rate) + (self.contracts * self.commission)
        return pay

    def __str__(self):
        return self.name + ' works on a contract of ' + str(self.hours) + ' hours at ' + str(self.rate) + '/hour and receives a commission for ' + str(self.contracts) + ' contract(s) at ' + str(self.commission) + '/contract.  Their total pay is ' + str(self.get_pay())  + '.'

class SalaryBonusEmployee(SalaryEmployee):
    def __init__(self, name, salarypay, bonus):
        self.bonus = bonus
        super().__init__(name, salarypay)

    def get_pay(self):
        return super().get_pay() + self.bonus

    def __str__(self):
        return self.name + ' works on a monthly salary of ' + str(self.salarypay) + ' and receives a bonus commission of ' + str(self.bonus) + '.  Their total pay is ' + str(self.get_pay()) + '.'

class HourlyBonusEmployee(HourlyEmployee):
    def __init__(self, name, hours, rate, bonus):
        self.bonus = bonus
        super().__init__(name, hours, rate)

    def get_pay(self):
        return super().get_pay() + self.bonus
    
    def __str__(self):
        return self.name + ' works on a contract of ' + str(self.hours) + ' hours at ' + str(self.rate) + '/hour and receives a bonus commission of ' + str(self.bonus) + '.  Their total pay is ' + str(self.get_pay()) + '.'

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryCommissionEmployee('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyCommissionEmployee('Jan', 150, 25, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryBonusEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyBonusEmployee('Ariel', 120, 30, 600)
