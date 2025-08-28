import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

class MentalWellnessSentiment:
    def __init__(self):
        nltk.download('vader_lexicon', quiet=True)
        self.nltk_analyzer = SentimentIntensityAnalyzer()
        try:
            self.emotion_classifier = pipeline(
                "text-classification",
                model="j-hartmann/emotion-english-distilroberta-base",
                return_all_scores=True
            )
        except Exception as e:
            print(f"Emotion model loading failed: {e}")
            self.emotion_classifier = None

    def analyze(self, text):
        nltk_scores = self.nltk_analyzer.polarity_scores(text)
        emotions = []
        if self.emotion_classifier:
            try:
                emotion_results = self.emotion_classifier(text)
                emotions = sorted(emotion_results[0], key=lambda x: x['score'], reverse=True)[:3]
            except Exception:
                emotions = []
        return {
            'sentiment': self._categorize_sentiment(nltk_scores['compound']),
            'confidence': abs(nltk_scores['compound']),
            'detailed_scores': nltk_scores,
            'emotions': emotions
        }

    def _categorize_sentiment(self, compound):
        if compound >= 0.05:
            return "positive"
        elif compound <= -0.05:
            return "negative"
        return "neutral"
