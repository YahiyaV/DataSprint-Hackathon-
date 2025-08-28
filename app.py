from flask import Flask, render_template, request, jsonify
from sentiment_analyzer import MentalWellnessSentiment
from response_generator import TherapeuticResponses
import datetime

app = Flask(__name__)
sentiment_analyzer = MentalWellnessSentiment()
response_gen = TherapeuticResponses()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    # Analyze sentiment and emotions
    analysis = sentiment_analyzer.analyze(user_message)

    # Generate therapeutic response
    bot_response = response_gen.generate_response(analysis)

    # Get mood-based suggestions
    suggestions = response_gen.get_suggestions(analysis['sentiment'])

    return jsonify({
        'response': bot_response,
        'analysis': analysis,
        'suggestions': suggestions,
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'service': 'Mental Wellness Chatbot'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
