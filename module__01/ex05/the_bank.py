import sys

class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")
        
        def transfer(self, amount):
         self.value += amount


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        if isinstance(new_account, Account) and\
         new_account not in self.accounts:
            self.accounts.append(new_account)
        else:
            print("either the acount already exists or it not really an acount")

    def corrupted(self,account):
        # account attribute start with b
        for key in account.__dict__.keys():
            if key[0] == "b":
                return True
            if key[0:3] == "zip" or key[0:4] == "addr":
                return True
        # acount got an even numbe of attr
        if len(account.__dict__) %2 == 0 :
            return True
        # name, id and value not included in acount attr
        if "name" and "id" and "value" not in account.__dict__.keys():
            return True
        # name is not a string
        if not isinstance(account.__dict__["name"],str):
            return True
        # id not being an int
        if not isinstance(account.__dict__["id"], int):
            return True
        # value not being an int or a float
        if not isinstance(account.__dict__["value"],(int, float)):
            return True
        return False
        

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        # if not isinstance(origin, Account):
        #     print("the problem is orig not an acount")
        #     sys.exit()
        # elif not isinstance(dest, Account):
        #     print("the problem is dest not an acount")
        #     sys.exit()
        if origin and dest not in self.accounts:
            # print("Error: you are sending from or into a non existing acount")
            # sys.exit()
            return False
        elif self.corrupted(origin):
            # print("the acount you are trying to send\
            # money from is corrupted")
            # sys.exit()
            return False
        elif self.corrupted(dest):
            # print("the account you are trying to send money\
            # to is corrupted")
            # sys.exit()
            return False
        elif amount < 0 or amount > origin.value:
            # print("Error: this transaction can't be made")
            # sys.exit()
            return False
        elif dest.name == origin.name:
            dest.value += 0
            return True
        else:
            dest.value +=amount
            origin.value -=amount
            return True

    def name_in_accounts(self,name):
        for i in self.accounts:
            if name == i.name:
                return True
        return False
    def account_name_to_indice(self,name):
        i = 0
        for account in self.accounts:
            if account.name == name:
                return i
            i +=1
        return None


    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
         # account attribute start with b
        # for key in account.__dict__.keys():
        #     if key[0] == "b":
        #         return True
        #     if key[0:3] == "zip" or key[0:4] == "addr":
        #         return True
        # acount got an even numbe of attr
        if self.name_in_accounts(name)is False:
            return False
        indice = self.account_name_to_indice(name)
        if len(self.accounts[indice].__dict__) %2 == 0 :
            self.accounts[indice].tmp = "randomstring"
            return True
        # name, id and value not included in acount attr
        if "value" not in self.accounts[indice].__dict__.keys():
            self.accounts[indice].value = 0
            return True
        if "id" not in self.accounts[indice].__dict__.keys():
            self.accounts[indice].value = 0
            return True
        lst = []
        for key in self.accounts[indice].__dict__.keys():
            if key[0:3] == "zip":
                lst.append(key)
                # delattr(self.accounts[indice],key)
            if key[0:4] == "addr":
                lst.append(key)
        for attri in lst:
            print("this is attri @@@@@@@@@@@@@@@@@@", attri)
            print("the acount name is ", self.accounts[indice].name)
            print("the acount attribute are",self.accounts[indice].__dir__())
            print(self.accounts[indice].zip)
            delattr(self.accounts[indice],'zip')
        return True
    
    def print_bank_acounts(self):
        for acount in self.accounts:
            print("#####################")
            # print("acount id:", acount.id)
            # print("acount name:",acount.name)
            # print("acount value:", acount.value)
            print(acount.__dict__)