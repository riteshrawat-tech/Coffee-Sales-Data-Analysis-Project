
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\HP\Downloads\index.csv')
print(df.head)
print(df.info)
df.duplicated().sum()
df.describe().T

df['date'] = pd.to_datetime(df['date'])
df['datetime'] = pd.to_datetime(df['datetime'])
df['coffee_name'] = df['coffee_name'].str.strip()
df['is_card'] = (df['cash_type'].str.lower() == 'card').astype(int)
df.isnull().sum()

df['month'] = df['date'].dt.to_period('M').astype(str)
df['dayofweek'] = df['date'].dt.day_name()
df['hour'] = df['datetime'].dt.hour




# Top 8 coffee products
sns.countplot(data=df, x='coffee_name', order=df['coffee_name'].value_counts().index)
plt.xticks(rotation=45)
plt.title("Top Coffee Products Sold")

# Hourly pattern
sns.histplot(df['hour'], bins=24)
plt.title("Transactions by Hour of Day")

# Payment type
df['cash_type'].value_counts(normalize=True).plot(kind='pie', autopct='%1.1f%%')
plt.title("Card vs Cash Payments")
plt.show()

daily = df.groupby('date')['money'].sum().reset_index()
daily.rename(columns={'money':'daily_sales'}, inplace=True)


from sklearn.preprocessing import OneHotEncoder
import sklearn  
import pandas as pd

# Extract relevant columns
X = df[['coffee_name', 'hour', 'dayofweek', 'is_card']]

# Detect sklearn version
version = sklearn.__version__
major, minor, *_ = map(int, version.split("."))

# Choose correct parameter based on version
if major >= 1 and minor >= 4:
    ohe = OneHotEncoder(sparse_output=False, drop='first')
else:
    ohe = OneHotEncoder(sparse=False, drop='first')

# Fit & transform
X_ohe = ohe.fit_transform(X[['coffee_name', 'dayofweek']])

# DataFrame of encoded columns
X_ohe_df = pd.DataFrame(
    X_ohe,
    columns=ohe.get_feature_names_out(['coffee_name', 'dayofweek']),
    index=X.index
)

# Combine with numeric features
X_final = pd.concat(
    [X[['hour', 'is_card']].reset_index(drop=True),
     X_ohe_df.reset_index(drop=True)],
    axis=1
)

# Target variable
y = df['money']

print(" One-hot encoding completed successfully")
print("Shape of X_final:", X_final.shape)
print("Columns:", X_final.columns.tolist())

# Machine lerning Import
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Train-Test Split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X_final, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print(" Model training and prediction completed")


# NOW YOU CAN PLOT
# Daily Sales Plot
plt.figure(figsize=(10,5))
plt.plot(daily['date'], daily['daily_sales'], label='Daily Sales')
plt.title("Daily Coffee Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales (₹)")
plt.legend()
plt.show()

# Actual vs Predicted Plot
plt.figure(figsize=(8,5))
plt.plot(y_test.values, label='Actual', marker='o')
plt.plot(y_pred, label='Predicted', marker='x')
plt.title("Actual vs Predicted Transaction Amount")
plt.xlabel("Samples")  
plt.ylabel("Transaction Amount (₹)")  
plt.legend()
plt.show()

# Overall Revenue by Product
revenue_by_product = df.groupby('coffee_name')['money'].sum().sort_values(ascending=False)

# Display the results
print("Overall Revenue by Coffee Product:")
print(revenue_by_product)

#  Revenue the top products
plt.figure(figsize=(10,5))
revenue_by_product.head(10).plot(kind='bar', color='saddlebrown')
plt.title("Top 10 Coffee Products by Total Revenue")
plt.xlabel("Coffee Product")
plt.ylabel("Total Revenue (₹)")
plt.xticks(rotation=45)
plt.show()


# Group by month and coffee_name
monthly_product_sales = df.groupby(['month', 'coffee_name'])['money'].sum().reset_index()

#  Convert month to datetime and sort
monthly_product_sales['month'] = pd.to_datetime(monthly_product_sales['month'])
monthly_product_sales = monthly_product_sales.sort_values('month')

# Pivot data — each coffee becomes a separate column
pivot_data = monthly_product_sales.pivot(index='month', columns='coffee_name', values='money').fillna(0)

#Plot all products in one line chart
plt.figure(figsize=(12,6))
for column in pivot_data.columns:
    plt.plot(pivot_data.index, pivot_data[column], marker='o', linewidth=2, label=column)

plt.title("Monthly Revenue Trend by Coffee Product", fontsize=15)
plt.xlabel("Month")
plt.ylabel("Total Revenue (₹)")
plt.legend(title="Coffee Name", bbox_to_anchor=(1.05, 1), loc='upper left')  
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Create a 'week' column (from 'date')
df['week'] = df['date'].dt.to_period('W').astype(str)

# Group by week and coffee product
weekly_sales = df.groupby(['week', 'coffee_name'])['money'].sum().reset_index()

# Pivot data so each coffee is a column
pivot_weekly = weekly_sales.pivot(index='week', columns='coffee_name', values='money').fillna(0)

# Plot stacked bar chart
pivot_weekly.plot(kind='bar',stacked=True,figsize=(12,6),colormap='tab20'   )

plt.title("Weekly Revenue by Coffee Product", fontsize=15)
plt.xlabel("Week")
plt.ylabel("Total Revenue (₹)")
plt.xticks(rotation=45)
plt.legend(title="Coffee Product", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#  Set figure size
plt.figure(figsize=(12,6))

# Plot histogram using seaborn
sns.histplot(data=df,x='hour',hue='coffee_name',multiple='stack',bins=24,palette='tab20')

#Chart formatting
plt.title("Hourly Sales Distribution by Coffee Product", fontsize=15)
plt.xlabel("Hour of Day")
plt.ylabel("Number of Transactions")
plt.xticks(range(0, 24))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()






