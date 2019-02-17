# AI on User Generated Content 

This projects has explorations of handling UGC:  Recommendation Engines, NLP, and more.  This material is covered in [Chapter 11 of Pragmatic AI](https://www.amazon.com/Pragmatic-AI-Introduction-Cloud-based-Learning/dp/0134863860)

## Jupyter Notebooks for UGC (User Generated Content)

### Recommendations

Explorations of recommendation engines 

* [Surprise Knn Recommendation Exploration](https://github.com/noahgift/recommendations/tree/master/notebooks)
* [Tanimoto (Or Similarity Score) Based Hand Coded Recommended Engine](https://github.com/noahgift/recommendations/tree/master/tanimoto_example)

*How to use:*

```ipython
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

```


### Cloud NLP

Explorations of Cloud NLP APIS on Google, Azure and AWS

* [Natural Language Processing on AWS](https://github.com/noahgift/recommendations/blob/master/notebooks/NLP_AWS.ipynb)
* [NLP on Azure](https://github.com/noahgift/recommendations/blob/master/notebooks/Azure_Sentiment_Analysis.ipynb)
* [NLP on GCP](https://github.com/noahgift/recommendations/blob/master/notebooks/NLP_GCP.ipynb)

![Kernel Density Plot of NLP Azure Call](https://user-images.githubusercontent.com/58792/36956624-4009fc9e-1fe4-11e8-9c0b-b76a72768a84.png)
