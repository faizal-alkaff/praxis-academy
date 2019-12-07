class Deposit:
    def __init__(self):
        self.deposit = deposit
    
    def setDeposit(self):
        self.deposit = int(input("\n\t\tEnter the amount of money to deposit : "))
        
    def getDeposit(self):
        BalanceInquiry.balance = BalanceInquiry.balance + self.deposit
        print('\t\tDeposit Success', self.deposit)
        
class Withdraw:
    def __init__(self):
        self.withdraw = withdraw
    
    def setWithdraw(self):
        if BalanceInquiry.balance == 0:
            print("\t\tYour current balance is zero.")
            print("\t\tYou cannot withdraw!")
            print("\t\tYou need to deposit money first.")
        elif BalanceInquiry.balance <= 500:
            print("\t\tYou do not have sufficient money to withdraw")
            print("\t\tChecked your balance to see your money in the bank.")
        else:
            self.withdraw = int(input("\n\t\tEnter amount of money to withdraw : "))
            if BalanceInquiry.balance < self.withdraw:
                print("\t\tThe amount you withdraw is greater than to your balance")
                print("\t\tPlease check the amount you entered.")
            else:
                Withdraw.getWithdraw(self)

    def getWithdraw(self):
        BalanceInquiry.balance = BalanceInquiry.balance - self.withdraw
        print('\t\tWithdraw Success', self.withdraw)
        
class BalanceInquiry():
    def __init__(self):
        self.balance = balance
    
    def setBalance(self, b):
        self.balance = b
        
    def getBalance(self):
        print('\t\tYour current balance is', self.balance)

class ATMMachine(Deposit, Withdraw, BalanceInquiry):

    def __init__(self,select=0,choice=1):
        self.select = select
        self.choice = choice
        Deposit.deposit = 0
        Withdraw.withdraw = 0
        BalanceInquiry.balance = 0
        
        print("================================================================")
        print("\t\tWelcome to this simple ATM machine")
        print("================================================================")
        print()
        print("\t\tPlease select ATM Transactions");
        print("\t\tPress [1] Deposit");
        print("\t\tPress [2] Withdraw");
        print("\t\tPress [3] Balance Inquiry");
        print("\t\tPress [4] Exit");
        
        while choice == 1:
            select = int(input("\n\t\tWhat would you like to do ? "))
            if select > 4:
                print("\n\t\tPlease select correct transaction.")
            elif select == 1:
                Deposit.setDeposit(self)
                Deposit.getDeposit(self)
            
            elif select == 2:
                Withdraw.setWithdraw(self)
                
            elif select == 3:
                BalanceInquiry.getBalance(self)
                
            elif select == 4:
                break
            
            print("\n\t\tWould you like to try another transaction ? ")
            print("\t\tPress [1] Yes \n\t\tPress [2] No")
            choice = int(input("\t\tEnter choice: "))

        print("\n\t\tThank you for using this simple ATM Machine.")
mech_A=ATMMachine()
