import mysql.connector
from getpass import getpass

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="iti",
        password="test@1234",
        database="mydatabase"
    )

def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee (
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            age INT,
            department VARCHAR(255),
            salary FLOAT
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

class Employee:
    employees_list = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        Employee.employees_list.append(self)
        self.insert_to_db()

    def insert_to_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO employee (first_name, last_name, age, department, salary)
            VALUES (%s, %s, %s, %s, %s)
        ''', (self.first_name, self.last_name, self.age, self.department, self.salary))
        conn.commit()
        cursor.close()
        conn.close()

    def transfer(self, new_department):
        self.department = new_department
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE employee SET department = %s WHERE first_name = %s AND last_name = %s
        ''', (self.department, self.first_name, self.last_name))
        conn.commit()
        cursor.close()
        conn.close()

    def fire(self):
        Employee.employees_list.remove(self)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM employee WHERE first_name = %s AND last_name = %s
        ''', (self.first_name, self.last_name))
        conn.commit()
        cursor.close()
        conn.close()

    def show(self):
        print(f'Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}')

    @staticmethod
    def list_employees():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employee')
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {row[0]} {row[1]}, Age: {row[2]}, Department: {row[3]}, Salary: {row[4]}')
        cursor.close()
        conn.close()

    @staticmethod
    def load_employees():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employee')
        rows = cursor.fetchall()
        for row in rows:
            Employee(*row)
        cursor.close()
        conn.close()

class Manager(Employee):
    def __init__(self, first_name, last_name, age, department, salary, managed_department):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        print(f'Name: {self.first_name} {self.last_name}, Age: {self.age}, Department: {self.department}, Managed Department: {self.managed_department}, Salary: Confidential')

def print_menu():
    print('Options:')
    print('add - Add new employee')
    print('transfer - Transfer employee')
    print('fire - Fire employee')
    print('show - Show employee data')
    print('list - List all employees')
    print('q - Quit the program')

def main():
    initialize_db()
    Employee.load_employees()

    while True:
        print_menu()
        choice = input('Enter your choice: ').strip().lower()

        if choice == 'q':
            break
        elif choice == 'add':
            role = input('If manager press "m"/ if employee press "e": ').strip().lower()
            first_name = input('First Name: ').strip()
            last_name = input('Last Name: ').strip()
            age = int(input('Age: ').strip())
            department = input('Department: ').strip()
            salary = float(input('Salary: ').strip())
            
            if role == 'm':
                managed_department = input('Managed Department: ').strip()
                Manager(first_name, last_name, age, department, salary, managed_department)
            else:
                Employee(first_name, last_name, age, department, salary)

        elif choice == 'transfer':
            first_name = input('First Name: ').strip()
            last_name = input('Last Name: ').strip()
            new_department = input('New Department: ').strip()
            for emp in Employee.employees_list:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.transfer(new_department)
                    break

        elif choice == 'fire':
            first_name = input('First Name: ').strip()
            last_name = input('Last Name: ').strip()
            for emp in Employee.employees_list:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.fire()
                    break

        elif choice == 'show':
            first_name = input('First Name: ').strip()
            last_name = input('Last Name: ').strip()
            for emp in Employee.employees_list:
                if emp.first_name == first_name and emp.last_name == last_name:
                    emp.show()
                    break

        elif choice == 'list':
            Employee.list_employees()
        else:
            print('Invalid choice, please try again.')

if __name__ == "__main__":
    main()
