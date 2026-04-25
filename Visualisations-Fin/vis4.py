import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"/Users/syroppers/Documents/archive/covid_19_clean_complete.csv")
data.columns = data.columns.str.strip()
data['Date'] = pd.to_datetime(data['Date'])

def getTop10RatioChart():
    """View top 10 countries by deaths to confirmed ratio (bar chart)"""
    overall = data.groupby('Country/Region')[['Confirmed', 'Deaths']].sum()
    overall['Ratio'] = overall['Deaths'] / overall['Confirmed'].replace(0, 1)
    top10 = overall.sort_values('Ratio', ascending=False).head(10)
    
    plt.figure(figsize=(10, 6))
    plt.barh(top10.index, top10['Ratio'], color='steelblue')
    plt.xlabel('Deaths to Confirmed Cases Ratio')
    plt.ylabel('Country')
    plt.title('Top 10 Countries by Deaths to Confirmed Cases Ratio')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    getTop10RatioChart()