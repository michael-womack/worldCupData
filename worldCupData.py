import requests
import pandas as pd

# URL for the CSV data
csv_url = 'https://raw.githubusercontent.com/code-and-dogs/python-dsd--14pythonWorldCupCrawl/refs/heads/main/WorldCupData.csv'

# Fetch the CSV file from the URL
response = requests.get(csv_url)

# Check if the request was successful
if response.status_code == 200:
    print("CSV file fetched successfully!")
else:
    print("Failed to fetch the CSV file.")
    exit()

# Load the CSV data into pandas
from io import StringIO
csv_data = StringIO(response.text)
df = pd.read_csv(csv_data)

# Print the first few rows to inspect the data
print("Data preview:")
print(df.head())

# Filter and print the games where 'teamA' scored more than 'teamB'
print("\nGames where teamA scored more goals than teamB:")
filtered_data = df[df['goalsA'] > df['goalsB']]
print(filtered_data[['year', 'teamA', 'teamB', 'goalsA', 'goalsB']])

# You can also explore other basic operations like counting the number of occurrences
print("\nCount of games where 'teamA' is the winner:")
teamA_wins = df[df['winner'] == 'teamA']
print(f"TeamA wins: {teamA_wins.shape[0]}")

print("\nCount of games where 'teamB' is the winner:")
teamB_wins = df[df['winner'] == 'teamB']
print(f"TeamB wins: {teamB_wins.shape[0]}")