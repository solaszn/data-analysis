# ASSIGNMENT
# Make a distribution plot (histogram) of the 'Fare' attribute of the data using Matplotlib
# Make a distribution plot of the 'Fare' attribute of the data using Seaborn
# Make a joint plot comparing the 'Fare' and 'Age' attributes of the data using Seaborn.
# Make a box plot comparing the 'Pclass' attribute (x axis) with the 'Age' attribute (y axis) using Seaborn
# Make a violin plot comparing the 'Embarked' attribute (x axis) with the 'Age' attribute (y axis) using Seaborn
# Make a count plot of the 'Pclass' attribute using Seaborn to display the number of passengers in each class
# Calculate the correlation of the DataFrame using Pandas, and make a heatmap of the correlation using Plotly (Don't forget to add the labels of the dataframe to the x and y axis)
# Make a violin plot comparing the 'Pclass' attribute (x axis) with the 'Age' attribute of the data using Plotly
# Make a density heatmap comparing the 'Pclass' attribute with the 'Survived' attribute using Plotly to see the number of people that survived or didn't survive in each passenger class

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv("Titanic_Detailed.csv")
df.head()
# 1
plt.hist('Fare', data=df)
plt.show()
# 2
sns.distplot(df['Fare'])
plt.show()
# 3
sns.jointplot(x='Fare', y='Age', data=df)
plt.show()
# 4
sns.boxplot(x='Pclass', y='Age', data=df)
plt.show()
# 5
sns.violinplot(x='Embarked', y='Age', data=df)
plt.show()
# 6
sns.countplot(x='Pclass', data=df)
plt.show()
# 7
df_copy = df.drop(['Cabin'], axis=1)
correlation = df_copy.corr()
labels=list(df_copy)
fig = px.imshow(correlation)
fig.show()
# 8
fig = px.violin(data_frame=df_copy, x='Pclass', y='Age')
fig.show()
# 9
fig = px.density_heatmap(df_copy, x='Pclass', y='Age')
fig.show()
