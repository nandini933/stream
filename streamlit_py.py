# -*- coding: utf-8 -*-
"""streamlit.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17BHRyZQwzuEExOHUd5QPXNK0RIk3UFmS
"""

pip install streamlit

pip install numpy

pip install pandas

import streamlit as st
import pandas as pd
import numpy as np

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Number")

    st.write("Enter three numbers:")
    a = st.number_input("Number 1")
    b = st.number_input("Number 2")
    c = st.number_input("Number 3")

    if st.button("Find Largest"):
        largest = find_largest(a, b, c)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()