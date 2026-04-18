import pandas as pd

data = pd.read_cvs('avgIQpercountry.csv')

print(data)

first_rows = data.head(10)
print(first_rows)

last_rows = data.tail(10)
print(last_rows)
#sa tdhana prej fundit po dojna mi shfaq

