# importing csv module
import pandas as pd
  
# initializing the titles and rows list
fields = []
rows = []

# reading csv file
df = pd.read_csv('Emp.csv')
#print(df)

intime = df['In-Time'].to_list()
#print(intime)

outtime = df['Out-Time'].to_list()
#print(outtime)

breakt = df['Break Time'].to_list()
print(breakt)

  



