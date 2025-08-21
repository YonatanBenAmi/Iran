from fetcher import Fetcher
import pandas
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer



class Processor:

    fetcher = Fetcher()
    dict_df = fetcher.get_df().to_dict(orient="index")

    def add_col_rarest(self):
        for tweet in self.dict_df.keys:
            print(tweet)
            self.dict_df["tweet"]["rarest"] = self.get_rarest_word(tweet["Text"])
        return self.dict_df

    
    def get_rarest_word(self, text):
        list_words = text.split()
        dict_words = {}
        for word in list_words:
            if word in dict_words:
                dict_words[word] += 1
            else:
                dict_words[word] = 1
        return max(dict_words, key=dict_words.get)
        
    def get_emotion(self, tweet):
        nltk.download('vader_lexicon')# Compute sentiment labels
        score = SentimentIntensityAnalyzer().polarity_scores(tweet)
        return score
    
a = Processor()

print(a.add_col_rarest())