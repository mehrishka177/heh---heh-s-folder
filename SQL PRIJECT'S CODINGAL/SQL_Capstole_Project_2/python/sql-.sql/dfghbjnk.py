import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'age': [25, 30, 35, 40]
})

# Perform an inner join (only common rows)
inner_join = pd.merge(df1, df2, on='id', how='inner')
print("Inner Join:")
print(inner_join)

# Perform a left join (all rows from df1 and matching rows from df2)
left_join = pd.merge(df1, df2, on='id', how='left')
print("\nLeft Join:")
print(left_join)

# Perform a right join (all rows from df2 and matching rows from df1)
right_join = pd.merge(df1, df2, on='id', how='right')
print("\nRight Join:")
print(right_join)

# Perform an outer join (all rows from both dataframes)
outer_join = pd.merge(df1, df2, on='id', how='outer')
print("\nOuter Join:")
print(outer_join)
