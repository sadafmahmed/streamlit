import streamlit as st

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Division by zero error"
        else:
            return num1 / num2

def main():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

    operator = st.selectbox("Select operation", ["+", "-", "*", "/"])

    result = calculate(num1, num2, operator)

    st.write("Result:", result)

if __name__ == "__main__":
    main()
