import re
from random import randint

import pandas as pd
from textblob import TextBlob


# Cleans the texts (links,special characters etc.) using a regex
def cleanText(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)" , " " , text).split())


# function to classify sentiment of passed text using textblob's sentiment method
def get_text_sentiment(text):
    # creates TextBlob object of passed tweet text
    analysis = TextBlob(text)
    # Checks the polarity of the text
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"


def get_texts():
    # empty list to store parsed texts
    texts = []
    # fetching texts
    texts_csv = pd.read_csv("Data Sets\Tweets.csv")
    # Creating an array to put the texts in
    texts_array = list()

    # Turns the dataframe objects into strings then adds them to a list so it can be analysed
    for i in range(len(texts_csv)):
        # Put the text column name from the csv file into " "
        texts_array.append(texts_csv["text"].iloc[i])

    # Puts the text and the sentiment into a dictinoray
    for text in texts_array:
        # empty dic to store params of a text
        parsed_text = {}
        # saving the text
        parsed_text["text"] = text
        # saving sentiment of a text
        parsed_text["sentiment"] = get_text_sentiment(text)
        # adding parsed text to the texts list
        texts.append(parsed_text)
    # Returns the dic
    return texts


def main():
    # Gets the texts
    texts = get_texts()
    # picking positive texts
    ptexts = [text for text in texts if text['sentiment'] == 'Positive']
    # percentage of positive texts
    print("Positive tweets percentage: {} %".format(100 * len(ptexts) / len(texts)))
    # picking neutral texts
    neutralTexts = [text for text in texts if text['sentiment'] == 'Neutral']
    # picking negative texts
    ntexts = [text for text in texts if text['sentiment'] == 'Negative']
    # percentage of negative texts
    print('Negative tweets percentage: {} %'.format(100 * len(ntexts) / len(texts)))
    # percentage of neutral texts
    print("Neutral tweets percentage: {} %".format(100 * (len(texts) - (len(ntexts) + len(ptexts))) / len(texts)))

    # printing 10 positive texts
    print("\n10 Random Positive Text:")
    for i in range(10):
        text = ptexts[randint(0 , len(ptexts))]
        print(i , ": " , text['text'])
    # printing 10 neutral texts
    print("\n10 Random Neutral Text:")
    for i in range(10):
        text = neutralTexts[randint(0 , len(neutralTexts))]
        print(i , ": " , text['text'])
    # printing 10 negative tweets
    print("\n10 Random Negative Text:")
    for i in range(10):
        text = ntexts[randint(0 , len(ntexts))]
        print(i , ": " , text['text'])


if __name__ == "__main__":
    # calling main function
    main()
