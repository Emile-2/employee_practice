class Employee:
    def __init__(self, id, f_name, l_name, position, y_ob, m_ob, d_ob, is_graduated):
        self.employee_id = id
        self.first_name = f_name
        self.last_name = l_name
        self.position = position
        self.year_of_birth = y_ob
        self.month_of_birth = m_ob
        self.day_of_birth = d_ob
        self.is_graduated = is_graduated

    def print_name(self):
        print(self.first_name, self.last_name)

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_position(self):
        return self.position

    def get_year_of_birth(self):
        return  self.year_of_birth

    def get_month_of_birth(self):
        return self.month_of_birth

    def get_day_of_birth(self):
        return self.day_of_birth

    def get_is_graduated(self):
        return self.is_graduated

    def get_id(self):
        return self.employee_id

    def change_attribute(self, update_attribute):
        if update_attribute == "first_name":
            new_first_name = read_name("New First Name")
            return new_first_name

        elif update_attribute == "last_name":
            new_last_name = read_name("New last Name")
            return new_last_name

        elif update_attribute == "position":
            new_position = read_position()
            return new_position

        elif update_attribute == "year_of_birth":
            new_year = read_year()
            return new_year

        elif update_attribute == "month_of_birth":
            new_month = read_month()
            return new_month

        elif update_attribute == "day_of_birth":
            new_day = read_day()
            return new_day

        elif update_attribute == "is_graduated":
            new_is_graduated = read_is_graduated()
            return new_is_graduated

    def add_to_dict(self):
        employee_id_value = self.employee_id
        first_name_value = self.first_name
        last_name_value = self.last_name
        position_value = self.position
        year_of_birth_value = self.year_of_birth
        month_of_birth_value = self.month_of_birth
        day_of_birth_value = self.day_of_birth
        is_graduated_value = self.is_graduated

        employee_temp_dict = {"id": employee_id_value,
                              "first_name": first_name_value,
                              "last_name": last_name_value,
                              "position" : position_value,
                              "year_of_birth" : year_of_birth_value,
                              "month_of_birth" : month_of_birth_value,
                              "day_of_birth" : day_of_birth_value,
                              "is_graduated" : is_graduated_value}
        # print(employee_temp_dict)
        return employee_temp_dict

def read_field_option():
    while True:
        field_option = input(
            "Please Enter the field you want to update: first_name, last_name, position, birth_year, birth_month, birth_day, is_graduated:")
        field_option = field_option.strip()

        if field_option in ["first_name", "last_name", "position", "birth_year", "birth_month", "birth_day",
                            "is_graduated"]:
            return field_option
        else:
            print("Please enter one of the mentioned fields")

def print_all_employees_data():
    for employee_id_key in employee_dict:
        print(f"The data of the employee with Employee_ID = {employee_id_key}")
        print(employee_dict[employee_id_key])

def read_option():
    while True:
        user_option = input("""
        This is a list of your options: 
        Add: Add an Employee 
        Remove: Remove an Employee 
        List: List the Employees
        Update: Update Employee Data 
        ID: View employee data by ID
        Total: View total amount of employees 
        Exit: Exit the app
        Enter Selected Option:""")
        user_option = user_option.strip()

        if user_option.lower() in ["add", "remove", "update", "list", "exit", "id", "total"]:
            return user_option.lower()
        else:
            print("Error, You should select one of the options in the list")

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

def read_name(text):
    while True:
        name = input(f"Please Enter The Employee {text}:")
        name = name.strip()

        if len(name) >= 2:
            return name
        else:
            print(f"Error, The Employee {text} Name should be at least 2 Characters")

def read_position():
    while True:
        position = input("Please Enter The Employee Position:")
        position = position.strip()

        if len(position) >= 1:
            return position
        else:
            print("Error, The Employee Position should be at least 1 Characters")

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

if __name__ == "__main__":

    employee_dict = {}
    while True:

        options = read_option()

        if options == "add":
            print("The user wants to add an Employee")

            employee = Employee(read_employee_id(),
                                read_name("First Name"),
                                read_name("Last Name"),
                                read_position(),
                                read_year(),
                                read_month(),
                                read_day(),
                                read_is_graduated()
                                )  # using my input to fill in f_name

            employee.print_name()  # using object method to print name of person
            employee_dict[employee.get_id()] = employee.add_to_dict()  # adding a dictionary to the dictionary using id as the key
            print("----------------------------------")
            print(employee_dict)

        elif options == "remove":

            print("The user wants to remove an employee")
            id_to_remove = read_employee_id()
            employee_dict.pop(id_to_remove, "Error, Key does not exist")

        elif options == "list":
            print("The user wants to list all employees")
            print_all_employees_data()

        elif options == "update":
            print("The user wants to update an employee")
            update_option = read_field_option()
            employee_dict[employee.get_id()][update_option] = employee.change_attribute(update_option)











