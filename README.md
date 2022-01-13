# RecommendationSystem
Content based Recommendation System on TMDB dataset

The recommendation system recommends relevant items, videos, or products to a given user based on historical data according to the user or
item he or she has liked. This system predicts the most likely product that the users are most likely to buy/watch  and 
are of interest to. There are many companies like Amazon, YouTube, Netflix, etc. Use recommender systems to help their users to identify the 
correct product or movies for them.

There are mainly 3 types of recommendation system, here I have worked on Content-based Recommendation system to work with TMDB dataset.

Content-based Recommendation System: It is a type of  recommendation system which recommends content on the basis of content similarity. 
If a user is watching a cricket-related video, then the recommender system will recommend other sports or cricket-related videos of similar content. 
There are various fundamentals attributes that are used to compute the similarity while checking about similar content.

I have used cosine similarity of each movie data and worked over their similarity to recommend movies accourding to similarity.

Cosine similarity
As we will be working on this concept, it would be nice to reiterate the basics.
Cosine similarity is a measure of similarity between two nonzero vectors of an inner product space that measures the cosine of the angle between them. 
Cosine of 00 is 1 and it is less than 1 for any other angle:

Cosine similarity is a metric, helpful in determining, how similar the data objects are irrespective of their size. We can measure the 
similarity between two sentences in Python using Cosine Similarity.
In cosine similarity, data objects in a dataset are treated as a vector. The formula to find the cosine similarity between two vectors is

Cos(x, y) = x . y / ||x|| * ||y||

x . y = product (dot) of the vectors ‘x’ and ‘y’.
||x|| and ||y|| = length of the two vectors ‘x’ and ‘y’.
||x|| * ||y|| = cross product of the two vectors ‘x’ and ‘y’.

You can see the live demo of this project:

https://moviersy.herokuapp.com/
