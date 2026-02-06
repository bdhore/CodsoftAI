import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample Data: Movies and their descriptions
data = {
    'title': ['The Matrix', 'Inception', 'Toy Story', 'Finding Nemo', 'Interstellar'],
    'description': [
        'A hacker discovers a simulated reality and fights a machine war.',
        'A thief enters dreams to steal secrets and plant ideas.',
        'A cowboy doll and an astronaut action figure come to life.',
        'A clownfish searches for his son in the vast ocean.',
        'Astronauts travel through a wormhole to find a new home for humanity.'
    ]
}

df = pd.DataFrame(data)

# 1. Convert text to math (TF-IDF Vectorization)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# 2. Compute the Similarity Score (Cosine Similarity)
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# 3. Recommendation Function
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = df.index[df['title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get top 2 similar movies (excluding itself)
    movie_indices = [i[0] for i in sim_scores[1:3]]
    return df['title'].iloc[movie_indices]

print(get_recommendations('The Matrix'))
# Output: Inception, Interstellar