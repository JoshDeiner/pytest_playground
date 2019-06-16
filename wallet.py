''' making wallet  '''


class Wallet:
    ''' implementing wallet class  '''
    def __init__(self, deposits=0, initial_amount=0, deposit_list=list()):
        self.deposit_list = deposit_list
        self.balance = initial_amount + deposits
        self.initial_amount = initial_amount

    def __str__(self):
        return f"Wallet => balance: {self.balance}"

    def spend_cash(self, amount):
        ''' amount of cash spent '''
        self.balance -= amount

    def add_cash(self, amount):
        ''' adding to account '''
        self.balance += amount
        self.deposit_list.append(amount)

    def close(self):
        ''' fake logout sequence  '''
        return f"remaining balance in account is {self.balance}"
