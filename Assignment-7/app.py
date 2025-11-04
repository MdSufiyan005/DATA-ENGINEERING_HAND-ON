import streamlit as st
import pandas as pd
from db import get_all_employees, add_employee, update_employee, get_roles, delete_employee,get_departments,get_role_byid

st.title("CRUD operations on emplyees db")

menu = st.sidebar.selectbox("Choose Action",['View','Add','Update','Delete'])

departments = get_departments()
roles = get_roles()

dept_dict = {name: id for id,name in departments}
roles_dict = {name: id for id,name in roles}

if menu=="View":
    st.subheader("All employees")
    data = get_all_employees()
    # for emp in data:
    #     st.write(f"{emp[1]} | {emp[2]} | {get_role_byid(emp[3])} | {emp[4]}")
        # Convert to DataFrame
    df = pd.DataFrame(data, columns=["ID", "Name", "Department", "Role", "Email"])
    st.table(df)
    
elif menu=="Add":
    st.subheader("Add New Employee")
    name = st.text_input("Name")
    email = st.text_input("Email")
    dept = st.selectbox("Department",list(dept_dict.keys()))
    role = st.selectbox("Role",list(roles_dict.keys()))
    if st.button("Add"):
        add_employee(name,dept_dict[dept],roles_dict[role],email)
        st.success("Employee Added")
elif menu == "Update":
    st.subheader("Update employee")
    emp_id = st.number_input("EmployeeId",min_value=1)
    name = st.text_input("New Name")
    email = st.text_input("New Email")
    dept = st.selectbox("New dept",list(dept_dict.keys()))
    role = st.selectbox("New role",list(roles_dict.keys()))
    if st.button("Update"):
        update_employee(emp_id,name,dept_dict[dept],roles_dict[role],email)
        st.success("Employee Updated")
elif menu=="Delete":
    st.subheader("Delete employee")
    emp_id = st.number_input("Employee Id to delete",min_value=1)
    if st.button("Delete"):
        delete_employee(emp_id)
        st.warning("Employee deleted")