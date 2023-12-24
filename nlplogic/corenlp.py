from textblob import TextBlob
import wikipedia

golden_state_warriors_text = wikipedia.summary("Golden State Warriors")
print(golden_state_warriors_text)
blob = TextBlob(golden_state_warriors_text)
print(blob.tags)
print(blob.noun_phrases)
print(blob.sentiment)
print(blob.sentences)
print(blob.words)
