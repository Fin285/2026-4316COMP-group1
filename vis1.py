import pandas as pd

# Load data
data = pd.read_csv(r"/Users/syroppers/Documents/archive/covid_19_clean_complete.csv")
data.columns = data.columns.str.strip()
data['Date'] = pd.to_datetime(data['Date'])

def getDeathsPerMonth(month):
    """Find country with most deaths in a specific month"""
    filtered = data[data['Date'].dt.month == month]
    deaths_by_country = filtered.groupby('Country/Region')['Deaths'].sum()
    top3 = deaths_by_country.sort_values(ascending=False).head(3)
    return list(top3.items())

# Run for user input
if __name__ == "__main__":
    month_input = input("Enter a month (1-12 or month name e.g. January): ").strip()
    try:
        if month_input.isdigit():
            month = int(month_input)
        else:
            month = pd.to_datetime(month_input, format='%B').month
        top_countries = getDeathsPerMonth(month)
        print(f"Top 3 countries with most deaths in month {month}:")
        for rank, (country, deaths) in enumerate(top_countries, start=1):
            print(f"  {rank}. {country}: {deaths} deaths")
    except:
        print("Invalid month input")