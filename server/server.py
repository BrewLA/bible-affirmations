from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import os
import random
import threading

# Load environment variables from .env file
load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Bible verses organized by emotion categories
bible_verses = {
    "POSITIVE": [
        "Do everything in love. — 1 Corinthians 16:14",
        "Rejoice always. — 1 Thessalonians 5:16",
        "The Lord is my strength and my shield; my heart trusts in him, and he helps me. — Psalm 28:7",
        "The Lord is good to all; he has compassion on all he has made. — Psalm 145:9",
        "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. — Galatians 5:22-23",
        "The Lord is my shepherd, I lack nothing. — Psalm 23:1",
        "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. — Jeremiah 29:11",
        "Cast all your anxiety on him because he cares for you. — 1 Peter 5:7",
        "And we know that in all things God works for the good of those who love him, who have been called according to his purpose. — Romans 8:28",
        "Be joyful in hope, patient in affliction, faithful in prayer. — Romans 12:12",
        "You will keep in perfect peace those whose minds are steadfast, because they trust in you. — Isaiah 26:3",
        "May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit. — Romans 15:13",
        "The Lord is my light and my salvation—whom shall I fear? The Lord is the stronghold of my life—of whom shall I be afraid? — Psalm 27:1",
        "You make known to me the path of life; you will fill me with joy in your presence, with eternal pleasures at your right hand. — Psalm 16:11",
        "Therefore, since we are surrounded by such a great cloud of witnesses, let us throw off everything that hinders and the sin that so easily entangles. And let us run with perseverance the race marked out for us. — Hebrews 12:1",
        "The Lord is my rock, my fortress and my deliverer; my God is my rock, in whom I take refuge, my shield and the horn of my salvation, my stronghold. — Psalm 18:2",
        "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. — Galatians 5:22-23",
        "I can do all this through him who gives me strength. — Philippians 4:13",
        "And my God will meet all your needs according to the riches of his glory in Christ Jesus. — Philippians 4:19",
        "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. — Galatians 5:22-23",
        "I keep my eyes always on the Lord. With him at my right hand, I will not be shaken. — Psalm 16:8",
        "The Lord is my light and my salvation—whom shall I fear? The Lord is the stronghold of my life—of whom shall I be afraid? — Psalm 27:1",
        "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. — Jeremiah 29:11",
        "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. — Galatians 5:22-23",
        "You make known to me the path of life; you will fill me with joy in your presence, with eternal pleasures at your right hand. — Psalm 16:11",
        "I keep my eyes always on the Lord. With him at my right hand, I will not be shaken. — Psalm 16:8",
        "The Lord is my light and my salvation—whom shall I fear? The Lord is the stronghold of my life—of whom shall I be afraid? — Psalm 27:1",
        "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. — Jeremiah 29:11",
        "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. — Galatians 5:22-23",
        "You make known to me the path of life; you will fill me with joy in your presence, with eternal pleasures at your right hand. — Psalm 16:11",
        "I keep my eyes always on the Lord. With him at my right hand, I will not be shaken. — Psalm 16:8",
        "The Lord is my light and my salvation—whom shall I fear? The Lord is the stronghold of my life—of whom shall I be afraid? — Psalm 27:1",
        "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. — Jeremiah 29:11",
        "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. — Galatians 5:22-23",
        "You make known to me the path of life; you will fill me with joy in your presence, with eternal pleasures at your right hand. — Psalm 16:11",
        "I keep my eyes always on the Lord. With him at my right hand, I will not be shaken. — Psalm 16:8",
        "The Lord is my light and my salvation—whom shall I fear? The Lord is the stronghold of my life—of whom shall I be afraid? — Psalm 27:1",
        "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. — Jeremiah 29:11",
        "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. — Galatians 5:22-23",
        "You make known to me the path of life; you will fill me with joy in your presence, with eternal pleasures at your right hand. — Psalm 16:11",
        "I keep my eyes always on the Lord. With him at my right hand, I will not be shaken. — Psalm 16:8",
        "The Lord is my light and my salvation—whom shall I fear? The Lord is the stronghold of my life—of whom shall I be afraid? — Psalm 27:1",
        "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future. — Jeremiah 29:11",
        "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness, gentleness and self-control. — Galatians 5:22-23",
        "You make known to me the path of life; you will fill me with joy in your presence, with eternal pleasures at your right hand. — Psalm 16:11"
    ],

    "NEGATIVE": [
        "Greater love has no one than this, that someone lay down his life for his friends. — John 15:13",
        "Therefore encourage one another and build each other up, just as in fact you are doing. — 1 Thessalonians 5:11",
        "And we know that in all things God works for the good of those who love him, who have been called according to his purpose. — Romans 8:28",
        "Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go. — Joshua 1:9",
        "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand. — Isaiah 41:10",
        "The Lord is close to the brokenhearted and saves those who are crushed in spirit. — Psalm 34:18",
        "But you, Lord, are a shield around me, my glory, the One who lifts my head high. — Psalm 3:3",
        "In all your ways submit to him, and he will make your paths straight. — Proverbs 3:6",
        "The righteous cry out, and the Lord hears them; he delivers them from all their troubles. — Psalm 34:17",
        "But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint. — Isaiah 40:31",
        "The Lord himself goes before you and will be with you; he will never leave you nor forsake you. Do not be afraid; do not be discouraged. — Deuteronomy 31:8",
        "But he said to me, 'My grace is sufficient for you, for my power is made perfect in weakness.' Therefore I will boast all the more gladly about my weaknesses, so that Christ’s power may rest on me. — 2 Corinthians 12:9",
        "Come to me, all you who are weary and burdened, and I will give you rest. — Matthew 11:28",
        "I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world. — John 16:33",
        "For our light and momentary troubles are achieving for us an eternal glory that far outweighs them all. — 2 Corinthians 4:17",
        "The Lord is my strength and my shield; my heart trusts in him, and he helps me. — Psalm 28:7",
        "The righteous person may have many troubles, but the Lord delivers him from them all. — Psalm 34:19",
        "I can do all this through him who gives me strength. — Philippians 4:13",
        "And my God will meet all your needs according to the riches of his glory in Christ Jesus. — Philippians 4:19",
        "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me. — Psalm 23:4",
        "The Lord is a refuge for the oppressed, a stronghold in times of trouble. — Psalm 9:9",
        "The righteous cry out, and the Lord hears them; he delivers them from all their troubles. — Psalm 34:17",
        "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. — Philippians 4:6",
        "The Lord is close to the brokenhearted and saves those who are crushed in spirit. — Psalm 34:18",
        "But you, Lord, are a shield around me, my glory, the One who lifts my head high. — Psalm 3:3",
        "In all your ways submit to him, and he will make your paths straight. — Proverbs 3:6",
        "The righteous cry out, and the Lord hears them; he delivers them from all their troubles. — Psalm 34:17",
        "But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint. — Isaiah 40:31",
        "The Lord himself goes before you and will be with you; he will never leave you nor forsake you. Do not be afraid; do not be discouraged. — Deuteronomy 31:8",
        "But he said to me, 'My grace is sufficient for you, for my power is made perfect in weakness.' Therefore I will boast all the more gladly about my weaknesses, so that Christ’s power may rest on me. — 2 Corinthians 12:9",
        "Come to me, all you who are weary and burdened, and I will give you rest. — Matthew 11:28",
        "I have told you these things, so that in me you may have peace. In this world you will have trouble. But take heart! I have overcome the world. — John 16:33",
        "For our light and momentary troubles are achieving for us an eternal glory that far outweighs them all. — 2 Corinthians 4:17",
        "The Lord is my strength and my shield; my heart trusts in him, and he helps me. — Psalm 28:7",
        "The righteous person may have many troubles, but the Lord delivers him from them all. — Psalm 34:19",
        "I can do all this through him who gives me strength. — Philippians 4:13",
        "And my God will meet all your needs according to the riches of his glory in Christ Jesus. — Philippians 4:19",
        "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me. — Psalm 23:4",
        "The Lord is a refuge for the oppressed, a stronghold in times of trouble. — Psalm 9:9",
        "The righteous cry out, and the Lord hears them; he delivers them from all their troubles. — Psalm 34:17",
        "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. — Philippians 4:6",
        "The Lord is close to the brokenhearted and saves those who are crushed in spirit. — Psalm 34:18",
        "But you, Lord, are a shield around me, my glory, the One who lifts my head high. — Psalm 3:3",
        "In all your ways submit to him, and he will make your paths straight. — Proverbs 3:6",
        "The righteous cry out, and the Lord hears them; he delivers them from all their troubles. — Psalm 34:17",
        "But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint. — Isaiah 40:31"
    ]

}

