import random

class TherapeuticResponses:
    def __init__(self):
        self.responses = {
            'negative': {
                'sadness': [
                    "I hear that you're feeling down. It's completely normal to have these feelings. Would you like to try some breathing exercises?",
                    "Thank you for sharing how you're feeling. Sometimes talking about sadness can help lighten the load.",
                    "I understand you're going through a tough time. Let's work together to find some comfort."
                ],
                'anger': [
                    "I can sense your frustration. Let's take a moment to breathe and find some calm together.",
                    "Anger can be overwhelming. Would you like me to guide you through some relaxation techniques?",
                    "It sounds like something is really bothering you. I'm here to help you work through these feelings."
                ],
                'fear': [
                    "I understand you might be feeling anxious. You're not alone in this - I'm here with you.",
                    "Fear can be very overwhelming. Let's focus on some grounding techniques that might help.",
                    "It's okay to feel scared sometimes. Would you like to try some mindfulness exercises?"
                ]
            },
            'positive': [
                "It's wonderful to hear you're feeling good! What's bringing you joy today?",
                "I'm so glad you're having a positive day. How can we keep this good energy going?",
                "Your positive energy is contagious! What would you like to talk about?"
            ],
            'neutral': [
                "Thanks for checking in. How has your day been so far?",
                "I'm here to listen. What's on your mind today?",
                "How are you feeling right now? I'm here to support you."
            ]
        }

        self.suggestions = {
            'negative': {
                'breathing': "Try the 4-7-8 technique: Inhale for 4, hold for 7, exhale for 8",
                'music': "Consider listening to calming music like ambient or classical",
                'activity': "A gentle walk or some stretching might help",
                'reading': "Perhaps some inspiring quotes or a calming book"
            },
            'positive': {
                'breathing': "Try energizing breath work to maintain your positive state",
                'music': "Upbeat music might complement your good mood",
                'activity': "Consider celebrating with a favorite activity",
                'reading': "Maybe some motivational content to keep the momentum"
            },
            'neutral': {
                'breathing': "Box breathing can help bring focus and clarity",
                'music': "Balanced, peaceful music might suit your current state",
                'activity': "A mindful activity like journaling could be beneficial",
                'reading': "Some reflective reading might provide insight"
            }
        }

    def generate_response(self, sentiment_result):
        sentiment = sentiment_result['sentiment']
        emotions = sentiment_result.get('emotions', [])
        if sentiment == 'negative' and emotions:
            emotion_name = emotions[0]['label'].lower()
            responses = self.responses['negative'].get(emotion_name, self.responses['negative']['sadness'])
        else:
            responses = self.responses.get(sentiment, self.responses['neutral'])
        return random.choice(responses)

    def get_suggestions(self, sentiment):
        return self.suggestions.get(sentiment, self.suggestions['neutral'])
