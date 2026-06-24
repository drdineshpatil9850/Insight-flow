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

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Insight Flow</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    background:#f4f7fc;
    color:#333;
}

header{
    background:linear-gradient(135deg,#2563eb,#06b6d4);
    color:white;
    text-align:center;
    padding:80px 20px;
}

header h1{
    font-size:3.5rem;
    margin-bottom:15px;
}

header p{
    font-size:1.2rem;
    max-width:700px;
    margin:auto;
}

.container{
    width:90%;
    max-width:1200px;
    margin:auto;
}

.features{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
    gap:20px;
    margin:60px 0;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
    transition:.3s;
}

.card:hover{
    transform:translateY(-5px);
}

.card h3{
    color:#2563eb;
    margin-bottom:10px;
}

.analytics{
    margin:60px 0;
}

.analytics h2{
    text-align:center;
    margin-bottom:30px;
}

.chart-container{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
    gap:25px;
}

.chart-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
}

.chart-title{
    margin-bottom:15px;
    font-weight:600;
}

.bar-chart{
    display:flex;
    align-items:flex-end;
    gap:15px;
    height:180px;
}

.bar{
    flex:1;
    border-radius:8px 8px 0 0;
    background:linear-gradient(to top,#2563eb,#60a5fa);
}

.b1{height:60%;}
.b2{height:90%;}
.b3{height:45%;}
.b4{height:100%;}
.b5{height:75%;}

.pie-chart{
    width:180px;
    height:180px;
    margin:auto;
    border-radius:50%;
    background:
    conic-gradient(
        #2563eb 0% 40%,
        #06b6d4 40% 70%,
        #8b5cf6 70% 100%
    );
}

.upload-section{
    background:white;
    padding:40px;
    border-radius:20px;
    text-align:center;
    box-shadow:0 5px 15px rgba(0,0,0,0.08);
    margin:60px 0;
}

.upload-section h2{
    margin-bottom:15px;
}

.upload-section p{
    margin-bottom:20px;
    color:#666;
}

input[type="file"]{
    padding:10px;
}

.cta{
    text-align:center;
    padding:60px 20px;
}

.cta h2{
    margin-bottom:15px;
}

.cta p{
    margin-bottom:25px;
}

.btn{
    background:#2563eb;
    color:white;
    text-decoration:none;
    padding:15px 35px;
    border-radius:50px;
    font-size:18px;
    transition:.3s;
}

.btn:hover{
    background:#1d4ed8;
}

footer{
    text-align:center;
    padding:25px;
    background:#111827;
    color:white;
    margin-top:50px;
}
</style>
</head>
<body>

<header>
    <h1>Insight Flow</h1>
    <p>
        Transform raw data into meaningful insights. Upload your files and
        instantly visualize data through interactive charts, graphs, and analytics dashboards.
    </p>
</header>

<div class="container">

    <section class="features">
        <div class="card">
            <h3>📁 Easy Upload</h3>
            <p>Upload CSV, Excel, or JSON files with a single click.</p>
        </div>

        <div class="card">
            <h3>📊 Smart Visualization</h3>
            <p>Generate bar charts, pie charts, line charts, and more automatically.</p>
        </div>

        <div class="card">
            <h3>⚡ Instant Insights</h3>
            <p>Analyze trends, patterns, and performance in seconds.</p>
        </div>

        <div class="card">
            <h3>📈 Interactive Dashboard</h3>
            <p>Explore your data through dynamic visual reports.</p>
        </div>
    </section>

    <section class="analytics">
        <h2>Sample Data Visualizations</h2>

        <div class="chart-container">

            <div class="chart-card">
                <div class="chart-title">Sales Performance (Bar Chart)</div>
                <div class="bar-chart">
                    <div class="bar b1"></div>
                    <div class="bar b2"></div>
                    <div class="bar b3"></div>
                    <div class="bar b4"></div>
                    <div class="bar b5"></div>
                </div>
            </div>

            <div class="chart-card">
                <div class="chart-title">Category Distribution (Pie Chart)</div>
                <div class="pie-chart"></div>
            </div>

        </div>
    </section>

    <section class="upload-section">
        <h2>Upload Your Data</h2>
        <p>
            Upload your dataset and Insight Flow will automatically analyze it
            and represent the information using multiple chart formats such as
            bar charts, pie charts, line graphs, and trend visualizations.
        </p>

        <input type="file">
    </section>

</div>

<section class="cta">
    <h2>Turn Data Into Actionable Insights</h2>
    <p>
        Start exploring your data and discover trends through beautiful visualizations.
    </p>

    <a href="#" class="btn">Get Started</a>
</section>

<footer>
    © 2026 Insight Flow | Data Analytics & Visualization Platform
</footer>

</body>
</html>
















































































































































































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
               


















                
                       
   
       
               

              
 
