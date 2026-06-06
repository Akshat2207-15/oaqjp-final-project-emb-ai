
"""
This module provides a Flask web application for emotion detection
using the Watson NLP library.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Analyzes the emotion of the given text and returns the result
    in a formatted string. Returns an error message for blank input.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    return (f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, "
            f"'fear': {fear}, 'joy': {joy} and "
            f"'sadness': {sadness}. The dominant emotion is {dominant}.")

@app.route("/")
def render_index_page():
    """
    Renders the index page of the web application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
