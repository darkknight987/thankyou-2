import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
df = pd.read_csv(r"D:\NISHANT\COLLEGE\F.Y MSC Practicals\BUISSNESS INTELLIGENCE\PRAC7\GroceryStoreDataSet.csv", names = ['products'], sep = ',')
df.head()
df.shape
data = list(df["products"].apply(lambda x:x.split(",") ))
print(data)
a = TransactionEncoder()
a_data = a.fit(data).transform(data)
df = pd.DataFrame(a_data,columns=a.columns_)
df = df.replace(False,0)
print(df)
df = apriori(df, min_support = 0.2, use_colnames = True, verbose = 1)
print(df)
df_ar = association_rules(df, metric = "confidence", min_threshold = 0.6)
print(df_ar)