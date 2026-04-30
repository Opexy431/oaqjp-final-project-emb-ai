import requests
import json

def emotion_detector(text_to_analyze):
   
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    
    response = requests.post(url, json=myobj, headers=header)
    
    formatted_response = json.loads(response.text)
    
    # Step 3: Extract the specific emotions from the nested dictionary
    # IBM's structure is: emotionPredictions[0]['emotion']
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Step 4: Extract individual scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    
   
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Step 6: Return the final formatted dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }