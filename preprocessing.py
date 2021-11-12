import pandas as pd

from nltk.stem import snowball

plot_summaries_path = "./MovieSummaries/plot_summaries.txt"
import nltk

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer





class Preprocessing():
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    stop_words = stopwords.words('english')
    f = None
    index_arr = []
    plot_summaries_obj = {}
    pd_phase1 = None

    def __init__(self) -> None:
        self.f = open(plot_summaries_path, "rt")

    def get_plot_summaries_obj(self):
        lines = self.f.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            line_words = line.split(None, 1)
            index = line_words[0]
            self.index_arr.append(index)
            tokenizer = nltk.RegexpTokenizer(r"\w+")
            line_words = tokenizer.tokenize(line_words[1])  # tokenize
            self.plot_summaries_obj[index] = []
            for word in line_words[1:]:
                result = self.preparing(word)
                if result is not None:
                    self.plot_summaries_obj[index] = result
        self.pd_phase1 = pd.Series(self.plot_summaries_obj, index=self.index_arr)

    @classmethod
    def preparing(cls,word):
        wordnet_lemmatizer = WordNetLemmatizer()
        if word not in cls.stop_words:
            word = word.lower()
            stemmer = snowball.SnowballStemmer('english')
            stemmed_word= stemmer.stem(word)
            return wordnet_lemmatizer.lemmatize(stemmed_word)
        return None

# preprocessor=Preprocessing()
# preprocessor.get_plot_summaries_obj()
# preprocessor.stemmer()
