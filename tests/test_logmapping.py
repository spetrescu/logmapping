from logmapping.logmapping import find_str
from collections import Counter

def test_count_words_substring_not_in_string():
    """Test word counting from a file."""
    expected = (-1, -1)
    string = "runt_log"
    substring = "constant"
    actual = find_str(string=string, substring=substring)
    assert actual == expected, "Test ran successfully!"

def test_count_words_substring_is_in_string():
    """Test word counting from a file."""
    expected = (0, 1)
    
    string = "runt_log"
    substring = "r"
    actual = find_str(string=string, substring=substring)
    assert actual == expected, "Test ran successfully!"