"""
Follow recommendations and descriptive statistics


In [1]: follows import *

In [2]: df = follows_dataframe()

In [3]: dfr = follow_relations_df(df)

In [4]: dfr.head()

In [5]: scores = generate_similarity_scores(dfr, "00480160-0e6a-11e6-b5a1-06f8ea4c790f")

In [5]: scores
Out[5]: 
2144    0.000000
713     0.000000
714     0.000000
715     0.000000
716     0.000000
717     0.000000
712     0.000000
980     0.333333
2057    0.333333
3       1.000000
Name: follow_relations, dtype: float64

In [6]: dfs = return_similarity_scores_with_ids(dfr, scores)

In [6]: dfs
Out[6]: 
                                followerId  \
980   76cce300-0e6a-11e6-83e2-0242528e2f1b   
2057  f5ccbf50-0e69-11e6-b5a1-06f8ea4c790f   
3     00480160-0e6a-11e6-b5a1-06f8ea4c790f   

                                       follow_relations    scores  \
980   [f5ccbf50-0e69-11e6-b5a1-06f8ea4c790f, 0048016...  0.333333   
2057  [76cce300-0e6a-11e6-83e2-0242528e2f1b, 0048016...  0.333333   
3     [f5ccbf50-0e69-11e6-b5a1-06f8ea4c790f, 76cce30...         1   

      following_count  
980                 2  
2057                2  
3                   2 


"""

import os
import pandas as pd

from .algorithms import tanimoto

def follows_dataframe(path=None):
    """Creates Follows Dataframe"""

    if not path:
        path = os.path.join(os.getenv('PYTHONPATH'), 'ext', 'follows.csv')

    df = pd.read_csv(path)
    return df

def follower_statistics(df):
    """Returns counts of follower behavior

    In [15]: follow_counts.head()
        Out[15]: 
        followerId
        581bea20-962c-11e5-8c10-0242528e2f1b    1558
        74d96701-e82b-11e4-b88d-068394965ab2      94
        d3ea2a10-e81a-11e4-9090-0242528e2f1b      93
        0ed9aef0-f029-11e4-82f0-0aa89fecadc2      88
        55d31000-1b74-11e5-b730-0680a328ea36      64
        Name: followingId, dtype: int64

    """

    follow_counts = df.groupby(['followerId'])['followingId'].\
        count().sort_values(ascending=False)
    return follow_counts

def follow_metadata_statistics(df):
    """Generates metadata about follower behavior
    
    In [13]: df_metadata.describe()
        Out[13]: 
        count    2145.000000
        mean        3.276923
        std        33.961413
        min         1.000000
        25%         1.000000
        50%         1.000000
        75%         3.000000
        max      1558.000000
        Name: followingId, dtype: float64

    """

    dfs = follower_statistics(df)
    df_metadata = dfs.describe()
    return df_metadata

def follow_relations_df(df):
    """Returns a dataframe of follower with all relations"""

    df = df.groupby('followerId').followingId.apply(list)
    dfr = df.to_frame("follow_relations")
    dfr.reset_index(level=0, inplace=True)
    return dfr

def simple_score(column, followers):
    """Used as an apply function for dataframe"""

    return tanimoto(column,followers)

def get_followers_by_id(dfr, followerId):
    """Returns a list of followers by followerID"""

    followers = dfr.loc[dfr['followerId'] == followerId]
    fr = followers['follow_relations']
    return fr.tolist()[0]

def generate_similarity_scores(dfr, followerId, limit=10, threshold=.1):
    """Generates a list of recommendations for a followerID"""

    followers = get_followers_by_id(dfr, followerId)
    recs = dfr['follow_relations'].\
        apply(simple_score, args=(followers,)).\
            where(dfr>threshold).dropna().sort_values()[-limit:]
    filters_recs = recs.where(recs>threshold)
    return filters_recs

def return_similarity_scores_with_ids(dfr, scores):
    """Returns Scores and FollowerID"""

    dfs = pd.DataFrame(dfr, index=scores.index.tolist())
    dfs['scores'] = scores[dfs.index]
    dfs['following_count'] = dfs['follow_relations'].apply(len)
    return dfs

    