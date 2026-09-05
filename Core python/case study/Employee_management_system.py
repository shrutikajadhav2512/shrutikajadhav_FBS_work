import pandas as pd
def show_emp():
    data=pd.DataFrame([v for v in all_emp_details.values()],columns=["ID","NAME","SALARY","DEPARTMENT"])
    print(data)
def update_emp(id):
    print("NOTE: If dont want to change leave field blank..")
    emp=all_emp_details.get(id)
    if(emp):
        name=input(f"Enter new NAME({emp[1]}):") or emp[1]
        salary = float(input(f"Enter new SALARY({emp[2]}):") or emp[2])
        dept=input(f"Enter new DEPARTMENT({emp[3]}):") or emp[3]
        all_emp_details[id]=[id,name,salary,dept]
        return "Employee updated successfully.."
    else:
        return "Id not found."

def delete_emp():
    id=int(input("Enter id,you want to delete:"))
    if(id in all_emp_details):
        del all_emp_details[id]
        return "Delete employee successfully."
    else:
        return "Id not found."
def search_emp():
    id=int(input("Enter id,you want to search: "))
    if(id in all_emp_details):
        emp=all_emp_details[id]
        print("Employee found..")
        print("id=",emp[0])
        print("name=",emp[1])
        print("salary=",emp[2])
        print("deparment=",emp[3])
    else:
        print("Id not found.")
def logout():
    print("Logout successfully.....")


def add_emp():
    id=int(input("Enter Id:"))
    name=input("Enter Name:")
    salary=float(input("Enter salary:"))
    dept=input("Enter Department:")
    if(id not in all_emp_details):
        all_emp_details[id]=[id,name,salary,dept]
        return "Employee added successfully.."
    else:
        return "ID already exist.."
    

def employeemanage():
    print("####EMPLOYEE MANAGEMENT SYSTEM..")
    ch=0
    while(ch!="6"):
        print('''Please select option from below..
        1.Add employee
        2.Show all employee
        3.Update employee
        4.Delete employee
        5.Search employee
        6.Logout''')
        ch=input("Enter choice:")
        if(ch=="1"):
            res=add_emp()
            print(res)
        elif(ch=="2"):
            show_emp()
        elif(ch=="3"):
            print("WARNING:ID not allowed to update..")
            id=int(input("Enter Id:"))
            res=update_emp(id)
            print(res)
        
        elif(ch=="4"):
            delete_emp()
        elif(ch=="5"):
            search_emp()
        elif(ch=="6"):
            logout()
            break
        else:
            print("Wrong input")


def login():
    id=input("Enter your id:")
    passw=(input("Enter password:"))
    if(id=="admin" and passw=="123"):
        print("login successfully..")
        employeemanage()
    else:
        print("Wrong input")
    print()

def main():
    ch=0
    while(ch!='2'):
        print("##Dashboard##")
        print("Welcome..")
        print('''Please select one option
        1.Login
        2.Exit''')
        ch=input("select 1 or 2 option:")
        if(ch=='1'):
            login()
        elif(ch=='2'):
            print("Thank you..")
        else:
            print("Wrong input")
all_emp_details={}
main()