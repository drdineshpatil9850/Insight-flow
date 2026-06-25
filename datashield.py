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

import tkinter as tk
from tkinter import filedialog, messagebox

# ---------------------------
# Functions
# ---------------------------
def upload_file():
    file_path = filedialog.askopenfilename(
        title="Select Dataset",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("Excel Files", "*.xlsx"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        file_label.config(text=f"Selected:\n{file_path}")

def get_started():
    messagebox.showinfo(
        "Insight Flow",
        "Dataset uploaded successfully!\nGenerating visual insights..."
    )

# ---------------------------
# Main Window
# ---------------------------
root = tk.Tk()
root.title("Insight Flow")
root.geometry("1100x700")
root.configure(bg="#F4F7FC")

# ---------------------------
# Header
# ---------------------------
title = tk.Label(
    root,
    text="Insight Flow",
    font=("Segoe UI", 32, "bold"),
    bg="#F4F7FC",
    fg="#1E3A8A"
)
title.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Transform your CSV/XLSX data into powerful visual insights",
    font=("Segoe UI", 14),
    bg="#F4F7FC",
    fg="#555"
)
subtitle.pack()

# ---------------------------
# Upload Section
# ---------------------------
upload_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)
upload_frame.pack(pady=25, padx=50, fill="x")

upload_title = tk.Label(
    upload_frame,
    text="📂 Upload CSV / XLSX File",
    font=("Segoe UI", 18, "bold"),
    bg="white"
)
upload_title.pack(pady=15)

upload_btn = tk.Button(
    upload_frame,
    text="Choose File",
    font=("Segoe UI", 12),
    bg="#2563EB",
    fg="white",
    padx=20,
    pady=8,
    command=upload_file
)
upload_btn.pack()

file_label = tk.Label(
    upload_frame,
    text="No file selected",
    bg="white",
    fg="gray",
    font=("Segoe UI", 10)
)
file_label.pack(pady=15)

# ---------------------------
# Charts Preview Section
# ---------------------------
preview_title = tk.Label(
    root,
    text="Supported Visualizations",
    font=("Segoe UI", 20, "bold"),
    bg="#F4F7FC",
    fg="#111827"
)
preview_title.pack(pady=10)

charts_frame = tk.Frame(root, bg="#F4F7FC")
charts_frame.pack()

# Histogram
hist_frame = tk.Frame(charts_frame, bg="white", bd=1, relief="solid")
hist_frame.grid(row=0, column=0, padx=15)

canvas1 = tk.Canvas(hist_frame, width=180, height=140, bg="white")
canvas1.pack()
canvas1.create_rectangle(20, 100, 50, 40, fill="#3B82F6")
canvas1.create_rectangle(60, 80, 90, 40, fill="#60A5FA")
canvas1.create_rectangle(100, 50, 130, 40, fill="#2563EB")
canvas1.create_rectangle(140, 90, 170, 40, fill="#93C5FD")

tk.Label(
    hist_frame,
    text="Histogram",
    bg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

# Pie Chart
pie_frame = tk.Frame(charts_frame, bg="white", bd=1, relief="solid")
pie_frame.grid(row=0, column=1, padx=15)

canvas2 = tk.Canvas(pie_frame, width=180, height=140, bg="white")
canvas2.pack()

canvas2.create_arc(
    30, 20, 140, 130,
    start=0, extent=120,
    fill="#2563EB"
)

canvas2.create_arc(
    30, 20, 140, 130,
    start=120, extent=90,
    fill="#60A5FA"
)

canvas2.create_arc(
    30, 20, 140, 130,
    start=210, extent=150,
    fill="#93C5FD"
)

tk.Label(
    pie_frame,
    text="Pie Chart",
    bg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

# Line Chart
line_frame = tk.Frame(charts_frame, bg="white", bd=1, relief="solid")
line_frame.grid(row=0, column=2, padx=15)

canvas3 = tk.Canvas(line_frame, width=180, height=140, bg="white")
canvas3.pack()

canvas3.create_line(
    20, 100,
    60, 80,
    100, 90,
    140, 50,
    170, 30,
    fill="#10B981",
    width=3
)

tk.Label(
    line_frame,
    text="Line Chart",
    bg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

# Bar Chart
bar_frame = tk.Frame(charts_frame, bg="white", bd=1, relief="solid")
bar_frame.grid(row=0, column=3, padx=15)

canvas4 = tk.Canvas(bar_frame, width=180, height=140, bg="white")
canvas4.pack()

canvas4.create_rectangle(20, 70, 50, 120, fill="#F97316")
canvas4.create_rectangle(70, 40, 100, 120, fill="#FB923C")
canvas4.create_rectangle(120, 20, 150, 120, fill="#EA580C")

tk.Label(
    bar_frame,
    text="Bar Chart",
    bg="white",
    font=("Segoe UI", 12, "bold")
).pack(pady=5)

# ---------------------------
# Description
# ---------------------------
desc = tk.Label(
    root,
    text="""
Upload your CSV or Excel file and instantly explore:
• Histograms
• Pie Charts
• Bar Charts
• Line Charts
• Data Insights & Analytics
""",
    bg="#F4F7FC",
    font=("Segoe UI", 12),
    justify="center"
)
desc.pack(pady=25)

# ---------------------------
# Get Started Button
# ---------------------------
start_btn = tk.Button(
    root,
    text="Get Started",
    font=("Segoe UI", 16, "bold"),
    bg="#10B981",
    fg="white",
    padx=30,
    pady=12,
    command=get_started
)
start_btn.pack(side="bottom", pady=25)

root.mainloop()












































































































































































USERS_FILE = "users.json"

# ---------- Utility functions ----------

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password, users):
    if username in users:
        return users[username]["password"] == hash_password(password)
    return False

# ---------- Session state ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

users = load_users()

# ---------- UI ----------
st.title("🔐 Streamlit Login System (JSON based)")

menu = ["Login", "Register", "Dashboard"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------- Register ----------
if choice == "Register":
    st.subheader("Create New Account")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Register"):
        if new_user in users:
            st.error("User already exists!")
        elif new_user == "" or new_pass == "":
            st.warning("Please fill all fields")
        else:
            users[new_user] = {
                "password": hash_password(new_pass)
            }
            save_users(users)
            st.success("Account created successfully!")

# ---------- Login ----------
elif choice == "Login":
    st.subheader("Login to your account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password, users):
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password")

# ---------- Dashboard ----------
elif choice == "Dashboard":
    if st.session_state.logged_in:
        st.subheader(f"👋 Hello {st.session_state.user}")
        st.write("You are successfully logged in.")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.rerun()
    else:
        st.warning("Please login first to access dashboard.")





















































































        

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
               


















                
                       
   
       
               

              
 
