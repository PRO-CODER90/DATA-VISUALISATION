import pandas as pd
import matplotlib.pyplot as plt
#providing row directory
while True:
    pd.set_option('display.expand_frame_repr',False)
    print("="*55)
    print("\t\t\tGames Sales ")
    print("="*55)
    print("1. Books2 ")
    print("2. Sales ")
    print("3. Employees ")
    print("4. Exit")
    ch=int(input("Enter the choice "))
    if ch==1:
        while True:
            print('-'*55)
            print("\t\t\tGame Stop Menu ")
            print('-'*55)
            print("1. View the Data ")
            print("2. Add new Record ")
            print("3. Delete a Record ")
            print("4. Modify a Record ")
            print("5. Search a Record ")
            print("6. Sort the record")
            print("7. Filter by Brand ")
            print("8. Total Stock Value")
            print("9. Bar Chart - Price of Games ")
            print("10. Line Chart - Stock of Games ")
            print("11. Exit ")
            opt = int(input("enter your choice"))
            if opt==1:
                print()
                df=pd.read_csv(r"Book2.csv", index_col="PassengerId")
                print(df)
                print()
            elif opt==2:
                df = pd.read_csv("Inventory.csv", index_col="S.NO.")
                p = df.index.max()+1
                n = input("Enter the Product ID.")
                b = input("Enter the Product Name")
                cp = int(input("Enter the Product  Brand"))
                sp = int(input("Enter the Cost per pice"))
                d = int(input("Enter the Manufacturing Date"))
                k = int(input("Enter the No. of Units in Stock"))
                u = int(input("Enter the Selles Per Units"))
                t = int(input("Enter the Total Stock in Inventory"))
                s = int(input("Enter the stock"))
                l = [n,b,cp,sp,d,k,u,t,s]
                df.loc[p]=l
                print()
                print(df)
                print()
                df.to_csv("Inventory.csv")
            elif opt==3:
                df = pd.read_csv("Inventory.csv", index_col="S.NO.")
                p = int(input("Enter the product no to be deleted"))
                df.drop(p, inplace=True)
                print()
                print(df)
                print()
                print("Record Deleted")
                    
            elif opt==4:
                df = pd.read_csv("Inventory.csv", index_col="S.NO.")
                p = int(input("Enter the product no to be modified"))
                print("current details are ")
                print()
                print(df.loc[p])
                print()
                df.loc[p,'Cost Price'] = int(input("Enter the new Cost Price"))
                df.loc[p,'Selling Price'] = int(input("Enter the new Selling Price"))
                df.loc[p,'Stock'] = int(input("Enter the new Stock"))
                print()
                print(df)
                print()
                print("Record Modified")
                df.to_csv("Inventory.csv")
            elif opt==5:
                df = pd.read_csv("Inventory.csv", index_col="S.NO.")
                print()
            elif opt==2:
                df = pd.read_csv("Inventory.csv", index_col="Bill No")
                p = df.index.max()+1
                b = input("Enter the Customr Name")
                cp = input("Enter the Product Name")
                sp = int(input("Enter the Bill Amount"))
                s = input("Enter GST")
                ta=int(input("Enter Total Amount"))
                pm= input("Enter Payment Method")
                l = [b,cp,sp,s,ta,pm]
                df.loc[p]=l
                print()
                print(df)
                print()
                df.to_csv("Sales.csv")
            elif opt==3:
                df = pd.read_csv("Sales.csv", index_col="Bill No")
                p = int(input("Enter the bill no to be deleted"))
                df.drop(p, inplace=True)
                print()
                print(df)
                print()
                print("Record Deleted")
                df.to_csv("Sales.csv")
            elif opt==4:
                df = pd.read_csv("Sales.csv", index_col="Bill No")
                p = int(input("Enter the bill no to be modified"))
                print("current details are ")
                print()
                print(df.loc[p])
                print()
                df.loc[p,'Product Name'] = input("Enter the new Product Name")
                df.loc[p,'Bill Amount'] = int(input("Enter the new Bll Amount"))
                df.loc[p,'Total Amount'] = int(input("Enter the new Total Amount"))
                df.loc[p,'Payment Method']=input("Enter the new Payment Method")
                print()
                print(df)
                print()
                print("Record Modified")
                df.to_csv("Sales.csv")
            elif opt==5:
                df = pd.read_csv("Sales.csv", index_col="Bill No")
                p = int(input("Enter the bill no to be searched "))
                print("Current details are ")
                print()
                print(df.loc[p])
                print()
            elif opt==6:
                df = pd.read_csv("Sales.csv", index_col="Bill No")
                c = input("Enter the name of the column by which you")
                o = int(input("Enter sort order 1-Ascending, 2-Descending"))
                if o==1:
                    print()
                    print(df.sort_values(c))
                    print()
                else:
                    print()
                    print(df.sort_values(c, ascending=False))
                    print()
            elif opt==7:
                df = pd.read_csv("Sales.csv",index_col="Bill No")
                b = input("Enter Payment Method ")
                print()
                print(df[df['Payment Method']==b])
                print()
            elif opt==8:
                df = pd.read_csv("Sales.csv",index_col="Bill No")
                df['TOTAL VALUE']=df['Bill Amount']*df['Total Amount']
                print()
                print(df[['TOTAL VALUE']])
                print() 
            elif opt==9:
                df = pd.read_csv("Sales.csv",index_col="Bill No")
                df[['Product Name','Total Amount']].plot(kind='bar', color='blue', edgecolor='k', hatch='/')
                plt.xticks(df.index-101, df['Product Name'], rotation=10, fontsize=10)
                plt.xlabel("Name of Product", fontsize=14)
                plt.ylabel("Price", fontsize=14)
                plt.title("Comparison of Prices ", fontsize=18)
                plt.subplots_adjust(bottom=0.2)
                plt.get_current_fig_manager().window.state('zoomed')
                plt.show()
            elif opt==10:
                df = pd.read_csv("Sales.csv",index_col="Bill No")
                df[['Product Name','Total Amount']].plot(kind='line', ls='dashdot',marker='*', markersize=8, color='r', markeredgecolor='k')
                plt.xticks(df.index, df['Product Name'], rotation=10, fontsize=10)
                plt.xlabel("Name of Product", fontsize=14)
                plt.ylabel("Amount", fontsize=14)
                plt.title("Amount Report ", fontsize=18)
                plt.subplots_adjust(bottom=0.2)
                plt.get_current_fig_manager().window.state('zoomed')
                plt.show()
            elif opt==10:
                break
        
    elif ch==3:
        while True:
            print('-'*55)
            print("\t\t\tEmployee Menu ")
            print('-'*55)
            print("1. View the Data ")
            print("2. Add new Record ")
            print("3. Delete a Record ")
            print("4. Modify a Record ")
            print("5. Search a Record ")
            print("6. Sort the record")
            print("7. Filter by Brand ")
            print("8. Total Number of Employee ")
            print("9. Bar Chart - Salary of Employees ")
            print("10. Line Chart - Salary of Employees ")
            print("11. Exit ")
            opt = int(input("enter your choice"))
            if opt==1:
                print()
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                print(df)
                print()
            elif opt==2:
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                p = df.index.max()+1
                n = input("Enter the Employee name")
                b = input("Enter the Position")
                cp = int(input("Enter the Salary"))
                sp = input("Enter the Address ")
                s = int(input("Enter the Mobile No"))
                l = [n,b,cp,sp,s]
                df.loc[p]=l
                print()
                print(df)
                print()
                print("Record Savede")
                df.to_csv("Employees.csv")
            elif opt==3:
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                p = int(input("Enter the Employee ID to be deleted"))
                df.drop(p, inplace=True)
                print()
                print(df)
                print()
                print("Record Deleted")
                df.to_csv("Employees.csv")
            elif opt==4:
               df=pd.read_csv("Employees.csv", index_col="Employee ID")
               p = int(input("Enter the EmpID to be modified"))
               print("current details are ")
               print()
               print(df.loc[p])
               print()
               df.loc[p,'Position'] = input("Enter the new position")
               df.loc[p,'Salary'] = int(input("Enter the new salary"))
               df.loc[p,'Address'] = input("Enter the new Address")
               df.loc[p,'Mobile No'] = input("Enter the new mobile number")
               print()
               print(df)
               print()
               print("Record Modified")
               df.to_csv("Employees.csv")
            elif opt==5:
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                p = int(input("Enter the EmpID to be searched "))
                print("Current details are ")
                print()
                print(df.loc[p])
                print()
            elif opt==6:
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                c = input("Enter the name of the column by which you want to sort the values")
                o = int(input("Enter sort order 1-Ascending, 2-Descending"))
                if o==1:
                    print()
                    print(df.sort_values(c))
                    print()
                else:
                    print()
                    print(df.sort_values(c, ascending=False))
                    print()
            elif opt==7:
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                b = input("Enter the position ")
                print()
                print(df[df['Position']==b])
                print()
            elif opt==8:
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                print()
                print("Total number of Employees are ",len(df))
                print() 
            elif opt==9:
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                df[['Employee Name','Salary']].plot(kind='bar', color='c', edgecolor='m', hatch='/')
                plt.xticks(df.index-101, df['Employee Name'], rotation=0, fontsize=10)
                plt.xlabel("Name of Employee", fontsize=14)
                plt.ylabel("Salary", fontsize=14)
                plt.title("Salary of Employees ", fontsize=18)
                plt.subplots_adjust(bottom=0.2)
                plt.get_current_fig_manager().window.state('zoomed')
                plt.show()
            elif opt==10:
                df=pd.read_csv("Employees.csv", index_col="Employee ID")
                df[['Employee Name','Salary']].plot(kind='line', ls='dashed',marker='o', markersize=8, color='g', markeredgecolor='k')
                plt.xticks(df.index,df['Employee Name'],rotation=0,fontsize=10)
                plt.xlabel("Name of Emplyee",fontsize=14)
                plt.ylabel("Salary",fontsize=14)
                plt.title("Salary of Employee ", fontsize=18)
                plt.subplots_adjust(bottom=0.2)
                plt.get_current_fig_manager().window.state('zoomed')
                plt.show()
            elif opt==11:
                break









