class Bank:
    def __init__(self):
        self.customers = {}
    
    def create_account(self, acc_no, init_bal):
        if acc_no not in self.customers:
            self.customers[acc_no] = init_bal
            return f"Account {acc_no} created successfully with an initial balance of Rs{init_bal}"
        else:
            return "Error"
     
    def bal(self, acc_no):
        if acc_no in self.customers:
            return f"The balance for account {acc_no} is Rs{self.customers[acc_no]}"
        else:
            return "Error"
    
    def dep(self, acc_no, amount):
        if acc_no in self.customers:
            self.customers[acc_no] += amount
            return f"Rs{amount} deposited successfully to account {acc_no}, new balance is Rs{self.customers[acc_no]}"
        else:
            return "Error"
        
    def wd(self, acc_no, amount):
        if acc_no in self.customers:
            if self.customers[acc_no] >= amount:
                self.customers[acc_no] -= amount
                return f"Rs{amount} withdrawn successfully from account {acc_no}, new balance is Rs{self.customers[acc_no]}"
            else:
                return "Error"
        else:
            return "Error"
        
    def close(self, acc_no):
        if acc_no in self.customers:
            del self.customers[acc_no]
            return f"Account {acc_no} closed"
        else:
            return "Error"
        
bnk = Bank()
print(bnk.create_account("18809",1000))
print(bnk.create_account("18009",800))

print(bnk.dep("18809",3000))
print(bnk.wd("18009",500))

print(bnk.bal("18809"))


