from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return "Uhm.. Say something!"

    emotions = emotion_detector(text_to_analyze)
    
    return f"For the given statement, the system response is anger: {emotions['anger']}, disgust: {emotions['disgust']}, fear: {emotions['fear']}, joy: {emotions['joy']} and sadness: {emotions['sadness']} The dominant emotion is joy."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)