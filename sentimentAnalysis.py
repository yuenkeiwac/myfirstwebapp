from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import pysenti
import bixin
import re
vad = SentimentIntensityAnalyzer()

class Prediction():
    
    def Compute_ENGWord_Sentiment(self, word):
        polarity_value = 0

        # Vader Lexicon
        try:
            polarity_value = vad.polarity_scores(re.sub('-', ' ', word))['compound']
        except Exception as e:
            print(e, word)
            polarity_value = 0

        return polarity_value

    def Compute_CHIWord_Sentiment(self, sent):
        return predict(sent)
        #return pysenti.classify(sent)['score']
    
    def split_sentence(self, sent):
        score = 0.0
        for word in sent.split():
            score += self.Compute_ENGWord_Sentiment(word)
        return score
    
    def returnSentiment(self, score):
        if (score < 0):
            color = 'highlight red'
            sentiment = 'Negative'
        elif (score > 0):
            color = 'highlight green'
            sentiment = 'Positive'
        else:
            color = 'highlight orange'
            sentiment = 'Neutral'
        return color, sentiment
