import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import warnings 
warnings.filterwarnings("ignore")
df=pd.read_csv("IPL.csv")
print(df.head(5))
print()
print(df.info())
print()
print(df.isnull().sum())
print()
print(df.describe())
print()
print(df.columns)

# Question 1 Which team won the most matches?

winner=df['match_winner'].value_counts()
sns.barplot(y=winner.index,x=winner.values,palette='rainbow',)
plt.title('MATCH WON BY TEAM')
plt.xlabel('Number of Time a Team Wins ')
plt.ylabel('Team Name')
plt.show()

# Question-2 trend of decision of toss

sns.countplot(x=df['toss_decision'],palette='rainbow')
plt.xlabel("2 Decision")
plt.ylabel("Times It's Selected")
plt.title('Toss Decision')
plt.show()

#Question-3 Toss winner vs match winner 

count=df[df['toss_winner']==df['match_winner']]['match_id'].count()
percentage=((count*100)/df.shape[0])
print(percentage.round(2))
print()
# Question-4 won by wickets or Runs
sns.countplot(x=df['won_by'])
plt.show()

#Question-5 Most "Player of the Match" Awards

count=df['player_of_the_match'].value_counts().head(10)
print(count)
sns.barplot(x=count.values,y=count.index,palette='rainbow')
plt.title("Top 10 player with MAN OF THE MATCH")
plt.show()

#Question-6 Top Scorers
top_count=df['top_scorer'].value_counts().head(2)
print(top_count)
sns.barplot(y=top_count.values,x=top_count.index,palette='rainbow')
plt.title("TOP 2 SCORER")
plt.xlabel("NAME OF PLAYER")
plt.ylabel("NUMBER OF TIMES THE BECOME TOP SCORCER")
plt.show()

# With there total Runs 

high = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(2)
print(high)
high.plot(kind='barh')
plt.show()

#Question-7 10 Best Bowling Figures

df['highest_wickets']=df['best_bowling_figure'].apply(lambda x:x.split('--')[0])
df['highest_wickets']=df['highest_wickets'].astype(int)
top_bolwer=df.groupby('best_bowling')['highest_wickets'].sum().sort_values(ascending=False).head(10)
top_bolwer.plot(kind='barh')
plt.show()
#Question-8 Most Matches Played by Venue
venue_count = df['venue'].value_counts()
sns.barplot(y = venue_count.index,x = venue_count.values,palette='rainbow')
plt.show()

#Question-9 Who won the highest margin by runs?
print(df[df['won_by']=='Runs'].sort_values(by='margin',ascending=False).head(1)[['match_winner','margin']])

#Question-10 Which player had the highest individual score?
print(df[df['highscore']==df['highscore'].max()] [['top_scorer','highscore']])

#Question-11 Which bowler had the best bowling figures?
print(df[df['highest_wickets']==df['highest_wickets'].max()][['best_bowling','best_bowling_figure']])