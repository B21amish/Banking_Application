dict = {}
sample = "abc"

# using nested dictionaries
def bank(str):
    x = str.split()
    AccNum = x[1]
    if len(x) == 3:
        # for create query
        if x[0] == "CREATE":
            dict[AccNum] = {}
            dict[AccNum]["name"] = x[2]
            dict[AccNum]["balance"] = 0
            return dict
        # for deposit query
        if x[0] == "DEPOSIT":
            amount = x[2]
            Ex_Balance = dict[AccNum]["balance"]
            dict[AccNum]["balance"] = Ex_Balance + int(amount)
            return dict
        # for withdraw query
        if x[0] == "WITHDRAW":
            amount = x[2]
            Ex_Balance = dict[AccNum]["balance"]
            dict[AccNum]["balance"] = Ex_Balance - int(amount)
            return dict
    if len(x) == 2:
        # for balance query
        if x[0] == "BALANCE":
            acc_name = dict[AccNum]["name"]
            acc_balance = dict[AccNum]["balance"]
            print(acc_name, " ", acc_balance)

# while loop to take input
while sample != "exit":
    bank_input = input()
    if bank_input == "exit":
        break
    bank(bank_input)