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
            print("either the acount already\
             exists or it is not really an acount")

    def name_in_accounts(self, name):
        for i in self.accounts:
            if name == i.name:
                return True
        return False

    def zip(self, account):
        for key in account.__dict__.keys():
            if key[0:3] == "zip":
                return True
        return False

    def addr(self, account):
        for key in account.__dict__.keys():
            if key[0:4] == "addr":
                return True
        return False

    def account_name_to_indice(self, name):
        i = 0
        for account in self.accounts:
            if account.name == name:
                return i
            i += 1
        return None

    def corrupted(self, account):
        # account attribute start with b
        for key in account.__dict__.keys():
            if key[0] == "b":
                print('cor: attribute start with b')
                return True
        # account has no attribute zip
        if not self.zip(account):
            print('cor: no attribute name zip')
            return True
        # account has no attribute addr
        if not self.addr(account):
            print('cor: no attr name addr')
            return True

        # acount got an even numbe of attr
        if len(account.__dict__) % 2 == 0:
            print("corr: even numbe of attr")
            return True
        # name, id and value not included in acount attr
        if "name" and "id" and "value" not in account.__dict__.keys():
            print("corr: name or vlaue or id dosen't exist")
            return True
        # name is not a string
        if not isinstance(account.__dict__["name"], str):
            print("name isn't str")
            return True
        # id not being an int
        if not isinstance(account.__dict__["id"], int):
            print("id isn't int")
            return True
        # value not being an int or a float
        if not isinstance(account.__dict__["value"], (int, float)):
            print("value isn't int or float")
            return True
        return False

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        indice = self.account_name_to_indice(origin)
        origin = self.accounts[indice]
        if self.corrupted(origin):
            # print("from tran: origin is corrupted")
            return False
        indice = self.account_name_to_indice(dest)
        dest = self.accounts[indice]
        if self.corrupted(dest):
            # print("from tran: dest is corrupted")
            # print("the account you are trying to send money\
            # to is corrupted")
            # sys.exit()
            return False
        elif amount < 0 or amount > origin.value:
            # print("amount is not enough")
            # print("Error: this transaction can't be made")
            # sys.exit()
            return False
        elif dest.name == origin.name:
            # print("sending to same account")
            dest.value += 0
            return True
        else:
            # print("transfer succeded")
            dest.value += amount
            origin.value -= amount
            return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        # account attribute start with b
        indice = self.account_name_to_indice(name)
        lst = []
        for key in self.accounts[indice].__dict__.keys():
            if key[0] == "b":
                lst.append(key)
        for key in lst:
            delattr(self.accounts[indice], key)
        # acount got an even numbe of attr
        if self.name_in_accounts(name) is False:
            return False
        indice = self.account_name_to_indice(name)
        # name, id and value not included in acount attr
        if "value" not in self.accounts[indice].__dict__.keys():
            self.accounts[indice].value = 0
        if "id" not in self.accounts[indice].__dict__.keys():
            self.accounts[indice].id = 0
        # account has no attr zip
        if not self.zip(self.accounts[indice]):
            self.accounts[indice].zip = "chila3ba"
        # account has no attr addr
        if not self.addr(self.accounts[indice]):
            self.accounts[indice].addr = "chila3batani"
        # account have even number of attr
        if len(self.accounts[indice].__dict__) % 2 == 0:
            self.accounts[indice].tmp = "randomstring"
        return True

    def print_bank_acounts(self):
        for acount in self.accounts:
            print("#####################")
            print("acount id:", acount.id)
            print("acount name:", acount.name)
            # print("acount value:", acount.value)
            # print(acount.__dict__)
