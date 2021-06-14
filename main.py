import string

from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter


def main():
    # First, load in the journal entry the user wrote
    temp = open('read.txt', 'r').read()
    # We then make the entire journal entry lower-case
    temp_lower = temp.lower()
    # Finally, we remove all the punctuation from the entry
    journal_entry = temp_lower.translate(str.maketrans('', '', string.punctuation))

    # Now that we have a cleaned journal entry, we can tokenize the words
    tokenized_entry = word_tokenize(journal_entry, "english")

    # And then we remove 'stop words,' or common words that don't have any information/emotion attached to them
    final_entry = []
    for word in tokenized_entry:
        if word not in stopwords.words('english'):
            final_entry.append(word)

    # Now that we have all the important words from the entry, we can preform lemmatization, or the process of
    # turning plural words into singular words, turning verbs into their base form, etc.
    # We want to get the part-of-speech of the word so we can lemmatize it properly, otherwise it'll be treated
    # as a noun always.
    lemma_entry = []
    for word, tag in pos_tag(final_entry):
        if tag.startswith('N'):
            lemma_word = WordNetLemmatizer().lemmatize(word, pos='n')
        elif tag.startswith('V'):
            lemma_word = WordNetLemmatizer().lemmatize(word, pos='v')
        elif tag.startswith('J'):
            lemma_word = WordNetLemmatizer().lemmatize(word, pos='a')
        lemma_entry.append(lemma_word)

    # Finally, we can compare the words we have to our emotion list and identify which two emotions are most prevalent!

    # First we go through the emotions file and compare the words there with the words in our journal entry
    potential_emotions = []
    with open('emotions.txt') as file:
        for line in file:
            stripped_line = line.replace('\n', '').replace(',', '').replace('\'', '').strip()
            word, emotion = stripped_line.split(':')

            if word in lemma_entry:
                potential_emotions.append(emotion)

    # Then, we go through all the emotions we found and see which is most common
    emotion = Counter(potential_emotions)
    print(emotion.most_common(2))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
