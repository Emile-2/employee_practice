def read_option():
    while True:
        user_option = input("""
        This is a list of your options: 
        add: Add an Employee 
        remove: Remove an Employee 
        list: List the Employees
        update: Update Employee Data 
        id: View employee data by ID
        total: View total amount of employees 
        exit: Exit the app
        Enter Selected Option:""")
        user_option = user_option.strip()

        if user_option in ["add", "remove", "update", "list", "exit", "id", "total"]:
            return user_option
        else:
            print("Error, You should select one of the options in the list")

def read_name(text):
    while True:
        name = input(f"Please Enter The Employee {text}:")
        name = name.strip()

        if len(name) >= 2:
            return name
        else:
            print(f"Error, The Employee {text} Name should be at least 2 Characters")

def read_year():
    while True:
        year_str = input("Please Enter the Employee Birth Year:")
        year_str = year_str.strip()

        if year_str.isdigit():
            year = int(year_str)
            if (year >= 1900) and (year <= 2004):
                return year
            else:
                print("Error, The Employee Birth Year should be between 1900 and 2004")
        else:
            print("Error, The Employee Birth Year should be a number")

def read_month():
    while True:
        month_str = input("Please Enter the Employee Birth Month:")
        month_str = month_str.strip()

        if month_str.isdigit():
            month = int(month_str)
            if (month >= 1) and (month <= 12):
                return month
            else:
                print("Error, The Employee Birth Month should be between 1 and 12")
        else:
            print("Error, The Employee Birth Month should be a number")

def read_position():
    while True:
        position = input("Please Enter The Employee Position:")
        position = position.strip()

        if len(position) >= 1:
            return position
        else:
            print("Error, The Employee Position should be at least 1 Characters")

def read_day():
    while True:
        day_str = input("Please Enter the Employee Birth Day:")
        day_str = day_str.strip()

        if day_str.isdigit():
            day = int(day_str)
            if (day >= 1) and (day <= 31):
                return day
            else:
                print("Error, The Employee Birth Day should be between 1 and 31")
        else:
            print("Error, The Employee Birth Day should be a number")

def read_is_graduated():
    while True:
        is_graduated_str = input("Have the Employee graduated from the univesity (y/n):")
        is_graduated_str = is_graduated_str.strip()

        if is_graduated_str in ["y", "n"]:
            if is_graduated_str == "y":
                return True
            else:
                return False
        else:
            print("Error, Please Enter y or n")

def read_employee_id():
    while True:
        id_str = input("Please Enter the Employee ID:")
        id_str = id_str.strip()

        if id_str.isdigit():
            id = int(id_str)
            if id > 0 :
                return id
            else:
                print("Error, The Employee ID should be positive number")
        else:
            print("Error, The Employee ID should be a number")

class Employee:

    def __init__(self, f_name, l_name, y_ob, m_ob, d_ob, position, graduated):
        self.first_name = f_name
        self.last_name = l_name
        self.year_of_birth = y_ob
        self.month_of_birth = m_ob
        self.day_of_birth = d_ob
        self.position = position
        self.graduation = graduated

    def print_data(self):
        print(self.first_name, self.last_name, self.year_of_birth, self.month_of_birth, self.day_of_birth, self.position, self.graduation)

    def save_data(self):
        saved_data = self.first_name, self.last_name, self.year_of_birth, self.month_of_birth, self.day_of_birth, self.position, self.graduation
        return saved_data

    def add_to_dict(self, id):

        employee_list = save_data()

        return employee_list


    def first_name(self):
        pass



if __name__ == "__main__":
    all_employees_dict = {
        2: {'first_name': 'test', 'last_name': 'data', 'position': 'engineer', 'birth_year': 1972, 'birth_month': 8,
            'birth_day': 14, 'is_graduated': True}}
    while True:
        option = read_option()

        if option == "add":
            print("The user wants to add an Employee")
            add_new_employee = Employee(f"{read_name('First Name')}",
                                        f"{read_name('Last Name')}",
                                        f"{read_year()}",
                                        f"{read_month()}",
                                        f"{read_day()}",
                                        f"{read_position()}",
                                        f"{read_is_graduated()}")

            print(add_new_employee.saved_data())

            # employee_dict = create_employee_dictionary()
            #
            # # employee_id = read_employee_id()
            # employee_id = employee_dict["id"]
            #
            # all_employees_dict[employee_id] = employee_dict
            #
            # print(all_employees_dict)

        elif option == "remove":
            print("The user wants to remove an Employee")
            # employee_id = read_employee_id()
            # del all_employees_dict[employee_id]

        elif option == "list":
            print("The user wants a list of the employees")
            # print_all_employees_data()

        elif option == "update":
            print("The user wants to update the data of an employee")


        elif option == "id":
            print("The user wants to view the data of a particular employee by ID")
            # employee_id = read_employee_id()
            # view_single_employee(employee_id)

        elif option == "total":
            print("The user wants to view the total amount of employees")
            # view_total()



        elif option == "exit":
            print("Thanks, see you later")
            break
        else:
            print("Unknown option")

