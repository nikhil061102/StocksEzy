print("""=====================================================
         \tSTOCKSEZY - STOCKS MANAGEMENT PROGRAM

Made by : Nikhil Rastogi
          Roll No. 2021MCB1240
          IIT Ropar
          Mathematics & Computing Branch
""")

import datetime
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

#OPENING MYSQL & CREATING REQUIRED DATABASE & TABLES IF NOT PRESENT 

psw = input('Enter the password to your server : ')
while True:
    try:
        db = mysql.connector.connect(host= "localhost",\
                             user = "root",\
                             passwd = psw)
        break
    except mysql.connector.Error as err:
        print("Wrong Password entered !!")
        psw = input('Enter the password to your server : ')

cur =db.cursor()

cur.execute('create database if not exists stocks')

db = mysql.connector.connect(host= "localhost",\
                             user = "root",\
                             passwd = psw,\
                             database = "stocks")
cur =db.cursor()

cur.execute('create table if not exists buy(DOP date, StockName varchar(40), BuyPrice decimal(10,2), NoBought int(11), Brokerage decimal(10,2))')
cur.execute('create table if not exists sell(DOS date, StockName varchar(40), SellPrice decimal(10,2), NoSold int(11), Brokerage decimal(10,2))')
cur.execute('create table if not exists net(Name varchar(40), DOT date, Net decimal(10,2))')
cur.execute('create table if not exists t_net(DATE date, net decimal(10,2))')


def locate_datapoint():  #for intaking data and outputing list of data for locating a particular data 
    org_name = input("\nINPUT THE NAME OF STOCK TO BE CHANGED: ").upper()
    org_price = float(input("\nINPUT THE PRICE OF STOCK TO BE CHANGED: "))
    org_no = int(input("\nINPUT THE NO. OF STOCK TO BE CHANGED: "))
    org_broke = float(input("\nINPUT THE BROKERAGE OF STOCK TO BE CHANGED: "))

    return [org_name,org_price,org_no,org_broke]
    
