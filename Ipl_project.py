import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('ipl_2022_match_wise.csv')
print(df)

print(df.head())
print()
print(df.shape)
#check the size of rows and columns of the dataset
print(f"your rows are {df.shape[0]} and your columns are {df.shape[1]}")
#now let's see how many columns have null values in total
print(df.isnull().sum())

#Which team won the most matches

match_wins = df['winner'].value_counts()
print(match_wins)
sns.barplot(x = match_wins.index, y=match_wins.values,palette='rainbow')
plt.title('Most match win by team')
plt.show()

#Toss Decision Trends
sns.countplot(x = df['toss_decision'],palette='rainbow')
plt.title('Toss Decision Trends')
plt.show()

# Toss winner vs Match winner
print(df[df['toss_winner'] == df['winner']]['match_id'].count())
count = df[df['toss_winner'] == df['winner']]['match_id'].count()
percentage = (count * 100)/df.shape[0]
print(percentage.round(2))


#How do team win? (Runs vs Wickets)

sns.countplot(y = df['win_margin'])
plt.title('win_margin')
plt.show()


# KEY PLAYER PERFORMANCES
 # 1 Most "player Of The Match" Awards


count = df['player_of_match'].value_counts().head(10)

print(count)
sns.barplot(y = count.index, x=count.values,palette='mako')
plt.title('Top 10 players win of the match')
plt.show()



high = df.groupby('team1')['team1_runs'].sum()
print(high)
#Top 2 team high run
high = df.groupby('team1')['team1_runs'].sum().sort_values(ascending=False).head(2)
print(high)
high.plot(kind='bar')
plt.show()


# VENUE ANALYSIS
# Most Matches Played by Venue

venue_court = df['venue'].value_counts()
print(venue_court)
sns.barplot(y =venue_court.index, x = venue_court.values,palette='rainbow')
plt.show()

# CUSTOM QUESTIONS AND INSIGHTS
df['highest_score'] = df[['team1_runs','team2_runs']].max(axis=1)


high_match = df.loc[df['highest_score'].idxmax()]

print("Highest Score:", high_match['highest_score'])
print("Winner:", high_match['winner'])

