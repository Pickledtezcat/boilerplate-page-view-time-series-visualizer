import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True)
#print(df.head())

df.set_index("date", inplace = True)
df = df.sort_values(['date', 'value'],ascending=False)

bottom = df["value"].quantile(0.025)
top = df["value"].quantile(0.975)

df = df[(df.value > bottom) | (df.value < top)]
#print (df.head())
#testing


def draw_line_plot():
    # Draw line plot
    df.plot(x = "date", y = "value")
    fig, ax = plt.subplots(figsize=(15, 7))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    #return fig
    

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    #fig.savefig('bar_plot.png')
    #return fig
    pass

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    #df_box = df.copy()
    #df_box.reset_index(inplace=True)
    #df_box['year'] = [d.year for d in df_box.date]
    #df_box['month'] = [d.strftime('%b') for d in #df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    #fig.savefig('box_plot.png')
    #return fig
    pass
