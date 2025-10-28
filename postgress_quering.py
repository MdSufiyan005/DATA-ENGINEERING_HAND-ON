# %%
from psycopg2 import connect

host = "localhost"
port = 5432
database = "EmployeesDb"
password = "admin"
username = "postgres"

def get_connection():
    return connect(
        host=host,
        port=port,
        database=database,
        user=username,
        password=password
    )


Creating_table_employee = """
CREATE TABLE IF NOT EXISTS employee (
    id Integer PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    employee_role INTEGER NOT NULL,
    department_id Integer,
    salary NUMERIC(10, 2) NOT NULL,
    FOREIGN KEY (department_id) REFERENCES department(department_id),
    FOREIGN KEY (employee_role) REFERENCES role(employee_role)
);
"""
Creating_table_department = """
    CREATE TABLE IF NOT EXISTS department(
    department_id INTEGER PRIMARY KEY,
    Department_name VARCHAR(100) NOT NULL,
    Employee_no INTEGER NOT NULL);
"""

Creating_table_role = """
    CREATE TABLE IF NOT EXISTS role(
    employee_role INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL
    );
"""

conn = get_connection()
curr = conn.cursor()

curr.execute(Creating_table_department)
curr.execute(Creating_table_role)
curr.execute(Creating_table_employee)


Insert_employee = """
INSERT INTO employee (id, name, employee_role, department_id, salary)
VALUES (%s, %s, %s, %s, %s);
"""
Insert_department = """
INSERT INTO department (department_id, Department_name, Employee_no)
VALUES (%s, %s, %s);
"""
Insert_role = """
INSERT INTO role (employee_role, name)
VALUES (%s, %s);
"""

employee_count_salary_by_department_query = """
    SELECT d.Department_name, COUNT(e.id) AS employee_count, SUM(e.salary) AS Total_salary
    FROM department d
    LEFT JOIN employee e ON d.department_id = e.department_id
    GROUP BY d.Department_name;
"""


try:
    conn = get_connection()
    curr = conn.cursor()

    curr.execute(Creating_table_department)
    curr.execute(Creating_table_role)
    curr.execute(Creating_table_employee)
    
    departments_value = [[1, 'HR', 10], [2, 'Engineering', 25], [3, 'Sales', 15]]
    for department in departments_value: 
        curr.execute(Insert_department, department)
    
    role_value = [[1, 'Manager'], [2, 'Developer'], [3, 'Salesperson'],[4,'Intern']]
    for role in role_value:
        curr.execute(Insert_role, role)
    
    employee_value = [[1, 'Joshua', 1, 1, 60000.00],
                      [2, 'Mohammad', 2, 2, 80000.00],
                      [3, 'Tanay', 3, 3, 70000.00],
                      [4, "Aman",3,3,72000.00],
                      [5, "Pranav",4,2,85000.00]]
    for employee in employee_value:
        curr.execute(Insert_employee, employee)
    
    conn.commit()
    
    curr.execute("SELECT * FROM employee;")
    employees = curr.fetchall()

    curr.execute("SELECT * FROM department;")
    departments = curr.fetchall()
    
    curr.execute("SELECT * FROM role;")
    role = curr.fetchall()
    
    curr.execute(employee_count_salary_by_department_query)
    results = curr.fetchall()

    print('----------------------------------------------------------------')
    print(" DATA PRESENT IN EMPLOYEE TABLE")
    for employee in employees:
        print(employee)

    print('----------------------------------------------------------------')
    print(" DATA PRESENT IN EMPDEPARTMENT TABLE")
    for department in departments:
        print(department)

    print('----------------------------------------------------------------')
    print(" DATA PRESENT IN ROLE TABLE")
    for roles in role:
        print(roles)

    print('----------------------------------------------------------------')
    print(" JOIN OPPERATION")
    for row in results:
        print(f"Department: {row[0]}, Employee Count: {row[1]}, Total Salary: {row[2]}")


except Exception as e:
    print(f"An error occurred: {e}")



curr.close()
conn.close()

# %%
