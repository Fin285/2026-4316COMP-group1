import pandas as pd

# Load data
data = pd.read_csv(r"/Users/syroppers/Documents/archive/covid_19_clean_complete.csv")
data.columns = data.columns.str.strip()
data['Date'] = pd.to_datetime(data['Date'])

def getTop5Confirmed():
    """Show top 5 countries with highest confirmed cases"""
    overall = data.groupby('Country/Region')['Confirmed'].sum()
    top5 = overall.sort_values(ascending=False).head(5)
    return list(top5.items())

# Run
if __name__ == "__main__":
    top5 = getTop5Confirmed()
    print("Top 5 countries with highest confirmed cases:")
    for rank, (country, cases) in enumerate(top5, start=1):
        print(f"  {rank}. {country}: {cases:,} cases")