## ==== Data Frames with Pandas ==== ##
import pandas as pd

df = pd.read_csv("./data/amazon_laptop_prices_v01.csv")


if __name__ == "__main__":
  print(df.head(5))
  list_products = df.head(20)
  print(list_products)
