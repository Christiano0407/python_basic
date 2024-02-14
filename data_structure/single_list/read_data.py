#####
#* ===== Data Base =====
#####
import pandas as pd
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "../../data", "mcu_box_office.csv")
df = pd.read_csv(file_path)

print(df)