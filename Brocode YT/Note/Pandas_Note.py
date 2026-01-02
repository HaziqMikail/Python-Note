import pandas as pd

# #?----------------------------------------------
# #? Series = 1D labeled array
# #?----------------------------------------------

# data = [10, 20, 30, 40]
# series = pd.Series(data, index=['apartment1', 'apartment2', 'apartment3', 'apartment4']) #index to label each element

# print(series)
# # Output:
# # apartment1    10   
# # apartment2    20
# # apartment3    30   
# # apartment4    40
# # dtype: int64

# series.loc['apartment3'] = 35     #? modifying element by label
# print(series)
# print(series.loc['apartment2'])   #? accessing element by label
# # Output: 20
# print(series[series > 20])        #? filtering elements greater than 20

# #? Creating Series from dictionary
# calories = {'day1': 2000, 
#             'day2': 2200, 
#             'day3': 2500}

# series = pd.Series(calories)  #?create series from dictionary
# series.loc["day1"] = 2100     #!modify element by label
# series.iloc[1] = 2300         #*modify element by integer location

# print(series["day1"])
# print(series[series > 2100]) #?filtering elements greater than 2100


# #?----------------------------------------------
# #? DataFrame = 2D labeled data structure (like a table)
# #?----------------------------------------------

# data = {"Name": ['John', 'Anna', 'Peter', 'Linda'],
#         "Age": [28, 24, 35, 32]}

# df = pd.DataFrame(data, index=['person1', 'person2', 'person3', 'person4']) #? create DataFrame from dictionary with custom index
# print(df)
# print(df.loc['person2'])   #? access row by label
# print(df.iloc[0])          #? access row by integer location

# #?adding new column
# df['job'] = ['Engineer', 'Doctor', 'Artist', 'Lawyer']
# print(df)

# #?adding new rows by concatenation
# new_persons = pd.DataFrame([{'Name': 'Mike', 'Age': 30, 'job': 'Chef'},
#                            {'Name': 'Michael', 'Age': 40, 'job': 'Waiter'}], 
#                            index=['person5', 'person6'])
# df = pd.concat([df, new_persons])
# print(df)


# #?----------------------------------------------
# #? Importing and Exporting Data
# #?----------------------------------------------

# # import data from CSV file
# df = pd.read_csv('pokemon.csv') 

# # import json file
# df = pd.read_json('pokemon.json') 
# print(df) #print entire DataFrame
# print(df.to_string())  #print entire DataFrame without truncation
# print(df.head(10))  #print first 10 rows
# print(df.tail(5))   #print last 5 rows



# #? ------------------------------------------------------
# #? Selection in DataFrames
# #? ------------------------------------------------------

# Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary

#TODO ----------------------------------------------------------------------
#TODO - Read pokemon.csv file and perform various DataFrame operations
df = pd.read_csv('pokemon.csv',index_col='Name',) #?set 'Name' column as index to access rows by pokemon name

pokemon = input("Enter Pokemon Name: ")

try:
    print(df.loc[pokemon].to_string()) #select row by label, to_string() to print entire row
except KeyError:
    print(f"{pokemon} not found.")
#TODO ----------------------------------------------------------------------

# print(df['Type 1'].value_counts())     #?count occurrences of each unique value in 'Type 1' column
# print(df['Generation'].unique())       #?get unique values in 'Generation' column
# print(df['Generation'].nunique())      #?get number of unique values in 'Generation'
# print(df.columns)                      #?get list of column names

# #? select specific columns
# print(df[['Name', 'Type 1', 'HP']].to_string())

# #? selection by rows
# print(df.loc["Latias", ["Type 1", "Type 2", "Generation"]].to_string())               #?select row by label
# print(df.loc["Bulbasaur" : "Pidgey", ["Type 1", "Type 2", "Generation"]].to_string()) #?select range of rows by label
# print(df.iloc[0:5:2, 0:3].to_string())                        #?select range of rows and columns by integer location

#TODO loc vs iloc
#? loc: label-based indexing, includes the last element in range
#? iloc: integer position-based indexing, excludes the last element in range


# #? ------------------------------------------------------
# #? Filtering DataFrames = conditions to filter rows
# #? ------------------------------------------------------

# df = pd.read_csv('pokemon.csv')

# high_attack = df[df['Attack'] > 100]              #?filter rows where Attack > 100
# legendary_pokemon = df[df['Legendary'] == True]   #?filter rows where Legendary is True

# water_type = df[(df['Type 1'] == 'Water') | (
#              df['Type 2'] == 'Water')]            #?filter rows where Type 1 or Type 2 is Water

# print(water_type.to_string()) 



# #? ------------------------------------------------------
# #? Agregating DataFrames = perform calculations on data
# #? ------------------------------------------------------

# df = pd.read_csv('pokemon.csv')

# #? group by and calculate statistics
# group = df.groupby('Type 1')   #?group by Type 1 column
# print(group["HP"].max())       #?calculate max HP for each Type 1 group
# print(group["Attack"].mean())  #?calculate mean Attack for each Type 1 group
# print(group["Speed"].sum())    #?calculate sum of Speed for each Type 1 group

# #? whole DataFrame statistics
# print(df.mean(numeric_only=True))  #calculate mean of numeric columns
# print(df.sum(numeric_only=True))  #calculate sum of numeric columns
# print(df.min(numeric_only=True))  #calculate min of numeric columns
# print(df.max(numeric_only=True))  #calculate max of numeric columns
# print(df.count(numeric_only=True))  #calculate count of numeric columns

# #? single column statistics, need to add column name in brackets
# print(df['HP'].mean())  #calculate mean of HP column
# print(df['Attack'].sum())  #calculate sum of Attack column


# #? ------------------------------------------------------
# #? Data Cleaning = handle missing or inconsistent data
# #? ------------------------------------------------------

# df = pd.read_csv('pokemon.csv')

# #? 1. drop irrelevant columns
# df = df.drop(columns=["Legendary", "HP"])

# #? 2. Drop irrelevant data
# df = df.dropna(subset=['Type 2'])   #? drop rows where Type 2 is NaN
# df = df.fillna({'Type 2': 'None'})  #? fill NaN in Type 2 with 'None'

# #? 3. fix inconsistent data
# df['Type 1'] = df['Type 1'].replace({'Fire': 'FIRE',
#                                      'Water': 'WATER',
#                                      'Grass': 'GRASS'})  #? change value in Type 1 column

# #? 4. standardize text data
# df["Name"] = df["Name"].str.lower()           #? convert Name column to lowercase
# df["Type 1"] = df["Type 1"].str.capitalize()  #? capitalize first letter of Type 1 column

# #? 5. fix data types
# df["Legendary"] = df["Legendary"].astype(bool)  #? convert Legendary column to boolean type

# #? 6. remove duplicates
# df = df.drop_duplicates()  #? remove duplicate rows

# print(df.to_string())










































