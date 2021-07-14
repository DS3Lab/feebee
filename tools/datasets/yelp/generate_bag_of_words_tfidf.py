import numpy as np
import json
import spacy
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
import os

os.makedirs("matrices/yelp/train/", exist_ok=True)
os.makedirs("matrices/yelp/test/", exist_ok=True)

nlp = spacy.load("en_core_web_sm")

corpus = []
labels = []

input_file = open("~/Downloads/yelp_academic_dataset_review.json", "r").readlines()
for line in tqdm(input_file[:550000]):
    review = json.loads(line)
    sample = review['text']

    labels.append(review['stars'])

    # preprocess samples
    raw_text = review['text']
    tokenized_text = nlp(raw_text)
    sample_string = ""
    for token in tokenized_text:
        sample_string += token.text + " "

    corpus.append(sample_string.lower())


print("samples:", len(corpus))

# use TF-IDF weighting on word counts
vectorizer = TfidfVectorizer()
# default configuration tokenizes the string by extracting words of at least 2 letters
bow_matrix = vectorizer.fit_transform(corpus)
baseline_features = bow_matrix.toarray()

# get vocabulary details
# print(vectorizer.vocabulary_.items())
print("vocab size:", baseline_features.shape[1])


# separate train and test split again
train_baseline = baseline_features[:500000]
test_baseline = baseline_features[500000:]

train_labels = labels[:500000]
test_labels = labels[500000:]

# save samples to files
np.save("matrices/yelp/train/features_bow_tfidf.npy", train_baseline)
np.save("matrices/yelp/test/features_bow_tfidf.npy", test_baseline)

np.save("matrices/yelp/train/labels_bow_tfidf.npy", train_labels)
np.save("matrices/yelp/test/labels_bow_tfidf.npy", test_labels)
