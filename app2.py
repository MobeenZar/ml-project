import streamlit as st
from math_utils import add, subtract, multiply, divide

st.title("Simple Math Operations App")

num1 = st.number_input("Enter first number", value=0.0, key="num1")
num2 = st.number_input("Enter second number", value=0.0, key="num2")

operation = st.selectbox(
    "Choose operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.success(f"Result: {result}")
