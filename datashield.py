import matplotlib.pyplot as plt
from scipy import stats  
from pandas.plotting import scatter_matrix
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans
import streamlit as st
from sklearn.neural_network import MLPRegressor
import hashlib
import json
import os





st.title("Insight flow")
st.markdown(
        """

        <style>
        .stApp {
           background-color: "#1E293B"
           color: green;

        }
        </style>
        """,

        unsafe_allow_html=True
)



import re

def is_strong_password(password):
    """
    Password must:
    - Be at least 8 characters long
    - Contain uppercase and lowercase letters
    - Contain a number
    - Contain a special character
    """
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True


# Registration
print("=== Create Account ===")
username = input("Create username: ")

while True:
    password = input("Create strong password: ")

    if is_strong_password(password):
        print("Account created successfully!\n")
        break
    else:
        print(
            "Password must be at least 8 characters long and contain "
            "uppercase, lowercase, number, and special character."
        )

# Login
print("=== Login ===")
login_username = input("Username: ")
login_password = input("Password: ")

if login_username == username and login_password == password:
    print("\nLogin successful!")
    print(f"Welcome, {username}!")
else:
    print("\nInvalid username or password.")

































































































        

file = st.file_uploader("Upload your file", type=["csv", "xlsx"])
if file is not None:
        if file.name.endswith(".csv"):
                try:
                        data = pd.read_csv(file, encoding="utf-8")
                        st.success("File uploaded successfully")
                        st.write(data.head())
                        st.write("Rows:", data.shape[0], "Columns:", data.shape[1])
                                                                     

                

                except:
                        file.seek(0)
                        data = pd.read_csv(file, encoding="latin1")
                        st.success("File uploaded successfully")
                        st.dataframe(data.head())

        elif file.name.endswith(".xlsx"):
                data = pd.read_excel(file, engine="openpyxl")

        columns = data.columns.tolist()
                        

        

        numeric_columns = data.select_dtypes(include=["number"]).columns.tolist()

               
        
                


        chart_type = st.selectbox("Choose Visualization/Model",[
                "Box plot",                 
                "Density plot",
                "Scatter matrix plot",
                "Simple linear regression",
                "Multiple linear regression",
                "Histogram",
                "Bar chart",
                "Pie chart",
                "Line chart"
                ])

    


        if chart_type == "Histogram":
                hist_col = st.selectbox("Choose numeric column", numeric_columns, key="hist")

                fig, ax = plt.subplots()
                ax.hist(data[hist_col])
                ax.set_title("Histogram")
               
                st.pyplot(fig)
                plt.savefig("Hist.png")
                
                
               
    


        
     

        elif chart_type == "Box plot":
                box_col = st.selectbox("Choose numeric column", numeric_columns, key="box")

                fig, ax = plt.subplots()
                ax.boxplot(data[box_col].dropna())
                ax.set_title("box plot")
                
                st.pyplot(fig)
                plt.savefig("Box.png")
            




























        elif chart_type == "Line chart":
                line_col = st.selectbox("Choose numeric column", numeric_columns, key="line")
                
                st.line_chart(data[line_col])
                
                plt.savefig("Line.png")
                

















        elif chart_type == "Bar chart":
            bar_col = st.selectbox("Choose numeric column", numeric_columns, key="bar")
            
            st.bar_chart(data[bar_col])

            plt.savefig("Bar.png")
                

                































        elif chart_type == "Scatter matrix plot":
                x_col = st.selectbox("Choose X-axis", numeric_columns)
                y_col = st.selectbox("Choose Y-axis", numeric_columns)

                fig, ax = plt.subplots()
                ax.scatter(data[x_col], data[y_col])
                
                ax.set_title("Scatter box")
                
               
                st.pyplot(fig)
                
                plt.savefig("Scatter.png")
               

        


























        elif chart_type == "Density plot":
                density_col = st.selectbox("Choose numeric column", numeric_columns, key="Density")

                fig, ax = plt.subplots()
                sns.kdeplot(data[density_col].dropna())
                ax.set_title("Density Plot")
               
               
                st.pyplot(fig)
                plt.savefig("Density.png")
               

                














        elif chart_type == "Simple linear regression":
                x_col = st.selectbox("Choose X-axis", numeric_columns)
                y_col = st.selectbox("Choose Y-axis", numeric_columns)

                



        
                X = data[[x_col]]
                y = data[[y_col]]

                model = LinearRegression()
                model.fit(X, y)

                y_pred = model.predict(X)

               
        
               
                fig, ax = plt.subplots()
                ax.scatter(X, y, color='blue')
                ax.plot(X, y_pred, color='red')
               
                ax.set_title("Simple Linear Regression")
                

                st.pyplot(fig)
                plt.savefig("Simple.png")
               
                
               
        elif chart_type == "Pie chart":
               pie_col = st.selectbox("Choose numeric column", numeric_columns)

               fig, ax = plt.subplots()

               values = data[pie_col].value_counts()
               ax.pie(values, labels=values.index, autopct='%1.1f%%')

              
               ax.set_title("Pie chart")
               
               st.pyplot(fig)
               plt.savefig("Pie.png") 






















                
       

    # -------- Multiple Linear Regression Plot --------
        elif chart_type == "Multiple linear regression":
                x_cols = st.selectbox("Select X-axis ", numeric_columns)
                y_col = st.selectbox("Select Y-axis", numeric_columns)


                if len(x_cols) >0:
                        X = data[[x_cols]]
                        y = data[[y_col]]

                        model = LinearRegression()
                        model.fit(X, y)

                        y_pred = model.predict(X)



                
                
                

                fig, ax = plt.subplots()
                ax.scatter(y, y_pred, color='purple')
               
                

               
                ax.set_title("Actual vs Predicted")
                

                st.pyplot(fig)
                
                plt.savefig("Multiple.png")
               


















                
                       
   
       
               

              
 
