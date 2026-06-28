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



import plotly.express as px

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Insight Flow",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>
.main-header{
    text-align:center;
    padding:20px;
}

.title{
    font-size:52px;
    font-weight:bold;
    color:#1E88E5;
}

.subtitle{
    font-size:20px;
    color:gray;
}

.upload-box{
    border:2px dashed #1E88E5;
    border-radius:15px;
    padding:30px;
    text-align:center;
    background-color:#f8fbff;
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:20px;
    font-weight:bold;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.markdown("""
<div class="main-header">
    <div class="title">📊 Insight Flow</div>
    <div class="subtitle">
        Transform your CSV/XLSX data into powerful visual insights
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------
# Upload Section
# ---------------------------
st.markdown("""
<div class="upload-box">
    <h3>📂 Upload CSV / XLSX File</h3>
    <p>Get your data automatically visualized into various charts and dashboards.</p>
</div>
""", unsafe_allow_html=True)



st.write("---")

# ---------------------------
# Sample Charts Section
# ---------------------------
st.subheader("📈 Dashboard Preview")

col1, col2 = st.columns(2)

# Sample Data
np.random.seed(42)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = pd.DataFrame({
    "Month": months,
    "Revenue": np.random.randint(1000, 5000, 6)
})

products = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Sales": [35, 25, 20, 20]
})

with col1:
    st.markdown("### Revenue Trend")
    fig1 = px.line(
        sales,
        x="Month",
        y="Revenue",
        markers=True,
        template="plotly_white"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.markdown("### Sales Distribution")
    fig2 = px.pie(
        products,
        names="Category",
        values="Sales",
        hole=0.4
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# More Preview Charts
# ---------------------------
col3, col4 = st.columns(2)

with col3:
    fig3 = px.bar(
        sales,
        x="Month",
        y="Revenue",
        color="Revenue",
        template="plotly_white"
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    scatter_data = pd.DataFrame({
        "X": np.random.randint(1, 100, 50),
        "Y": np.random.randint(1, 100, 50)
    })

    fig4 = px.scatter(
        scatter_data,
        x="X",
        y="Y",
        template="plotly_white"
    )
    st.plotly_chart(fig4, use_container_width=True)

st.write("---")

# ---------------------------
# Features
# ---------------------------
st.subheader("✨ What Insight Flow Offers")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("📊 Automatic Chart Generation")

with c2:
    st.info("📈 Interactive Dashboards")

with c3:
    st.info("📑 CSV & Excel Data Analysis")

st.write("")
st.write("")

# ---------------------------
# Get Started Button
# ---------------------------
if st.button("🚀 Get Started"):
    st.success(
        "Upload a CSV/XLSX file and start exploring insights through multiple visualizations!"
    )


































































































































































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
               


















                
                       
   
       
               

              
 
