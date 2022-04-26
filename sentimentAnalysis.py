import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
vad = SentimentIntensityAnalyzer()

class Prediction():
    def Compute_ENGWord_Sentiment(word):
        polarity_value = 0

        # Vader Lexicon
        try:
            polarity_value = vad.polarity_scores(re.sub('-', ' ', word))['compound']
        except Exception as e:
            print(e, word)
            polarity_value = 0

        return polarity_value

    def split_sentence(sent):
        score = 0.0
        for word in sent.split():
            score += Compute_ENGWord_Sentiment(word)
        return score
