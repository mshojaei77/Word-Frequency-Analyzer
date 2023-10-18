import pytest
from unittest.mock import patch
from project import analyze, get_text, get_word_count, get_most_repeated_words

def test_analyze():
    # Test with valid inputs
    assert analyze('1', '2023') is None  # Since this function prints and writes to file, we can't capture a return value

def test_get_text():
    url = 'https://edition.cnn.com/article/sitemap-2023-01.html'
    text = get_text(url)
    assert isinstance(text, str)  # The function should return a string

def test_get_word_count():
    url = 'https://edition.cnn.com/article/sitemap-2023-01.html'
    word_count = get_word_count(url)
    assert isinstance(word_count, dict)  # The function should return a dictionary

@patch('project.get_text', return_value='some text')
def test_get_most_repeated_words(mock_get_text):
    url = 'https://edition.cnn.com/article/sitemap-2023-01.html'
    most_repeated_words = get_most_repeated_words(url)
    assert isinstance(most_repeated_words, list)  # The function should return a list
