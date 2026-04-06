import pandas as pd

df = pd.read_csv('bestsellers.csv')

print(df.head(5))

print("Shape of the dataset:", df.shape)
print("Columns in the dataset:", df.columns)
print("Summary statistics of the dataset:\n", df.describe())
print()
print()

#Cleaning the dataset
df.dropna(inplace=True)  # Remove any rows with missing values
df.drop_duplicates(inplace=True)  # Remove duplicate rows

#Renamin columns for better readability
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#Converting data types
df['Price'] = df['Price'].astype(float)

#Which Author have how many books in the bestsellers list?
author_count = df["Author"].value_counts()
print(author_count)
print()

## Average Rating by Genre
average_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(average_rating_by_genre)

#Export the top 10 best-selling books to a new CSV file
author_count.head(10).to_csv('outputs/top_authors.csv',header=True)

# Export average rating by genre to a CSV file
average_rating_by_genre.to_csv('outputs/average_rating_by_genre.csv', header=True)