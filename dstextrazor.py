import dstextrazor
import streamlit as st

def textrazoroutput():
    st.title("Simple Calculator App")

    num1 = st.number_input("Enter first number:")
    num2 = st.number_input("Enter second number:")

    operations = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    if st.button("Calculate"):
        if operations == "Addition":
            result = num1 + num2
            st.success(f"The result of {num1} + {num2} is {result}")
        elif operations == "Subtraction":
            result = num1 - num2
            st.success(f"The result of {num1} - {num2} is {result}")
        elif operations == "Multiplication":
            result = num1 * num2
            st.success(f"The result of {num1} x {num2} is {result}")
        else:
            if num2==0:
                st.error("Cannot divide by zero")
            else:
                result = num1 / num2
                st.success(f"The result of {num1} / {num2} is {result}")


if __name__=="__main__":
    textrazoroutput()