ans_start = "n"
while ans_start in ("n","N"):
    cur.execute("set autocommit = 1")    

    print("""
=====================================================
Main Menu:
\t1. BOUGHT STOCKS
\t2. SOLD STOCKS
\t3. MODIFY DATA
\t4. DELETE DATA
\t5. SHOW DAILY PROFIT/LOSS\n""")
    print("=====================================================")
    ans_main_menu = input("What do you want to do? : ")
    
    while ans_main_menu not in ("1","2","3","4","5") :
        print("Invalid Input!")
        print("Valid Inputs are 1,2,3,4,5\n")
        ans_main_menu = input("Give your input again : ")
    else:

        #BUYING STOCKS

        if ans_main_menu == "1":
            def buying ():
                b_name = input("\nName of Stock Bought: ").upper()
                b_date =  datetime.date.today()

                state_buyprice = "\nBuying Price: "
                while True:
                    try:
                        b_price = float(input(state_buypriceprice))
                        if type(b_price) != float:
                            raise ValueError
                        break
                    except ValueError:
                        state_buypriceprice = """\nWrong Entry!!
Give correct buying price: """

                state_buyno = "\nNo. of stocks bought: "
                while True:
                    try:
                        b_no = int(input(state_buyno))
                        if type(b_no) != int:
                            raise ValueError
                        break
                    except ValueError:
                        state_buyno = """\nWrong Entry!!
Give correct no. of stocks bought: """

                state_buybroke = "\nBrokerage in percent: "
                while True:
                    try:
                        b_broke = float(input(state_buybroke))
                        if type(b_broke) != float or b_broke > 100:
                            raise ValueError
                        break
                    except ValueError:
                        state_buybroke = """\nWrong Entry!!
Give correct brokerage in percent: """
                    
                sql_buy = "INSERT INTO buy(DOP,StockName,BuyPrice,NoBought,Brokerage) values(%s,%s,%s,%s,%s)"
                val_buy = (b_date,b_name,b_price,b_no,b_broke)
                cur.execute(sql_buy,val_buy)
                print("\nRecorded successful!")

            buying()
            
            #RERUNNING 'BUYING' CODE BLOCK

            ans_re_buy = input("\nDo you want to do again: ")
            while ans_re_buy not in ("n","N","y","Y"):
                    print("\nInvalid Input!")
                    print("Valid Inputs are n, N, y or Y")
                    ans_re_buy = input("Give your input again : ")
            else:
                    while ans_re_buy in ("y","Y"):
                        buying()
                        
                        ans_re_buy = input("\nDo you want to do again: ")
                        while ans_re_buy not in ("n","N","y","Y"):
                            print("\nInvalid Input!")
                            print("Valid Inputs are n, N, y or Y")
                            ans_re_buy = input("Give your input again : ")

        #SELLING STOCKS

        elif ans_main_menu == "2":

            def selling():
                s_name = input("\nName of Stock Sold: ").upper()
                s_date =  datetime.date.today()

                state_sellprice = "\nSelling Price: "
                while True:
                    try:
                        s_price = float(input(state_sellprice))
                        if type(s_price) != float:
                            raise ValueError
                        break
                    except ValueError:
                        state_sellprice = """\nWrong Entry!!
Give correct selling price: """

                state_sellno = "\nNo. of stocks sold: "
                while True:
                    try:
                        s_no = int(input(state_sellno))
                        if type(s_no) != int:
                           raise ValueError
                        break
                    except ValueError:
                        state_sellno = """\nWrong Entry!!
Give correct no. of stocks sold: """

                state_sellbroke = "\nBrokerage in percent: : "
                while True:
                    try:
                        s_broke = float(input(state_sellbroke))
                        if type(s_broke) != float or s_broke > 100:
                            raise ValueError
                        break
                    except ValueError:
                        state_sellbroke = """\nWrong Entry!!
Give correct brokerage given in percent: """
            
                sql_sell = "INSERT INTO sell(DOS,StockName,SellPrice,NoSold,Brokerage) values(%s,%s,%s,%s,%s)"
                val_sell = (s_date,s_name,s_price,s_no,s_broke)
                cur.execute(sql_sell,val_sell)
                print("\nRecored successful!")

            selling()    

            #RERUNNING 'SELLING' CODE BLOCK  
            
            ans_re_sell= input("\nDo you want to do again: ")
            while ans_re_sellnot in ("n","N","y","Y"):
                    print("Invalid Input!")
                    print("Valid Inputs are n, N, y or Y")
                    ans_re_sell= input("Give your input again : ")
            else:
                    while ans_re_sellin ("y","Y"):
                        selling()

                        ans_re_sell= input("\nDo you want to do again: ")
                        while ans_re_sellnot in ("n","N","y","Y"):
                            print("\nInvalid Input!")
                            print("Valid Inputs are n, N, y or Y")
                            ans_re_sell= input("Give your input again : ")

        #MODIFY THE RECORDED DATA

        elif ans_main_menu == "3":
            print("""\n1. MAKE CHANGES IN BUYING TABLE
2. MAKE CHANGES IN SELLING TABLE""")
            ans_change = input("\nWhat do you want to do?: ")
            while ans_change not in ("1","2"):
                print("\nInvalid Input!")
                print("Valid Inputs are 1 or 2")
                ans_change = input("Give your input again : ")

            if ans_change == "1":
                print("""1. CHANGE NAME OF STOCK
2. CHANGE BUY PRICE
3. CHANGE NO. OF STOCKS BOUGHT
4. CHANGE BROKERAGE""")
                ans_change_buy = input("\nWhat do you want to do?: ")
                while ans_change_buy not in ("1","2","3","4"):
                        print("\nInvalid Input!")
                        print("Valid Inputs are 1, 2, 3 or 4")
                        ans_change_buy = input("Give your input again : ")

                if ans_change_buy == "1":
                    
                    lst = locate_datapoint()
                    n_buyname = input("New Name of stock: ").upper()
                    lst.insert(0, n_buyname)
                    new_buy = tuple(lst)
                    
                    update_buy_name = "UPDATE buy set StockName = %s WHERE StockName = %s AND BuyPrice = %s AND NoBought = %s AND Brokerage = %s"
                    cur.execute(update_buy_name,new_buy)
                    print("\nChanges done successfully")
                    
                elif ans_change_buy == "2":
                    
                    lst = locate_datapoint()
                    
                    edit_buyprice = "\nNew buying price: "
                    while True:
                        try:
                            n_buyprice = float(input(edit_buyprice))
                            if type(n_buyprice) != float:
                                raise ValueError
                            break
                        except ValueError:
                            edit_buyprice = """\nWrong Entry!!
Give correct new buying price: """

                    lst.insert(0, n_buyprice)
                    new_buyprice = tuple(lst)
                    
                    update_buy_price = "UPDATE buy set BuyPrice = %s WHERE StockName = %s AND BuyPrice = %s AND NoBought = %s AND Brokerage = %s"

                    cur.execute(update_buy_price,new_buyprice)
                    print("\nChanges done successfully")

                elif ans_change_buy == "3":

                    lst = locate_datapoint()
                    
                    edit_buyno = "\nNew no. of stocks bought: "
                    while True:
                        try:
                            n_buyno = int(input(edit_buyno))
                            if type(n_buyno) != int:
                                raise ValueError
                            break
                        except ValueError:
                            edit_buyno = """\nWrong Entry!!
Give correct no. of stocks bought: """
                            
                    lst.insert(0, n_buyno)
                    new_buyno = tuple(lst)
                    
                    update_buy_no = "UPDATE buy set NoBought = %s WHERE StockName = %s AND BuyPrice = %s AND NoBought = %s AND Brokerage = %s"

                    cur.execute(update_buy_no,new_buyno)
                    print("\nChanges done successfully")

                else:
                    lst = locate_datapoint()

                    edit_buybroke = "\nNew brokerage: "
                    while True:
                        try:
                            n_buybroke = int(input(edit_buybroke))
                            if type(n_buybroke) != float or nbroke1 > 100:
                                raise ValueError
                            break
                        except ValueError:
                            edit_buybroke = """\nWrong Entry!!
Give correct new brokerage: """
                            
                    lst.insert(0, n_buybroke)
                    new_buybroke = tuple(lst)
                    
                    update_buy_broke = "UPDATE buy set NoBought = %s WHERE StockName = %s AND BuyPrice = %s AND NoBought = %s AND Brokerage = %s"
    
                    cur.execute(update_buy_broke,new_buybroke)
                    print("\nChanges done successfully")
            
            if ans_change == "2":
                print("""1. CHANGE NAME OF STOCK
2. CHANGE SELL PRICE
3. CHANGE NO. OF STOCKS SOLD
4. CHANGE BROKERAGE""")
                ans_change_sell = input("\nWhat do you want to do?: ")
                while ans_change_sell not in ("1","2","3","4"):
                    print("\nInvalid Input!")
                    print("Valid Inputs are 1, 2, 3 or 4")
                    ans_change_sell = input("Give your input again : ")
                            
                if ans_change_sell == "1":
                        
                    lst = locate_datapoint()
                    n_sellname = input("New Name of stock: ").upper()
                    lst.insert(0, n_sellname)
                    new_sell = tuple(lst)
                    
                    update_sell_name = "UPDATE sell set StockName = %s WHERE StockName = %s AND SellPrice = %s AND NoSold = %s AND Brokerage = %s"
                    cur.execute(update_sell_name,new_sell)
                    print("\nChanges done successfully")

                
                elif ans_change_sell == "2":
                    
                    lst = locate_datapoint()
                    
                    edit_sellprice = "\nNew selling price: "
                    while True:
                        try:
                            n_sellprice = float(input(edit_sellprice))
                            if type(n_sellprice) != float:
                                raise ValueError
                            break
                        except ValueError:
                            edit_sellprice = """\nWrong Entry!!
Give correct new selling price: """

                    lst.insert(0, n_sellprice)
                    new_sellprice = tuple(lst)
                    
                    update_sell_price = "UPDATE sell set SellPrice = %s WHERE StockName = %s AND SellPrice = %s AND NoSold = %s AND Brokerage = %s"

                    cur.execute(update_sell_price,new_sellprice)
                    print("\nChanges done successfully")

                elif ans_change_sell == "3":

                    lst = locate_datapoint()
                    
                    edit_sellno = "\nNew no. of stocks sold: "
                    while True:
                        try:
                            n_sellno = int(input(edit_sellno))
                            if type(n_sellno) != int:
                                raise ValueError
                            break
                        except ValueError:
                            edit_sellno = """\nWrong Entry!!
Give correct no. of stocks sold: """
                            
                    lst.insert(0, n_sellno)
                    new_sellno = tuple(lst)
                    
                    update_sell_no = "UPDATE sell set NoSold = %s WHERE StockName = %s AND SellPrice = %s AND NoSold = %s AND Brokerage = %s"

                    cur.execute(update_sell_no,new_sellno)
                    print("\nChanges done successfully")

                else:
                    lst = locate_datapoint()

                    edit_sellbroke = "\nNew brokerage: "
                    while True:
                        try:
                            n_sellbroke = int(input(edit_sellbroke))
                            if type(n_sellbroke) != float or nbroke1 > 100:
                                raise ValueError
                            break
                        except ValueError:
                            edit_sellbroke = """\nWrong Entry!!
Give correct new brokerage: """
                            
                    lst.insert(0, n_sellbroke)
                    new_sellbroke = tuple(lst)
                    
                    update_sell_broke = "UPDATE sell set NoSold = %s WHERE StockName = %s AND SellPrice = %s AND NoSold = %s AND Brokerage = %s"
    
                    cur.execute(update_sell_broke,new_sellbroke)
                    print("\nChanges done successfully")
                        
        #DELETE THE RECORDED DATA

        elif ans_main_menu == "4":
            print("""1. DELETE FROM BUYING TABLE
2. DELETE FROM SELLING TABLE""")
            ans_del = input("\nWhat do you want to do?: ")
            while ans_del not in ("1","2"):
                print("\nInvalid Input!")
                print("Valid Inputs are 1 or 2")
                ans_del = input("Give your input again : ")

            if ans_del == "1":
                buyname = input("INPUT THE NAME WHOSE RECORD HAS TO BE DELETED: ").upper()
                del_buyname = (buyname,)
                del_buy = "DELETE FROM buy WHERE StockName = %s"
                cur.execute(del_buy,del_buyname)
                print("\nChanges done successfully")

            else:
                sellname = input("\nINPUT THE NAME WHOSE RECORD HAS TO BE DELETED: ").upper()
                del_sellname = (sellname,)
                del_sell = "DELETE FROM sell WHERE StockName = %s"
                cur.execute(del_sell,del_sellname)
                print("\nChanges done successfully")
                
        #SHOW PROFIT/LOSS IN FORM OF GRAPH FROM INPUT DATA        
        
        else:

            def graphing():
                
                cur.execute("set autocommit = 0")

                cur.execute("INSERT INTO net(Name,DOT,Net) SELECT StockName, DOP, (-1)*(BuyPrice*NoBought*(1+Brokerage/100)) FROM buy")
                cur.execute("INSERT INTO net(Name,DOT,Net) SELECT StockName, DOS, (SellPrice*NoSold*(1-Brokerage/100)) FROM sell")
                
                cur.execute("INSERT INTO t_net(DATE,net) SELECT DOT,sum(net) FROM net GROUP BY DOT ")
                cur.execute("SELECT * FROM t_net")
                records = cur.fetchall()
                datelist = []
                tnetlist = []
                dic = {}
                for x in records:
                    a,b = x
                    datelist.append(a)
                    tnetlist.append(b)

                for n in range(len(datelist)):
                    dic[datelist[n]] = tnetlist[n]

                datelist.sort()
                ntnetlist = []
                for x in datelist:
                    ntnetlist.append(dic[x])

                x_pos = np.arange(len(datelist))
                plt.plot(x_pos, ntnetlist,"bo")
                plt.title("DAILY PROFIT/LOSS")
                plt.xticks(x_pos,datelist)
                plt.xlabel("Dates")
                plt.ylabel("Loss/Profit")
                plt.show()

            graphing()
           
    ans_start = input("\nDo you want to exit: ")
    while ans_start not in ("y","Y","n","N"):
        print("\nWrong Input! Correct input are y, Y, n or N")
        ans_start = input("Give your input again : ")
        
print("\nThanks for using our software")
