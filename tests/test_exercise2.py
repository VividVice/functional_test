import pytest
import sys

sys.path.append(r'D:\coding\functional_test')

from exercice2 import StringAnalyzer

@pytest.fixture
def analyzer():
    return StringAnalyzer("Hello World!\nThis is a test string.\n12345")

def test_count_vowels(analyzer):
    result = analyzer.count_vowels()
    assert result == 6

def test_count_consonants(analyzer):
    result = analyzer.count_consonants()
    assert result == 11

def test_count_digits(analyzer):
    result = analyzer.count_digits()
    assert result == 5

def test_count_words(analyzer):
    result = analyzer.count_words()
    assert result == 7

def test_count_lines(analyzer):
    result = analyzer.count_lines()
    assert result == 3
