# coding: utf-8

# In[62]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime as dt

get_ipython().run_line_magic('matplotlib', 'inline')

# In[303]:


tizibika = pd.read_csv('tiziba_dataset_2.csv')

# In[304]:


tizibika.head()

# In[305]:


tizibika.info()

# In[306]:


tizibika['time_date'] = pd.to_datetime(tizibika['timestamp'])

# In[307]:


tizibika['date'] = [d.date() for d in tizibika['time_date']]
tizibika['time'] = [d.time() for d in tizibika['time_date']]
tizibika['hour'] = tizibika.time_date.dt.hour

# In[308]:


tizibika.head()

# In[309]:


date_tweet_count = tizibika['date'].value_counts()


# In[314]:


def convert_index_column(df_tweet_count):
    index_list = np.array(df_tweet_count.index)
    tweets_list = []
    for index, date_from_index in enumerate(index_list):
        tweets_counts = df_tweet_count['date'][index]
        tweets_per_day = {'date': date_from_index, 'number_of_tweets': tweets_counts}
        tweets_list.append(tweets_per_day)
    return tweets_list


# In[315]:


df_tweet_date_count = pd.DataFrame(data=date_tweet_count)
tweets_per_day = convert_index_column(df_tweet_date_count)
tweets_per_day_df = pd.DataFrame(tweets_per_day)
tweets_per_day_df

# In[316]:


tweets_per_day_df.plot.line(x=tweets_per_day_df['date'], y='number_of_tweets', figsize=(15, 8), lw=1)

# In[503]:


hour_tweet_count = tizibika['hour'].value_counts()
df_tweet_hour_count = pd.DataFrame(data=hour_tweet_count)


# In[387]:


def convert_index_hour(df_tweet_count):
    index_list = np.array(df_tweet_count.index)
    tweets_list = []
    for index, hour_from_index in enumerate(index_list):
        tweets_counts = df_tweet_count['hour'][hour_from_index]
        hour = str(hour_from_index) + "hrs"
        tweets_per_hour = {'hour': hour, 'number_of_tweets': tweets_counts}
        tweets_list.append(tweets_per_hour)
    return tweets_list


# In[495]:


tweets_per_hour = convert_index_hour(df_tweet_hour_count)
tweets_per_hour_df = pd.DataFrame(tweets_per_hour)
tweets_per_hour_df

# In[491]:


tweets_per_hour_df.plot.line(x='hour', y='number_of_tweets', figsize=(15, 8), lw=1)

# In[494]:


sns.barplot(x='hour', y='number_of_tweets', data=tweets_per_hour_df)

# In[392]:


tizibika[tizibika['retweets'] == tizibika['retweets'].max()]

# In[396]:


highly_retweeted = tizibika[tizibika['retweets'] == tizibika['retweets'].max()]

# In[398]:


sns.barplot(x='user', y='retweets', data=highly_retweeted)

# In[400]:


tizibika[tizibika['likes'] == tizibika['likes'].max()]

# In[433]:


tweep_group = tizibika.groupby('user')
tweep_most_likes = tweep_group['likes'].sum()
tweep_most_likes_df_temp = pd.DataFrame(tweep_most_likes)
tweep_most_likes_df = pd.DataFrame(tweep_most_likes_df_temp['likes'])


# In[443]:


def convert_index_most_liked(tweep_most_likes_df):
    index_list = np.array(tweep_most_likes_df.index)
    tweeps = []
    for index, user_from_index in enumerate(index_list):
        total_likes = tweep_most_likes_df['likes'][index]
        likes_per_user = {'user': user_from_index, 'number_of_likes': total_likes}
        tweeps.append(likes_per_user)
    return tweeps


# In[454]:


temp = convert_index_most_liked(tweep_most_likes_df)
most_likes_df = pd.DataFrame(temp)
most_liked_tweets = most_likes_df.sort_values(by='number_of_likes')
most_liked_tweets.tail(5)

# In[458]:


sns.barplot(x='user', y='number_of_likes', data=most_liked_tweets.tail(5))

# In[484]:


most_retweeted_tweeps_sum = tizibika.groupby('user')['retweets'].sum()

# In[485]:


temp = pd.DataFrame(most_retweeted_tweeps_sum)


# In[486]:


def convert_index_most_retweeted(tweep_most_retweeted_df):
    index_list = np.array(tweep_most_likes_df.index)
    tweeps = []
    for index, user_from_index in enumerate(index_list):
        total_retweets = tweep_most_retweeted_df['retweets'][index]
        retweets_per_user = {'user': user_from_index, 'number_of_retweets': total_retweets}
        tweeps.append(retweets_per_user)
    return pd.DataFrame(tweeps)


# In[487]:


most_retweeted_tweeps_df = convert_index_most_retweeted(temp)

# In[489]:


most_retweeted_tweeps_sorted = most_retweeted_tweeps_df.sort_values(by='number_of_retweets')
most_retweeted_tweeps_sorted.tail(5)

# In[490]:


sns.barplot(x='user', y='number_of_retweets', data=most_retweeted_tweeps_sorted.tail(5))

# In[53]:


tizibika.info()

# In[252]:


tizibika.head()

# In[253]:


tizibika.drop(['timestamp'], axis=1, inplace=True)

# In[261]:


tizibika.head()


# In[262]:


def get_hour(tizibika):
    for tweet in tizibika:
        tizibika['hour'] = pd.to_datetime(tizibika['time'])
    return tizibika


# In[263]:


get_hour(tizibika)

# In[131]:


by_date['user'].value_counts()

# In[133]:


df_tweet_count

# In[138]:


df_tweet_count.index

# In[148]:





# In[162]:





# In[239]:


tizibika.info()


# In[179]:


def convert_time_index_column(df_tweet_count):
    index_list = np.array(df_tweet_count.index)
    tweets_list = []
    for index, date_from_index in enumerate(index_list):
        tweets_counts = df_tweet_count['time'][index]
        tweets_per_hour = {'time': date_from_index.hour, 'number_of_tweets': tweets_counts}
        tweets_list.append(tweets_per_hour)
    return tweets_list


# In[183]:


tweets_per_hour = convert_time_index_column(df_time_tweet_count)


# In[ ]:





# In[211]:


def convert_time_index_to_hours(df_tweet_count):
    index_list = np.array(df_tweet_count.index)
    tweets_list = []
    for index, hour_from_index in enumerate(index_list):
        tweets_counts = df_tweet_count['number_of_tweets'][index]
        tweets_per_hour = {'hour': hour_from_index, 'tweets_number': tweets_counts}
        tweets_list.append(tweets_per_hour)
    return tweets_list


# In[212]:


convert_time_index_to_hours(df_tweets_per_hour)

