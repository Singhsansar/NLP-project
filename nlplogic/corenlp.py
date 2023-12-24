from textblob import TextBlob
import wikipedia


def search_wiki(query):
    """Searching Wikipedia:"""

    print(f"Searching Wikipedia for {query}...")
    return wikipedia.search(query)


def get_wiki_summary(query):
    """Summarize wikipedia:"""

    print(f"Getting Wikipedia summary for {query}...")
    return wikipedia.summary(query)


def text_blob(text):
    blob = TextBlob(text)
    return blob


def get_phrases(text):
    """Searching a wikipedia page for phrases..."""
    text = get_wiki_summary(text)
    blob = TextBlob(text)
    pharses = blob.noun_phrases
    return pharses


# golden_state_warriors_text = wikipedia.summary("Golden State Warriors")
# blob = TextBlob(golden_state_warriors_text)
