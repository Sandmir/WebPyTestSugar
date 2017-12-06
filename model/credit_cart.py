class CreditCart:
    def __init__(self, owner, number, month, year, cvv, type):
        self.owner = owner
        self.number = number
        self.month = month
        self.year = year
        self.cvv = cvv
        self.type = type


class VisaCart:
    def __init__(self, owner='Tom Tom', number='4242424242424242', month='08', year='2018', cvv='123', type='VISA'):
        self.owner = owner
        self.number = number
        self.month = month
        self.year = year
        self.cvv = cvv
        self.type = type


class Mastercard:
    def __init__(self, owner='Tom Tom', number='5555555555554444', month='08', year='2018', cvv='123'
                 , type='Mastercard'):
        self.owner = owner
        self.number = number
        self.month = month
        self.year = year
        self.cvv = cvv
        self.type = type


class MastercardDebit:
    def __init__(self, owner='Tom Tom', number='5200828282828210', month='08', year='2018', cvv='123'
                 , type='MastercardDebit'):
        self.owner = owner
        self.number = number
        self.month = month
        self.year = year
        self.cvv = cvv
        self.type = type


class AmericanExpress:
    def __init__(self, owner='Tom Tom', number='378282246310005', month='08', year='2018', cvv='1234'
                 , type='AmericanExpress'):
        self.owner = owner
        self.number = number
        self.month = month
        self.year = year
        self.cvv = cvv
        self.type = type


class Discover:
    def __init__(self, owner='Tom Tom', number='6011111111111117', month='08', year='2018', cvv='123'
                 , type='Discover'):
        self.owner = owner
        self.number = number
        self.month = month
        self.year = year
        self.cvv = cvv
        self.type = type


class DinersClub:
    def __init__(self, owner='Tom Tom', number='30569309025904', month='08', year='2018', cvv='123'
                 , type='DinersClub'):
        self.owner = owner
        self.number = number
        self.month = month
        self.year = year
        self.cvv = cvv
        self.type = type


class JCB:
    def __init__(self, owner='Tom Tom', number='3530111333300000', month='08', year='2018', cvv='123'
                 , type='JCB'):
        self.owner = owner
        self.number = number
        self.month = month
        self.year = year
        self.cvv = cvv
        self.type = type
