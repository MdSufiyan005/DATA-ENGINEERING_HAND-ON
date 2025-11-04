import psycopg2, os
from dotenv import load_dotenv
load_dotenv()

def connect():
    return psycopg2.connect(
        host = "localhost",
        database = "employees",
        user = "postgres",
        password = os.getenv("POSTGRES_PASSWORD")
    )

def get_all_employees():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
                SELECT e.id, e.name, d.name, r.id, e.email
                FROM employees as e
                JOIN departments d ON e.department_id = d.id
                JOIN roles r ON e.roles_id = r.id
                """)
    rows = cur.fetchall()
    conn.close()
    return rows

def add_employee(name, dept_id, role_id, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO employees (name, department_id, roles_id, email)
        VALUES (%s, %s, %s, %s)
    """, (name, dept_id, role_id, email))
    conn.commit()
    conn.close()

def update_employee(emp_id, name, dept_id, role_id, email):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE employees
        SET name=%s, department_id=%s, roles_id=%s, email=%s
        WHERE id=%s
    """, (name, dept_id, role_id, email, emp_id))
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    conn.commit()
    conn.close()

def get_departments():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM departments")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_roles():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM roles")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_role_byid(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT name FROM roles WHERE id= %s",(id,))
    res = cur.fetchone()
    conn.close()
    return res[0] if res else "UnknownRole"