def get_feeling_classification(feeling_text):
    # Use the sentiment analysis pipeline to classify the feeling
    result = sentiment_analyzer(feeling_text)[0]
    label = result['label']
    score = result['score']
    return label, score

def get_bible_verse(emotion_label):
    # Fetch a Bible verse based on the emotion label
    if emotion_label == 'POSITIVE':
        return random.choice(bible_verses['POSITIVE'])
    elif emotion_label == 'NEGATIVE':
        return random.choice(bible_verses['NEGATIVE'])
    else:
        return "Rejoice always, pray without ceasing, give thanks in all circumstances; for this is the will of God in Christ Jesus for you. — 1 Thessalonians 5:16"

def generate_response(emotion_label):
    # Generate a response based on the emotion label
    if emotion_label == 'POSITIVE':
        return "That's great to hear! Remember to keep a positive outlook."
    elif emotion_label == 'NEGATIVE':
        return "I'm sorry you're feeling this way. It's important to take care of yourself."
    else:
        return "I see. It's important to acknowledge how you feel."

@app.route('/api/home', methods=['POST'])
def generate_verse():
    data = request.get_json()
    user_feeling = data.get('feeling')

    if not user_feeling:
        return jsonify({'error': 'Feeling is required!'}), 400

    try:
        emotion_label, confidence_score = get_feeling_classification(user_feeling)
        verse = get_bible_verse(emotion_label)
        response_message = generate_response(emotion_label)
        return jsonify({
            'emotion': emotion_label,
            'confidence_score': confidence_score,
            'verse': verse,
            'response_message': response_message
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def run_flask_app():
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)

if __name__ == '__main__':
    # Run Flask app in a separate thread
    threading.Thread(target=run_flask_app).start()