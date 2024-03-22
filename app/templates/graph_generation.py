# graph_generation.py
import matplotlib
matplotlib.use('Agg')  # Set the backend to 'Agg' for headless environments
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import pandas as pd
import io

def generate_sales_graph(sales_data):
    df_sales = pd.DataFrame(sales_data)
    plt.figure(figsize=(10, 6))
    plt.bar(df_sales['Category'], df_sales['Percentage'], color='skyblue')
    plt.title('Domestic Sales Distribution')
    plt.xlabel('Category')
    plt.ylabel('Percentage')
    plt.xticks(rotation=45)
    plt.tight_layout()
    buf = io.BytesIO()  # Create a buffer to hold the image in memory
    plt.savefig(buf, format='png')  # Save the figure to the buffer
    plt.close()
    buf.seek(0)  # Seek to the start of the buffer
    return buf

