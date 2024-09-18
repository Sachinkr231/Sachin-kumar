def sentiment_analysis(text):
    positive_words = ["amazing", "fantastic", "wonderful", "brilliant", "awesome"]
    negative_words = ["horrible", "disappointing", "awful", "miserable", "dreadful"]

    words = text.lower().split()
    
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    if pos_count > neg_count:
        return "Positive"
    elif pos_count < neg_count:
        return "Negative"
    else:
        return "Neutral"

text = input("Please enter a sentence to analyze sentiment: ")
print("Sentiment:", sentiment_analysis(text))
