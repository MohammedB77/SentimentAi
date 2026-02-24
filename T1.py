from textblob import TextBlob

def choose(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity

    if polarity > 0:
        return "happy", polarity
    elif polarity < 0:
        return "sad", polarity
    else:
        return "neutral", polarity

text = input(" Hala Wallah , What Do You Feel right now ? : ")
mood, polarity = choose(text)

print(f"Your mood is {mood}")
print(f"Polarity score: {polarity}")