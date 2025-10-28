# Coffee Sales Analysis — Project Report
# Objective
 
The objective of this project is to analyze coffee sales transaction data from a vending machine to uncover customer purchasing patterns, peak sales periods, and product performance trends.
Additionally, a Machine Learning model is developed to predict sales revenue and assist in inventory management and marketing decisions.


# Dataset Overview

•	Dataset Name: index.csv

•	Total Records: 1,133 transactions

•	Time Period: March 2024 – July 2024

•	Source: Open dataset (Kaggle / Google Drive)

•	Key Columns:

o	date – Transaction date

o	datetime – Exact timestamp

o	cash_type – Payment method (card/cash)

o	card – Unique card number (if applicable)

o	money – Amount spent

o	coffee_name – Type of coffee purchased

This dataset captures daily transaction-level data and enables time-based and product-level analysis.

# Data Cleaning and Preparation

The dataset was carefully cleaned and prepared for analysis:

•	Converted date and datetime to proper datetime format.

•	Created new columns:

o	month – Monthly period

o	dayofweek – Day name (e.g., Monday, Tuesday)

o	hour – Hour extracted from timestamp

o	is_card – Binary flag for payment method (1 = Card, 0 = Cash)

•	Removed leading/trailing spaces from product names.

•	Verified there were no duplicate rows.

•	Handled missing card details (all missing values corresponded to cash transactions).

After cleaning, the data was fully consistent and ready for analysis.


# Exploratory Data Analysis (EDA)

➤ Top Selling Products

•	Top 3: Latte, Americano with Milk, and Cappuccino.

•	Lowest: Espresso and Cocoa.

•	The most popular drinks are milk-based coffees, indicating customer preference for creamy flavors.

➤ Monthly Sales Trend

•	Sales steadily increased from March to July 2024.

•	Latte and Americano with Milk show upward trajectories.

•	Cocoa and Espresso had lower and flatter sales patterns.

•	These patterns suggest growing demand for premium coffee types as the months progress.


➤ Weekly Revenue

•	Weekly sales analysis revealed consistent patterns with mid-month weeks showing the highest revenues.

•	Latte and Cappuccino dominate most weeks.

•	A stacked bar chart showed the contribution of each coffee type to total weekly sales.


➤ Hourly Sales Insights

•	Two major peak hours were identified each day:

o	10:00 AM → Morning rush hour

o	7:00 PM → Evening refreshment time

•	Morning: Dominated by Latte and Americano with Milk.

•	Evening: Hot Chocolate, Cappuccino, and Cocoa sell more.

These patterns indicate the importance of timing in restocking and marketing strategies.

➤ Product-wise Hourly Pattern

Each product shows unique sales behavior:

•	Latte & Americano with Milk: Strong morning demand.

•	Cappuccino & Cocoa: Preferred during the evening hours.

•	Hot Chocolate: Evening favorite, especially after 6 PM.

•	Espresso: Moderate sales across the day, niche preference.

These insights can help optimize supply chain scheduling and promotion timing.

# Machine Learning Model

A Random Forest Regressor model was developed to predict transaction value (money) based on:

•	coffee_name

•	hour

•	dayofweek

•	is_card

 # Model Steps:

•	Encoding: OneHotEncoder was used for categorical variables.

•	Data Split: 80% training, 20% testing.

•	Goal: Predict future transaction values and daily/weekly sales revenue.

The model performed efficiently and could be extended for sales forecasting and inventory prediction.


# Key Insights
 
•	92% of transactions were made using card payments.

•	Latte is the highest revenue-generating product.

•	 Sales peak around 10 AM and 7 PM daily.

•	Tuesday shows the highest overall sales volume.

•Evening customers prefer sweeter and richer drinks like Hot Chocolate.

# Business Recommendations
 
Based on the analysis, the following actions are recommended:

1.	Stock popular items (Latte, Americano with Milk) heavily in the morning.
   
2.	Promote evening drinks (Cappuccino, Cocoa, Hot Chocolate) with offers between 6–8 PM.
  
3.	Implement loyalty programs for frequent card users.
   
4.	Plan refills and maintenance after 7 PM to prepare for next-day peaks.
   
5.	Use the machine learning model to forecast next day/week sales for inventory optimization.

# Conclusion
 
The Coffee Sales Data Analysis project successfully identified:

•	Clear daily and weekly sales patterns

•	Product-specific demand cycles

•	A strong correlation between time of day and product preference


