class BankAccount:
    def __init__(self ,account_number ,account_holder ):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if self.balance >= amount :
            self.balance -= amount
            
    def get_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    
    def __init__(self,account_number, account_holder, interest_rate):
            super().__init__(account_number, account_holder)
            self.interest_rate = interest_rate
            
    def apply_interrest(self):
        interest_amount = self.balance *self.interest_rate
        self.balance += interest_amount
        
    def print(self):
        print(f'current balance: ${self.balance}, interest rate: {self.interest_rate}')
        
bank_acc=BankAccount('9638522741','Reem Alali')
bank_acc.deposit(1000)
print(f'balance after deposit: $ {bank_acc.get_balance()}')
bank_acc.withdraw(500)
print(f'Balance after withdraw: $ {bank_acc.get_balance()}')
savings_acc = SavingsAccount('123456789', 'Nabel', 0.05)
savings_acc.deposit(2000)
savings_acc.apply_interrest()
savings_acc.print()