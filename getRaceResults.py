import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

# take in the link to get results from, and the csv name INCLUDING the .csv extension
def raceResults(link, csvName):
    # Making a GET request
    data = requests.get(link).text

    # Make a soup object of the html
    soup = BeautifulSoup(data, 'html.parser')

    # Extract just the desired table
    table = soup.find('table', class_='responsive-table')

    # Get Table Headers
    col = []
    for th in table.thead.find_all('th'):
        col.append(th.text)

    # Create and fill the Dataframe
    df = pd.DataFrame(columns=col)

    # Each rider is a 'tr' in the html table
    for i, tr in enumerate(table.find_all('tr')):
        # 'i' is race position
        rows = [i]
        # Each additional piece of data is a 'td'
        for td in tr.find_all('td'):
            rows.append(td.text)
        # Append a row to the Dataframe
        if i > 0:
            df.loc[i-1] = rows

    # Output Race Results to a CSV
    df.to_csv(csvName, index = False)



