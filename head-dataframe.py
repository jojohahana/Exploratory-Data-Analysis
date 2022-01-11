#check bagaimana contoh data dari dataframe tersebut dengan fungsi head dengan limit 10 baris!

import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.head(10))


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe(include="all"))
# Median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median)