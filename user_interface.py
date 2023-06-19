import streamlit as st
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv("elements.csv")

# Create a dictionary to map symbols to element information
elements = {
    row['symbol']: {
        'atomic_number': row['atomic_number'],
        'atomic_weight': row['atomic_weight'],
        'name': row['name'],
        'group': row['group'],
        'period': row['period']
    }
    for _, row in data.iterrows()
}

# Display the elements using buttons
st.title("Periodic Table of Elements")

# Define the number of rows and columns for the layout
num_rows = 10
num_cols = 18

# Create a grid layout for the elements
grid = st.container()
with grid:
    cols = st.columns(num_cols)
    for i in range(num_rows):
        for j in range(num_cols):
            index = i * num_cols + j
            if index < len(data):
                symbol = data.iloc[index]['symbol']
                with cols[j]:
                    if symbol in elements:
                        element_info = elements[symbol]
                        button_label = f"{symbol}\n{element_info['atomic_number']}"
                        button_tooltip = f"Name: {element_info['name']}\n" \
                                         f"Atomic Weight: {element_info['atomic_weight']}\n" \
                                         f"Group: {element_info['group']}\n" \
                                         f"Period: {element_info['period']}"
                        if st.button(button_label, help=button_tooltip):
                            st.info(button_tooltip)
                    else:
                        st.empty()
