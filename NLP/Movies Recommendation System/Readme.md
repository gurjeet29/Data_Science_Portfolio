# Movies Recommendation System

## The deployed app can be found here: https://movies-recommendation-system-0.herokuapp.com/

## The datasets are collected form different sources.The links can be found below:
1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)
6. [List of movies in 2021](https://en.wikipedia.org/wiki/List_of_American_films_of_2021)
7. [List of movies in 2022](https://en.wikipedia.org/wiki/List_of_American_films_of_2022)

## Project Objective
The purpose of this Content Based Movies Recommendation System is to recommend movies similar to the movie user likes based on Cosine Similarlity metrics.

## Methods Used
* Inferential Statistics
* NLP
* Cosine Similarlity metrics

## Technologies
* Python
* Pandas
* Jupyter
* Numpy
* Sci-Kit Learn (for data handling)
* Count Vectorizer
* Streamlit

## Project Description
This project was developed by collecting data from different sources like kaggle and web scraping and then combining and transforming the data into a common format to convert the features into vectors to apply Cosine Similarlity metrics. The details of the movies(title, genre, rating, poster, id etc) were fetched using an API by TMDB, https://www.themoviedb.org/documentation/api.

## How to get the API key?
Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## Algorithm
**Content-based recommenders:** suggest similar items based on a particular item. This system uses item metadata, such as genre, director, description, actors, etc. for movies, to make these recommendations. The general idea behind these recommender systems is that if a person likes a particular item, he or she will also like an item that is similar to it. And to recommend that, it will make use of the user's past item metadata. A good example could be YouTube, where based on your history, it suggests you new videos that you could potentially watch.

## Similarity Score : 
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.
   
## How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![img](https://user-images.githubusercontent.com/84326897/184502978-b10401b0-53ba-48c9-a7c7-41cd43b32103.png)

More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

## Deployment
The model is deployed on heroku using streamlit:

Deployed model: https://movies-recommendation-system-0.herokuapp.com/

![image](https://user-images.githubusercontent.com/84326897/186660548-58b8b110-1600-4f3c-8ca8-dc9ab5191424.png)

**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
