import requests
import json

def emotion_detector(text_to_analyse):
    URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers={"grpc-metadata-mm-model-id":   "emotion_aggregated-workflow_lang_en_stock"}
    json_obj={ "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = json_obj, headers=headers)
    if response.status_code == 400:
        return  {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
         
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = 'anger'
    for emotion, emotion_score in emotion_scores.items():
        if emotion_score > emotion_scores[dominant_emotion]:
            dominant_emotion = emotion

    emotions = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return emotions