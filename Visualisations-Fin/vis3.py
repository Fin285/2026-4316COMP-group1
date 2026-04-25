import pandas as pd

data = pd.read_csv(r"/Users/syroppers/Documents/archive/covid_19_clean_complete.csv")
data.columns = data.columns.str.strip()
data['Date'] = pd.to_datetime(data['Date'])

def getHighestDay():
    """Find the day with the most confirmed cases"""
    confirmed_by_date = data.groupby('Date')['Confirmed'].sum()
    max_date = confirmed_by_date.idxmax()
    max_cases = confirmed_by_date.max()
    return max_date, max_cases

if __name__ == "__main__":
    max_date, max_cases = getHighestDay()
    print(f"Day with the most confirmed cases: {max_date.strftime('%Y-%m-%d')} ({max_cases} cases)")