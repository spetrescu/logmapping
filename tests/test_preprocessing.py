from logmapping.preprocessing import PreprocessRuntimeLogs


def test_removal_of_empty_elements_hadoop():
    """Test that the generated elements in runtime logs are correct"""
    process_runtime_logs = PreprocessRuntimeLogs("")
    process_runtime_logs.runtime_logs_in_dir = [
        "2015 Launching attempt_14\n",
        " ",
        "2015 Launching attempt_14 ",
        "2015 Launching attempt_13",
        "",
        " ",
    ]
    expected = [
        "2015 Launching attempt_14",
        "2015 Launching attempt_14",
        "2015 Launching attempt_13",
    ]
    actual = process_runtime_logs.preprocess_runtime_logs()
    assert actual == expected, "Test ran successfully!"


def test_line_strip_hadoop():
    """Test that the generated elements in runtime logs are correct"""
    process_runtime_logs = PreprocessRuntimeLogs("")
    process_runtime_logs.runtime_logs_in_dir = [
        "2015 Launching attempt_14\n",
        " ",
        "2015 Launching attempt_14 ",
        "2015 Launching attempt_13\n",
        "2015 Launching attempt  ",
    ]
    expected = [
        "2015 Launching attempt_14",
        "2015 Launching attempt_14",
        "2015 Launching attempt_13",
        "2015 Launching attempt",
    ]
    actual = process_runtime_logs.preprocess_runtime_logs()
    assert actual == expected, "Test ran successfully!"
