username = ["Username"]
password = ["Password"]
x = 'y'
total = 0
payment = 0
order = ""
all =""
foodprice = [115 , 99 , 89 , 90]
dessertprice = [70 , 75 , 90 , 60]
drinkprice  = [20 , 20 , 30 , 30]
foodchoice = ["Spaghetti with Fried Chicken",
              "1pc. Chicken with Rice" ,
              "Shanghai with Egg and Rice",
              "Burgersteak with fries and Rice"]
dessertchoice = ["Buko salad" , "Buko pandan" , "Fruit salad" , "Mango float"]
drinkchoice = ["Coke" , "Royal" , "Pineapple Juice" , "Ice Tea"]
totalall = []
while x == 'y' or x == 'Y':
    welcome = input("=====================================================\n"
                    "Welcome to Console Based\n"
                    "Point of Sale System\n"
                    "[1] For Login.\n"
                    "[2] For Register.\n"
                    "[3] For Exit.\n"
                    "[4] For Information of this System.")

    if welcome == '1':
        uname = input("Insert Cashier Username: ")
        pword = input("Insert Cashier Password: ")
        if uname in username and pword in password:
            z = 'y'
            while z == 'y' or z == "Y" or z == "Yes":
                print("================================================================"
                  "\nWelcome to Point of Sale System"
                  "\nThis is Console Base(Pos)"
                  "\nCashier Name:", uname)
                pos = input("pls Choose an item."
                            "\n [1] For Food."
                            "\n [2] For Dessert."
                            "\n [3] For Drinks."
                            "\n [4] For Cancel Item."
                            "\n [5] For Exit System.\n")
                if pos == '1':
                    food = input("Pls Choose a Category:"
                                 "\n    Item Name                            Price"
                                 "\n[1] Spaghetti with Fried Chicken          115"
                                 "\n[2] 1pc. Chicken with Rice                99"
                                 "\n[3] Shanghai with Egg and Rice            89"
                                 "\n[4] Burgersteak with fries and Rice       90\n")
                    if food == '1':
                        print("How many " + foodchoice[0] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = foodprice[0] * quant
                        totalall.append(total)
                        all += "\n" + foodchoice[0] + "\t\t\t" + str(foodprice[0]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + foodchoice[0] + "\t\t\t" + str(foodprice[0]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '2':
                        print("How many " + foodchoice[1] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = foodprice[1] * quant
                        totalall.append(total)
                        all += "\n" + foodchoice[1] + "\t\t\t\t\t" + str(foodprice[1]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + foodchoice[1] + "\t\t\t\t\t" + str(foodprice[1]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '3':
                        print("How many " + foodchoice[2] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = foodprice[2] * quant
                        totalall.append(total)
                        all += "\n" + foodchoice[2] + "\t\t\t\t" + str(foodprice[2]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + foodchoice[2] + "\t\t\t\t" + str(foodprice[2]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '4':
                        print("How many " + foodchoice[3] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = foodprice[3] * quant
                        totalall.append(total)
                        all += "\n" + foodchoice[3] + "\t\t\t" + str(foodprice[3]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + foodchoice[3] + "\t\t\t" + str(foodprice[3]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")

                if z == "n" or z == "N":
                    try:
                        payment = int(input("Insert payment: "))
                    except ValueError as error:
                        print("Invalid Input")
                        print("Pls Input Valid Option.")
                        print("Error: ", error)
                        z = "y"
                        continue
                    alltotal = sum(totalall)
                    if payment >= alltotal:
                        alltotal = sum(totalall)
                        change = payment - alltotal
                        print("\n----------------------------------------------------------------")
                        print("\n------------------------Total-Receipt---------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal" + "\n")
                        print(all)
                        print("----------------------------------------------------------------")
                        print("Total\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) +
                              "\nCash\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(payment) +
                              "\nChange\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(change) +
                              "\n----------------------------------------------------------------"
                              "\n-----------------------Thank-You-Come-Again---------------------\n\n")
                        z = "Y"
                        all = ""
                        order = ""
                        total = 0
                        totalall.clear()
                    else:
                        alltotal = sum(totalall)
                        while payment<alltotal:
                            print("Not Enough Money. Pls Enter cash again:")
                            try:
                                payment = int(input("Insert payment: "))
                            except ValueError as error:
                                print("Invalid Input")
                                print("Pls Input Valid Option.")
                                print("Error: ", error)
                                z = "y"
                                continue
                            change = payment - alltotal
                            print("\n----------------------------------------------------------------")
                            print("\n------------------------Total-Receipt---------------------------")
                            print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal" + "\n")
                            print(all)
                            print("----------------------------------------------------------------")
                            print("Total\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) +
                                  "\nCash\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(payment) +
                                  "\nChange\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(change) +
                                  "\n----------------------------------------------------------------"
                                  "\n-----------------------Thank-You-Come-Again---------------------\n\n")
                            z = "Y"
                            all = ""
                            order = ""
                            total = 0
                            totalall.clear()
                elif pos == '2':
                    food = input("Pls Choose a Category:"
                                     "\n    Item Name                            Price"
                                     "\n[1] Buko salad                           70"
                                     "\n[2] Buko pandan                          75"
                                     "\n[3] Fruit salad                          90"
                                     "\n[4] Mango float                          60\n")
                    if food == '1':
                        print("How many " + dessertchoice[0] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total += dessertprice[0] * quant
                        totalall.append(total)
                        all += "\n" + dessertchoice[0] + "\t\t\t\t\t\t\t\t" + str(dessertprice[0]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + dessertchoice[0] + "\t\t\t\t\t\t\t\t" + str(dessertprice[0]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '2':
                        print("How many " + dessertchoice[1] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = dessertprice[1] * quant
                        totalall.append(total)
                        all += "\n" + dessertchoice[1] + "\t\t\t\t\t\t\t\t" + str(dessertprice[1]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + dessertchoice[1] + "\t\t\t\t\t\t\t\t" + str(dessertprice[1]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '3':
                        print("How many " + dessertchoice[2] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = dessertprice[2] * quant
                        totalall.append(total)
                        all += "\n" + dessertchoice[2] + "\t\t\t\t\t\t\t\t" + str(dessertprice[2]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + dessertchoice[2] + "\t\t\t\t\t\t\t\t" + str(dessertprice[2]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '4':
                        print("How many " + dessertchoice[3] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = dessertprice[3] * quant
                        totalall.append(total)
                        all += "\n" + dessertchoice[3] + "\t\t\t\t\t\t\t\t" + str(dessertprice[3]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + dessertchoice[3] + "\t\t\t\t\t\t\t\t" + str(dessertprice[3]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        total = int(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                if z == "n" or z == "N":
                    try:
                        payment = int(input("Insert payment: "))
                    except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                    alltotal = sum(totalall)
                    if payment >= alltotal:
                        alltotal = sum(totalall)
                        change = payment - alltotal
                        print("\n----------------------------------------------------------------")
                        print("\n------------------------Total-Receipt---------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal" + "\n")
                        print(all)
                        print("----------------------------------------------------------------")
                        print("Total\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) +
                              "\nCash\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(payment) +
                              "\nChange\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(change) +
                              "\n----------------------------------------------------------------"
                              "\n-----------------------Thank-You-Come-Again---------------------\n\n")
                        z = "Y"
                        all = ""
                        order = ""
                        total = 0
                        totalall.clear()
                    else:
                        alltotal = sum(totalall)
                        while payment < alltotal:
                            print("Not Enough Money. Pls Enter cash again:")
                            try:
                                payment = int(input("Insert payment: "))
                            except ValueError as error:
                                print("Invalid Input")
                                print("Pls Input Valid Option.")
                                print("Error: ", error)
                                z = "y"
                                continue
                            change = payment - alltotal
                            print("\n----------------------------------------------------------------")
                            print("\n------------------------Total-Receipt---------------------------")
                            print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal" + "\n")
                            print(all)
                            print("----------------------------------------------------------------")
                            print("Total\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) +
                                  "\nCash\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(payment) +
                                  "\nChange\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(change) +
                                  "\n----------------------------------------------------------------"
                                  "\n-----------------------Thank-You-Come-Again---------------------\n\n")
                            z = "Y"
                            all = ""
                            order = ""
                            total = 0
                            totalall.clear()
                elif pos == '3':
                    food = input("Pls Choose a Category:"
                                     "\n    Item Name                      Price"
                                     "\n[1] Coke                           20"
                                     "\n[2] Royal                          20"
                                     "\n[3] Pineapple Juice                30"
                                     "\n[4] Ice Tea                        30\n")
                    if food == '1':
                        print("How many " + drinkchoice[0] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = dessertprice[0] * quant
                        totalall.append(total)
                        all += "\n" + drinkchoice[0] + "\t\t\t\t\t\t\t\t\t" + str(drinkprice[0]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + drinkchoice[0] + "\t\t\t\t\t\t\t\t\t" + str(drinkprice[0]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '2':
                        print("How many " + drinkchoice[1] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = drinkprice[1] * quant
                        totalall.append(total)
                        all += "\n" + drinkchoice[1] + "\t\t\t\t\t\t\t\t\t" + str(drinkprice[1]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + drinkchoice[1] + "\t\t\t\t\t\t\t\t\t" + str(drinkprice[1]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?""\n [Y] or [y] Yor Yes: ""\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '3':
                        print("How many " + drinkchoice[2] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = drinkprice[2] * quant
                        totalall.append(total)
                        all += "\n" + drinkchoice[2] + "\t\t\t\t\t\t\t" + str(drinkprice[2]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + drinkchoice[2] + "\t\t\t\t\t\t\t" + str(drinkprice[2]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?\n [Y] or [y] Yor Yes:\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                    elif food == '4':
                        print("How many " + drinkchoice[3] + " whould you like to order: ")
                        try:
                            quant = int(input("Insert number of item: "))
                        except ValueError as error:
                            print("Invalid Input")
                            print("Pls Input Valid Option.")
                            print("Error: ", error)
                            z = "y"
                            continue
                        total = drinkprice[3] * quant
                        totalall.append(total)
                        all += "\n" + drinkchoice[3] + "\t\t\t\t\t\t\t\t\t" + str(drinkprice[3]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        order += "\n" + drinkchoice[3] + "\t\t\t\t\t\t\t\t\t" + str(drinkprice[3]) + "\t\t" + str(quant) + "\t\t" + str(total)
                        z = input("Whold you Like to Continue.?"
                                  "\n [Y] or [y] Yor Yes: "
                                  "\n [N] or [n] For No: \n")
                        alltotal = sum(totalall)
                        print("\n----------------------------------------------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal\n" + all +
                              "\n----------------------------------------------------------------"
                              "\nTotal\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) + "\n\n1")
                if z == "n" or z == "N":
                    try:
                        payment = int(input("Insert payment: "))
                    except ValueError as error:
                        print("Invalid Input")
                        print("Pls Input Valid Option.")
                        print("Error: ", error)
                        z = "y"
                        continue
                    alltotal = sum(totalall)
                    if payment >= alltotal:
                        change = payment - alltotal
                        print("\n----------------------------------------------------------------")
                        print("\n------------------------Total-Receipt---------------------------")
                        print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal" + "\n")
                        print(all)
                        print("----------------------------------------------------------------")
                        print("Total\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) +
                              "\nCash\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(payment) +
                              "\nChange\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(change) +
                              "\n----------------------------------------------------------------"
                              "\n-----------------------Thank-You-Come-Again---------------------\n\n")
                        z = "Y"
                        all = ""
                        order = ""
                        total = 0
                        totalall.clear()
                    else:
                        alltotal = sum(totalall)
                        while payment < alltotal:
                            print("Not Enough Money. Pls Enter cash again:")
                            try:
                                payment = int(input("Insert Payment"))
                            except ValueError as error:
                                print("Invalid Input")
                                print("Pls Input Valid Option.")
                                print("Error: ", error)
                                z = "y"
                                continue
                            alltotal = sum(totalall)
                            change = payment - alltotal
                            print("\n----------------------------------------------------------------")
                            print("\n------------------------Total-Receipt---------------------------")
                            print("Order\t\t\t\t\t\t\t\t\tPrice\tQnty\tTotal" + "\n")
                            print(all)
                            print("----------------------------------------------------------------")
                            print("Total\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(alltotal) +
                                  "\nCash\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(payment) +
                                  "\nChange\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(change) +
                                  "\n----------------------------------------------------------------"
                                  "\n-----------------------Thank-You-Come-Again---------------------\n\n")
                            z = "Y"
                            all = ""
                            order = ""
                            total = 0
                            totalall.clear()
                elif pos == '4':
                    print("Item Cleared.")
                    z = "Y"
                    all = ""
                    order = ""
                    total = 0
                    totalall.clear()
                elif pos == '5':
                    print("Exiting System")
                    exit()

        else:
            print("Invalid input")
    elif welcome == '2':
        print("Welcome to register form.\n"
              "Pls fill up the form: ")
        cuname = input("Create Username: ")
        cpassword1 = input("Enter Password: ")
        cpassword2 = input("Re-enter Password: ")
        if cpassword1 == cpassword2:
            username.append(cuname)
            password.append(cpassword1)
            print("Cashier Account Has Been Created")
            x = 'y'
        else:
            print("Invalid Input.")
    elif welcome == '3':
        print("Exiting System!")
        exit()
    elif welcome == '4':
        print("This System Features")
        print("Log in, \n"
              "Register, \n"
              "Customer Choose /view the list of product, \n"
              "Customer order confirmation , \n"
              "Add more product, \n"
              "Change computation, \n"
              "Cancellable order/selected product, \n"
              "If incorrect input, will ask another input, until it satisfies  with the correct one.\n")
        x = "y"