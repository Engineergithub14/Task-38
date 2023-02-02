# COMPULSORY TASK 2

# importing spacy
import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') 

# description given
desc= '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet
where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''
nlp_d=nlp(desc)

# reading data from a file movies.txt
file_data=open("movies.txt",'r')
most_similar_movie=''
max_similarity=0

# running a for loop for the whole length and finding the movie with most similariy
for line in file_data.readlines():
    # splitting the line
    movie_data=line.split(':')
    # getting movie name and movie description
    movie_name=movie_data[0]
    movie_text=movie_data[1]
    nlp_f = nlp(movie_text)
    
    # finding the nlp similarity
    the_sim=nlp_f.similarity(nlp_d)
    print(the_sim)

    # if this is the max similairt till now, make this movie the most probable one
    if the_sim>max_similarity:
        max_similarity=the_sim
        most_similar_movie=movie_name
    else:
        pass

file_data.close()

print(f"The movie similar movie is {most_similar_movie}")