import pandas as pd
import streamlit as st
from models import add_doctor, update_doctor, delete_doctor,list_doctors

if __name__=="__main__":
    st.title("Doctors Management system")

    menu = st.sidebar.selectbox("Choice",['View','Add','Update','Delete'])

    if menu=="View":
        st.subheader("View all doctors")
        data = list_doctors()
        df = pd.json_normalize(data)
        print(df)
        # df = pd.DataFrame(df,columns=['Name','Specialization','Phone','email'])
        st.table(df)
        
        
    elif menu=="Add":
        st.subheader("Add New Doctor")
        name = st.text_input("Name")
        specialization = st.selectbox("Choose the Specialization",['Radiology','Cardiology','Optomology'])
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        if st.button("Add doctor"):
            add_doctor(name, specialization,phone, email)
            st.success("Doctor added successfully!")
            st.experimental_rerun()
        else:
            st.warning("Pls fill in all required details")
            
    elif menu =="Update":
        st.subheader("Update doctor information")
        name = st.text_input("Enter doctors name to update")
        field = st.selectbox("Select Field to Update",['specialization','name','email'])
        new_value = st.text_input("Enter new value")
        if st.button("Save Changes"):
            update_doctor(name, field, new_value)
            st.success("Doctor details are updated")
            st.experimental_rerun()