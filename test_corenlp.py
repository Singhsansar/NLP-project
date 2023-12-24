from nlplogic.corenlp import get_phrases, search_wiki, get_wiki_summary, text_blob
import fire 
def test_get_phrases():
    assert 'golden state' in get_phrases("Golden State Warriors") 