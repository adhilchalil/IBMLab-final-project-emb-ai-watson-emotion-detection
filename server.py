'''Module to run a Web app handling text emotion analyzing'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' Renders the base page '''
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_api():
    ''' Takes in a text string and returns emotions by
    calling Watson API for text emotion analyzing'''
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is anger: {emotions['anger']},-\
     disgust: {emotions['disgust']}, fear: {emotions['fear']}, joy: {emotions['joy']}-\
      and sadness: {emotions['sadness']} The dominant emotion is joy."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
