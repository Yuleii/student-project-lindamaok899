"""This module contains auxiliary function which we use in the example notebook."""

import pandas as pd
import numpy as np
from IPython.display import display,HTML
import matplotlib.pyplot as plt
import seaborn as sns


def multi_column_df_display(list_dfs, cols=3):

    """Print tables side by side.

    """

    html_table = "<table style='width:100%; border:0px'>{content}</table>"
    html_row = "<tr style='border:0px'>{content}</tr>"
    html_cell = "<td style='width:{width}%;vertical-align:top;border:0px'>{{content}}</td>"
    html_cell = html_cell.format(width=100/cols)

    cells = [ html_cell.format(content=df.to_html()) for df in list_dfs ]
    cells += (cols - (len(list_dfs)%cols)) * [html_cell.format(content="")] # pad
    rows = [ html_row.format(content="".join(cells[i:i+cols])) for i in range(0,len(cells),cols)]
    display(HTML(html_table.format(content="".join(rows))))




def plot_bars(df_unindexed, ax):
    choice_names = ['Schooling', 'Home', 'White', 'Blue', 'Military']

    plt.figure(figsize=[16,8])

    for i, name in enumerate(choice_names):

        df_unindexed[name] = (df_unindexed['Choice'] == name).astype(float)

        plt.subplot(2,3,i+1)

        if i in ['Schooling', 'Home', 'White']:

             sns.barplot(y=name, x='Period', data=df_unindexed, color=sns.color_palette()[i])
        else:
             sns.barplot(y=name, x='Period', data=df_unindexed, color=sns.color_palette()[i])

        ax.set_ylim(0, 1)
        plt.tight_layout()

    plt.tight_layout()


def period_pairs_rows(combined):

    period_pairs = np.arange(10).reshape(5, 2).tolist()
    fig, axes = plt.subplots(2, 3, figsize=(18, 8), )

    for i, (pair, ax) in enumerate(zip(period_pairs, axes.reshape(-1))):
        period_df = combined.query('Period in {}'.format(pair))
        tab_rows = (pd.crosstab(index=period_df['Choice'], columns=period_df['NextChoice'], normalize='index') * 100).round(1)
        if i in [2, 4]:
            sns.heatmap(tab_rows, cmap='Blues', vmin=0, vmax=90, annot=True, ax=ax)
        else:
            sns.heatmap(tab_rows, cmap='Blues', vmin=0, vmax=90, annot=True, ax=ax, cbar=False)


        ax.set_title('Period in {}'.format(pair))
        plt.tight_layout()

    axes.reshape(-1)[-1].remove()
    plt.tight_layout()


def period_pairs_cols(combined):
    period_pairs = np.arange(10).reshape(5, 2).tolist()
    fig, axes = plt.subplots(2, 3, figsize=(18, 8), )

    for i, (pair, ax) in enumerate(zip(period_pairs, axes.reshape(-1))):
        period_df = combined.query('Period in {}'.format(pair))
        tab_cols = (pd.crosstab(index=period_df['Choice'], columns=period_df['NextChoice'], normalize='columns') * 100).round(1)
        if i in [2, 4]:
            sns.heatmap(tab_cols, cmap='Blues', vmin=0, vmax=90, annot=True, ax=ax)
        else:
            sns.heatmap(tab_cols, cmap='Blues', vmin=0, vmax=90, annot=True, ax=ax, cbar=False)


        ax.set_title('Period in {}'.format(pair))
        plt.tight_layout()

    axes.reshape(-1)[-1].remove()
    plt.tight_layout()


def choice_dist(table):
    stacked_data = table.stack().reset_index().rename(columns={0:'value'})

    #plot only age excluding the share of individuals per choice to visualise the withing age distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=stacked_data.Age.iloc[0:66], y=stacked_data.value, hue=stacked_data.Choice)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()


def occupational_choice(tab):
    fig, ax = plt.subplots(figsize=(10, 6))
    stacked = tab.stack().reset_index().rename(columns={0:'value'})
    sns.barplot(x=stacked.Age, y=stacked.value, hue=stacked.Choice)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

def real_wage(df_unindexed):
    fig, ax = plt.subplots(figsize=(16, 6))
    # This box plox excludes outliers from the data via the Showfliers=False command
    #ensures better visibility of the data
    sns.boxplot(x="Period", y="Wage", data=df_unindexed, hue="Choice", showfliers=False)
    plt.show()

def initial_schooling(df_unindexed):
    fig, ax = plt.subplots(figsize=(10, 6))
    initial_period = df_unindexed[(df_unindexed['Period'].isin(['1']))]
    sns.countplot(initial_period['Schooling'])


def wage_schooling(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x="Schooling", y="Wage", hue="Choice", data=df)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)