import pandas as pd

data = pd.read_csv(r"/Users/syroppers/Documents/archive/covid_19_clean_complete.csv")
data.columns = data.columns.str.strip()
data['Date'] = pd.to_datetime(data['Date'])

def getHighestRatio():
    """Find country with highest deaths to confirmed cases ratio overall"""
    overall = data.groupby('Country/Region')[['Confirmed', 'Deaths']].sum()
    overall['Ratio'] = overall['Deaths'] / overall['Confirmed'].replace(0, 1)
    max_country = overall['Ratio'].idxmax()
    max_ratio = overall['Ratio'].max()
    return max_country, max_ratio

if __name__ == "__main__":
    max_country, max_ratio = getHighestRatio()
    print(f"Country with highest deaths to confirmed cases ratio overall: {max_country} (Ratio: {max_ratio:.4f})")