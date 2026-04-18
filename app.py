import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Page Config
st.set_page_config(page_title="Crop Auditor", layout="wide")
st.title("🌾 Satellite Data Auditor")

# 2. NumPy Logic: Create the Field
st.subheader("Satellite Grid Analysis")
field = np.random.randint(0, 100, size=(100, 100)) # Smaller for speed

# Display Heatmap
fig, ax = plt.subplots()
cax = ax.imshow(field, cmap='RdYlGn')
fig.colorbar(cax)
st.pyplot(fig)

# 3. Pandas Logic: The Audit Table
st.subheader("Field Audit Results")
data = {
    'Plot_ID': ['Plot A', 'Plot B', 'Plot C', 'Plot D'],
    'Area': [50, 120, 80, 200],
    'Greenness': [85, 42, 78, 25]
}
df = pd.DataFrame(data)
df['Predicted_Yield'] = df['Area'] * (df['Greenness'] / 100)

# 4. Custom Quick Sort Logic
def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    return quick_sort([x for x in arr if x > pivot]) + [x for x in arr if x == pivot] + quick_sort([x for x in arr if x < pivot])

# Sort and display
sorted_yields = quick_sort(df['Predicted_Yield'].tolist())
st.write("Ranked Yields (High to Low):", sorted_yields)
st.dataframe(df) # Shows an interactive table on your website

