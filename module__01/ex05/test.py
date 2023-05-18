from the_bank import Account
from the_bank import Bank

first_acount = Account("first_acount", value = 10)
second_acount = Account("second_name", value = 5)
bank = Bank()
bank.add(first_acount)
bank.add(second_acount)
# print(first_acount.value)
# print(first_acount.name)
bank.print_bank_acounts()
bank.transfer(first_acount,second_acount,2)
print("##############after transfer***********")
bank.print_bank_acounts()

