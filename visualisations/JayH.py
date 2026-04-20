import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.style.use('_mpl-gallery')

def first_case_dates(df):
    first_cases = df[df['Confirmed'] > 0].groupby('Country/Region')['Date'].min().reset_index()

    x = first_cases['Date'].map(pd.Timestamp.toordinal)
    y = np.arange(len(first_cases))
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    ax.set(
        title="First COVID Case by Country",
        xlabel="Date",
        ylabel="Country Index"
    )

    plt.show()
