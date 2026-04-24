import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('vgsales.csv')
# print(df.head(5))

# info

# print(df.isna().sum())
# change null Year with avg year
df_new = df.copy()
df_new['Year'] = df_new['Year'].fillna(int(df_new['Year'].mean()))

# print(df_new.head(5))


# drop null publisher
df_new.dropna(subset=['Publisher'], inplace=True)
# print(df_new.isna().sum())

# duplicates
# print(df_new.duplicated().sum())


# compare total sales of ps2 in all regions using [pie chart]
# ps2_data = df_new[df_new['Platform'] == 'PS2']
# ps2_sales = ps2_data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
# # print(ps2_sales)

# labels = ps2_sales.index
# sizes = ps2_sales.values
# plt.figure(figsize=(8, 6))
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# plt.title('Total Sales of PS2 in Different Regions')
# plt.show()


# top 5 publishers in na sales using [bar plot]
# top_publishers = df_new.groupby('Publisher')['NA_Sales'].sum().nlargest(5)
# # print(top_publishers)

# plt.figure(figsize=(10, 6))
# sns.barplot(x=top_publishers.index, y=top_publishers.values, palette='viridis')
# plt.title('Top 5 Publishers in NA Sales')
# plt.xlabel('Publisher')
# plt.ylabel('Total NA Sales (in millions)')
# plt.show()


# # top 1 best selling games per year world wide using [line plot]

# df_new['Total_Sales'] = df_new[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum(axis=1)
# best_selling_games = df_new.loc[df_new.groupby('Year')['Total_Sales'].idxmax()]
# # print(best_selling_games[['Year', 'Name', 'Total_Sales']])
# plt.figure(figsize=(12, 6))
# sns.lineplot(data=best_selling_games, x='Year', y='Total_Sales', marker='o')
# plt.title('Best Selling Games Per Year Worldwide')
# plt.xlabel('Year')
# plt.ylabel('Total Sales (in millions)')
# plt.show()


# genre popularity in japan using [histogram]
# japan_genre_sales = df_new.groupby('Genre')['JP_Sales'].sum().sort_values(ascending=False)
# # print(japan_genre_sales)
# plt.figure(figsize=(12, 6))
# sns.barplot(x=japan_genre_sales.index, y=japan_genre_sales.values, palette='magma')
# plt.title('Genre Popularity in Japan')
# plt.xlabel('Genre')
# plt.ylabel('Total JP Sales (in millions)')
# plt.xticks(rotation=45)
# plt.show()

# least popular genre in europe using [bar plot]
# europe_genre_sales = df_new.groupby('Genre')['EU_Sales'].sum().sort_values()
# # print(europe_genre_sales)
# plt.figure(figsize=(12, 6))
# sns.barplot(x=europe_genre_sales.index, y=europe_genre_sales.values, palette='coolwarm')
# plt.title('Least Popular Genre in Europe')
# plt.xlabel('Genre')
# plt.ylabel('Total EU Sales (in millions)')
# plt.xticks(rotation=45)
# plt.show()


