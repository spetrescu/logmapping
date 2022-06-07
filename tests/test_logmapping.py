from logmapping.logmapping import find_str, create_training_data_for_ner_model
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

def test_create_training_data_for_ner_model():
    """Test if ner data is correct."""

    raw_templates_matched = ["LOG.info(\"MapCompletionEvents request from \" + taskAttemptID.toString() + \". startIndex \" + abc);\""]
    proc_template = ["MapCompletionEvents request from <GENERIC_VAR>. startIndex <GENERIC_VAR>"]
    runtime_messag= ["MapCompletionEvents request from attempt_1445062781478_0011_r_000000_0. startIndex 123"]
    
    expected = [{"entities": [(33, 70, 'GENERIC_VAR', 'ttempt_1445062781478_0011_r_000000_0'), (83, 86, 'GENERIC_VAR', '123')], "text": ["MapCompletionEvents request from attempt_1445062781478_0011_r_000000_0. startIndex 123", 
                                                "MapCompletionEvents request from <GENERIC_VAR>. startIndex <GENERIC_VAR>",  
                                                "LOG.info(\"MapCompletionEvents request from \" + taskAttemptID.toString() + \". startIndex \" + abc);\"", ]}]

    actual = create_training_data_for_ner_model(raw_templates_matched=raw_templates_matched, processed_templates_matched=proc_template, runtime_logs_matched=runtime_messag)

    print("actual", actual, "\n")
    print("expected", expected)

    ranges = []
    for range in expected:
        for entity in range["entities"]:
            beinging, end, _, _ = entity
            ranges.append([beinging, end])

    assert actual == expected, "NER test ran successfully!"