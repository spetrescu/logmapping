class LoggingStatementsProcessor:
    def __init__(self, logging_statements):
        self.logging_statements = logging_statements
        self.processed_logging_statements = None

    def _preprocess_logging_statement_log(self, logging_statement):
        logging_statement = logging_statement.rstrip()
        logging_statement = logging_statement.lstrip()
        return logging_statement

    def process_logging_statements_level_1(self):
        processed_logging_statements_level_1 = []
        raw_logging_statements_level_1 = []
        for logging_statement in self.logging_statements:
            logging_statement = self._preprocess_logging_statement_log(logging_statement)
            if (
                logging_statement.count('"') == 2
                and "{" not in logging_statement
                and "%" not in logging_statement
                and "+" not in logging_statement
                and "\"," not in logging_statement
                and "(\"" in logging_statement
            ):
                logging_statement = logging_statement.split('"')[1]
                processed_logging_statements_level_1.append(logging_statement)
            else:
                raw_logging_statements_level_1.append(logging_statement)
        return processed_logging_statements_level_1, raw_logging_statements_level_1

    def process_logging_statements_level_2(self):
        processed_logging_statements_level_2 = []
        raw_logging_statements_level_2 = []
        for logging_statement in self.logging_statements:
            if (
                logging_statement.count('"') == 2
                and "{" not in logging_statement
                and "%" not in logging_statement
                #and "+" not in logging_statement
                and logging_statement.count('+') == 1
                and "\"," not in logging_statement
                and "(\"" in logging_statement
            ):
                if "," in logging_statement.split("\"")[2] or "," in logging_statement.split("\"")[0]:
                    raw_logging_statements_level_2.append(logging_statement)
                    continue
                #logging_statement = logging_statement.split('"')[1]
                processed_logging_statements_level_2.append(logging_statement)
            else:
                raw_logging_statements_level_2.append(logging_statement)
        return processed_logging_statements_level_2, raw_logging_statements_level_2


class LogMapper:
    def __init__(self, logging_statements, runtime_logs):
        self.logging_statements = logging_statements
        self.runtime_logs = runtime_logs
    
    def log_mapping_level_1(self):
        mapped_runtime_logs_to_loggging_statements_level_1 = []
        runtime_logs_mapped_level_1 = []
        for runtime_log in self.runtime_logs:
            # print(runtime_log)
            for logging_statement in self.logging_statements:
                if logging_statement == runtime_log:
                    if logging_statement == "":
                        continue
                    mapped_runtime_logs_to_loggging_statements_level_1.append([logging_statement, runtime_log])
                    runtime_logs_mapped_level_1.append(runtime_log)
                    break
        return mapped_runtime_logs_to_loggging_statements_level_1, runtime_logs_mapped_level_1
    def log_mapping_level_2(self):
        mapped_runtime_logs_to_loggging_statements_level_2 = []
        runtime_logs_mapped_level_2 = []
        for runtime_log in self.runtime_logs:
            potential_matches = []
            for logging_statement in self.logging_statements:
                # print(logging_statement)
                if logging_statement.startswith("//"):
                    continue
                if "info(\"" in logging_statement:
                    if "\"\"" in logging_statement or "\" \"" in logging_statement:
                        continue
                    else:
                        logging_statement_static_part = logging_statement.split("\"")[1]
                else:
                    if "\"\"" in logging_statement or "\" \"" in logging_statement:
                        continue
                    # print(logging_statement)
                    logging_statement_static_part = logging_statement.split("\"")[2]
                
                if logging_statement_static_part in runtime_log:
                    if runtime_log.startswith(logging_statement_static_part) or  runtime_log.endswith(logging_statement_static_part):
                        potential_matches.append(logging_statement)
                        # break
            if not potential_matches:
                continue
            else:
                potential_matches = sorted(potential_matches, key=len)
                logging_statement_mapped = potential_matches[0]
                if logging_statement_mapped != "":
                    mapped_runtime_logs_to_loggging_statements_level_2.append([logging_statement_mapped, runtime_log])
                    runtime_logs_mapped_level_2.append(runtime_log)
                # whitespace_min_number = 10000
                # best_candidate = ""
                # a = 0
                # for match in potential_matches:
                #     if a == 0:
                #         if " " in match and match!= "":
                #             whitespace_min_number = match.count(' ')
                #             a += 1
                #             continue
                #     if " " in match and match!= "":
                #         whitespace_current_number = match.count(' ')
                #         if whitespace_current_number < whitespace_min_number:
                #             best_candidate = match
                #             whitespace_min_number = whitespace_current_number
                #     # else:
                #     #     whitespace_current_number = 0
                #     #     best_candidate = match
                # final_match = best_candidate
                # if final_match != "":
                #     mapped_runtime_logs_to_loggging_statements_level_2.append([final_match, runtime_log])
                #     runtime_logs_mapped_level_2.append(runtime_log)
        return mapped_runtime_logs_to_loggging_statements_level_2, runtime_logs_mapped_level_2
    # def log_mapping_level_2(self, runtime_logs, logging_statements):
    #     mapped_runtime_logs_to_loggging_statements_level_2 = []
    #     runtime_logs_mapped_level_2 = []

    #     for runtime_log in runtime_logs:
    #         runtime_log_split = runtime_log.split(" ")
    #         for split_part in runtime_log_split:
    #         logging_statement

    #     return mapped_runtime_logs_to_loggging_statements_level_2, runtime_logs_mapped_level_2




JAVA_LINE_TERMINATOR = ";"
JAVA_LOGGING_FORMULAE = ["LOG.info("]

JAVA_LOGGING_FORMULAE_logger = [
    "log.trace(",
    "log.debug(",
    "log.info(",
    "log.warn(",
    "log.error(",
    "log.fatal(",
]


CODE_EXTENSIONS_SPECIFIC_LANGUAGE = {"JAVA": "*.java", "Python": "*.py", "C++": "*.cpp"}

FORMULAE_LOGGING_STATEMENTS_SPECIFIC_LANGUAGE = {
    "JAVA": ["LOG.info("],
}

LINE_TERMINATOR_SPECIFIC_LANGUAGE = {
    "JAVA": ";\n",
}

DATASET_SPECIFIC_META_SEPARATORS = {
    "Hadoop": ";\n",
}


def clone_repository():
    """Clone git repository"""
    raise NotImplementedError


import os
from itertools import chain
from glob import glob
import glob
import pandas as pd
import json

from collections import Counter
from string import punctuation


def generate_log_templates_with_generic_tokens_from_raw_logging_statements(
    logging_statements,
):
    print(
        f"Now processing {len(logging_statements)} logging statements to generate log templates with generic tokens only..."
    )

    processed_lines = []
    lines = []

    raw_templates = []

    list_of_templates = logging_statements

    for line in list_of_templates:
        processed_line = line.split('"')

        if r"\{\}" in line or "{" in line or "}" in line or "{}" in line:
            continue

        if "+" in line and len(processed_line) > 3:
            if "+ " in processed_line[0] or "+" in processed_line[0]:
                processed_lines.append(line)
                raw_templates.append(line)
                continue
            else:
                entire_line = []
                for el, a in zip(processed_line, range(len(processed_line))):
                    if "LOG.info(" in el:
                        continue
                    elif "+" in el and ");" in el:
                        entire_line.append("<GENERIC_VAR>")
                    elif ");" in el:
                        continue
                    elif el.count("+") == 1:
                        continue
                    elif "+" in el and el.count("+") == 2:
                        el = el.replace("+", "").strip()
                        entire_line.append("<GENERIC_VAR>")
                    else:
                        entire_line.append(el)
                entire_line = "".join(entire_line)
                processed_lines.append(entire_line)
                raw_templates.append(line)

        # lines that have no variables
        if len(processed_line) == 3:
            if processed_line[-1] == ");":
                if "+" in processed_line[0]:
                    continue
                else:
                    processed_lines.append(processed_line[1])
                    raw_templates.append(line)

    generic_templates = list(zip(raw_templates, processed_lines))
    df = pd.DataFrame(generic_templates, columns=[["raw_template", "log_template"]])
    df = df.drop_duplicates()
    save_path = "refactored_code_output/generic_templates.csv"
    df.to_csv(save_path)
    print(
        f"Generated {len(processed_lines)} generic log templates... Can be found under {save_path}\n"
    )

    return generic_templates


def generate_log_templates_with_rich_tokens_from_raw_logging_statements(
    logging_statements,
):
    print(
        f"Now processing {len(logging_statements)} logging statements to generate log templates with generic tokens only..."
    )

    processed_lines = []
    lines = []

    raw_templates = []

    list_of_templates = logging_statements

    for line in list_of_templates:
        processed_line = line.split('"')

        if r"\{\}" in line:
            continue

        if "+" in line and len(processed_line) > 3:
            if "+ " in processed_line[0] or "+" in processed_line[0]:
                processed_lines.append(line)
                raw_templates.append(line)
                continue
            else:
                entire_line = []
                for el, a in zip(processed_line, range(len(processed_line))):
                    if "LOG.info(" in el:
                        continue
                    elif "+" in el and ");" in el:
                        if "id" in el.lower():
                            entire_line.append("<ID>")
                        else:
                            entire_line.append("<GENERIC_VAR>")
                    elif ");" in el:
                        continue
                    elif el.count("+") == 1:
                        continue
                    elif "+" in el and el.count("+") == 2:
                        el = el.replace("+", "").strip()
                        if "id" in el.lower():
                            entire_line.append("<ID>")
                        else:
                            entire_line.append("<GENERIC_VAR>")
                    else:
                        entire_line.append(el)
                entire_line = "".join(entire_line)
                processed_lines.append(entire_line)
                raw_templates.append(line)

        # lines that have no variables
        if len(processed_line) == 3:
            if processed_line[-1] == ");":
                if "+" in processed_line[0]:
                    continue
                else:
                    processed_lines.append(processed_line[1])
                    raw_templates.append(line)

    rich_templates = list(zip(raw_templates, processed_lines))
    df = pd.DataFrame(rich_templates, columns=[["raw_template", "log_template"]])
    df = df.drop_duplicates()
    save_path = "refactored_code_output/rich_templates.csv"
    df.to_csv(save_path)
    print(
        f"Generated {len(processed_lines)} rich log templates... Can be found under {save_path}\n"
    )

    return rich_templates


def find_logging_statements(files_with_logging_statements, language):

    logging_statements_found = []

    warnings_found = []

    for file in files_with_logging_statements:
        with open(file) as f:
            lines = f.readlines()

        for line, i in zip(lines, range(len(lines))):

            for formula in FORMULAE_LOGGING_STATEMENTS_SPECIFIC_LANGUAGE[language]:
                save_i = i
                if formula in line:
                    entire_line = []
                    if not line.endswith(LINE_TERMINATOR_SPECIFIC_LANGUAGE[language]):
                        entire_line.append(line.strip())
                        while True:
                            i += 1
                            warning_line = lines[i]
                            if not warning_line.endswith(
                                LINE_TERMINATOR_SPECIFIC_LANGUAGE[language]
                            ):
                                entire_line.append(warning_line.strip())
                            else:
                                entire_line.append(warning_line.strip())
                                break
                        warnings_found.append([entire_line, file.split("/")[-1]])
                        i = save_i
                    else:
                        logging_statements_found.append(
                            [line.strip(), file.split("/")[-1]]
                        )

    logging_statements_on_a_single_line = []
    logging_statements_on_multiple_lines = []

    a = 0
    for stmnt in logging_statements_found:
        logging_statements_on_a_single_line.append(stmnt[0])
        a += 1

    final_warnings = []
    a = 0
    for stmnt in warnings_found:

        entire_line = stmnt[0]
        entire_line = " ".join(entire_line)

        final_warnings.append([entire_line, stmnt[1]])
        a += 1

    a = 0
    for stmnt in final_warnings:
        logging_statements_on_multiple_lines.append(stmnt[0])
        a += 1

    logging_statements = []

    for statement in logging_statements_on_a_single_line:
        logging_statements.append(statement)

    for statement in logging_statements_on_multiple_lines:
        logging_statements.append(statement)

    print("Single-line logging statements: ", len(logging_statements_on_a_single_line))
    print(
        "Multiple-line logging statements: ", len(logging_statements_on_multiple_lines)
    )
    print("Total logging statements found: ", len(logging_statements))
    print("Unique logging statements found: ", len(list(set(logging_statements))), "\n")

    return list(set(logging_statements))


def find_code_files(path, file_extension):
    print(f"Looking for code files with the {file_extension} extension...")
    list_of_all_files = []
    for x in os.walk(path):
        for y in glob.glob(os.path.join(x[0], file_extension)):
            list_of_all_files.append(y)

    print(
        f"Found {len(list_of_all_files)} code files with the {file_extension} extension\n"
    )

    return list_of_all_files


def find_files_that_contain_logging_statements(list_of_code_files, logging_formulae):
    print("Looking for files that contain logging statements...")
    files_with_logging_statements = []

    for filename in list_of_code_files:
        file = filename
        # print(file)
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                for formula in logging_formulae:
                    if formula in line:
                        files_with_logging_statements.append(file)
    print(
        f"Found {len(list(set(files_with_logging_statements)))} files that contain logging statements\n"
    )
    return list(set(files_with_logging_statements))


def read_runtime_logs(path_to_log_dataset):
    with open(path_to_log_dataset) as f:
        lines = f.readlines()
    return lines


def remove_log_meta_information(list_of_log_messages):

    lines_no_meta_information = []

    for line in list_of_log_messages:
        if str(line).split("]")[0].lstrip().count(":") > 2:
            continue
        new_line = ":".join(str(line).split(":")[3:]).strip()
        lines_no_meta_information.append(new_line)
    lines_no_meta_information = [x for x in lines_no_meta_information if x != ""]
    return lines_no_meta_information


def find_str(string, substring):
    index = 0

    if substring in string:
        c = substring[0]
        for ch in string:
            if ch == c:
                if string[index : index + len(substring)] == substring:
                    return index, index + len(substring)
            index += 1

    return -1, -1


def match_runtime_log_to_template(runtime_logs, templates):

    raw_templates_matched = []
    processed_templates_matched = []
    runtime_logs_matched = []

    for log in runtime_logs:
        for template in templates:
            split_template = template[1].split("<GENERIC_VAR>")

            if len(split_template) > 1:

                match = []
                for split_el in split_template:
                    if split_el == "":
                        continue
                    if split_el in log:
                        match.append("match")
                    else:
                        match.append("no match")
                if len(list(set(match))) == 1 and list(set(match))[0] == "match":
                    raw_templates_matched.append(template[0])
                    processed_templates_matched.append(template[1])
                    runtime_logs_matched.append(log)

    logs_matched = list(
        zip(raw_templates_matched, processed_templates_matched, runtime_logs_matched)
    )
    df = pd.DataFrame(
        logs_matched,
        columns=[
            [
                "raw_templates_matched",
                "processed_templates_matched",
                "runtime_logs_matched",
            ]
        ],
    )
    df = df.drop_duplicates()
    save_path = "refactored_code_output/mapped_logs.csv"
    df.to_csv(save_path, index=False)
    print(
        f"Matched {len(logs_matched)} runtime logs to logging statements... Can be found under {save_path}\n"
    )

    return raw_templates_matched, processed_templates_matched, runtime_logs_matched


def create_training_data_for_ner_model(
    raw_templates_matched, processed_templates_matched, runtime_logs_matched
):

    training_data = []
    ner_char_training_data = []

    for raw, proc_temp, runt_log in zip(
        raw_templates_matched, processed_templates_matched, runtime_logs_matched
    ):
        print("Current raw template message: ", raw)
        print("Current log message: ", runt_log)
        print("Current processed template: ", proc_temp)
        save_runt = runt_log
        if "Moved tmp to done:" in runt_log:
            continue

        constants_in_template = proc_temp.split("<GENERIC_VAR>")
        constants_placed = []

        counter = 0
        a = 0
        for constant in constants_in_template:
            if constant == "":
                break
            start, end = find_str(runt_log, constant)  # [:len(constant)]
            if start != -1 and end != -1:
                constants_placed.append([constant, start + counter, end + counter])
                runt_log = runt_log[end:]
                counter += end
            # else:
            #     break

        print(constants_placed)

        indices_for_variables = []
        character_level_annotations = []

        if len(constants_placed) > 1 or "<GENERIC_VAR>" in constants_in_template:
            for i in range(len(constants_placed)):

                print(i, "Mainlen(constants_placed) - 1", len(constants_placed) - 1)
                print(i, "Mainlen(constants_placed)", len(constants_placed))

                if i == (len(constants_placed) - 1) and constants_placed[i][2] < len(
                    save_runt
                ):
                    print("len(constants_placed) - 1", len(constants_placed) - 1)
                    print("len(constants_placed)", len(constants_placed))
                    indices_for_variables.append(
                        (
                            constants_placed[i][2],
                            len(save_runt),
                            "GENERIC_VAR",
                            save_runt[constants_placed[i][2] : len(save_runt)],
                        )
                    )
                    character_level_annotations.append(
                        [constants_placed[i][2], len(save_runt)]
                    )
                elif i == (
                    len(constants_placed) - 1
                ):  # and len(constants_placed) == 1 and not constants_placed[i][2] < len(save_runt)
                    # indices_for_variables.append((constants_placed[i][2] + 1, len(save_runt), "GENERIC_VAR"))
                    break
                else:
                    # print(constants_placed[i])
                    a = constants_placed[i][2]
                    b = constants_placed[i + 1][1]
                    indices_for_variables.append((a, b, "GENERIC_VAR", save_runt[a:b]))
                    character_level_annotations.append([a, b])
                    if a > b:
                        print(constants_placed)
                    print(i, indices_for_variables)
        elif len(constants_placed) == 1 or "<GENERIC_VAR>" in constants_in_template:
            for i in range(len(constants_placed)):
                if (
                    i == (len(constants_placed) - 1) and len(constants_placed) == 1
                ):  # and not constants_placed[i][2] < len(save_runt)
                    indices_for_variables.append(
                        (
                            constants_placed[i][2],
                            len(save_runt),
                            "GENERIC_VAR",
                            save_runt[constants_placed[i][2] : len(save_runt)],
                        )
                    )
                    character_level_annotations.append(
                        [constants_placed[i][2], len(save_runt)]
                    )

        print("indices_for_variables", indices_for_variables, "\n")
        print("character_level_annotations", character_level_annotations, "\n")

        training_data.append(
            {"entities": indices_for_variables, "text": [save_runt, proc_temp, raw]}
        )

        ner_char_entry = list(save_runt)
        ner_annotations_per_char = []

        for i in range(len(ner_char_entry)):
            ner_annotations_per_char.append("O")

        for i in range(len(ner_char_entry)):

            for specific_range in character_level_annotations:
                for el in range(specific_range[0], specific_range[1]):
                    ner_annotations_per_char[el] = "VAR"

        ner_char_training_data.append(
            {"entities": [ner_char_entry, ner_annotations_per_char]}
        )

    jsonString = json.dumps(ner_char_training_data)
    jsonFile = open("refactored_code_output/ner_training_data_char.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

    for el, el2 in zip(training_data, ner_char_training_data):
        print("Entities:")
        for ent in el["entities"]:
            print(ent)
        print("Text:")
        for ent in el["text"]:
            print(ent)
        print("Entities NER char:")
        for ent in el2["entities"]:
            print(ent)
        print("\n\n")

    return training_data, ner_char_training_data


"Moved tmp to done: hdfs://msra-sa-41:9000/tmp/hadoop-yarn/staging"


def map_runtime_logs_logging_statements(
    path_to_dir_containing_codebase, path_to_log_dataset, language
):
    list_of_code_files = find_code_files(
        path=path_to_dir_containing_codebase,
        file_extension=CODE_EXTENSIONS_SPECIFIC_LANGUAGE[language],
    )

    list_of_files_that_contain_logging_statements = find_files_that_contain_logging_statements(
        list_of_code_files=list_of_code_files,
        logging_formulae=FORMULAE_LOGGING_STATEMENTS_SPECIFIC_LANGUAGE[language],
    )

    logging_statements = find_logging_statements(
        files_with_logging_statements=list_of_files_that_contain_logging_statements,
        language=language,
    )

    generic_templates = generate_log_templates_with_generic_tokens_from_raw_logging_statements(
        logging_statements
    )
    rich_templates = generate_log_templates_with_rich_tokens_from_raw_logging_statements(
        logging_statements
    )

    runtime_logs = read_runtime_logs(path_to_log_dataset)
    print("Initial:", runtime_logs[0])

    runtime_logs = remove_log_meta_information(runtime_logs)
    print("Meta removed:", runtime_logs[0])

    (
        raw_templates_matched,
        processed_templates_matched,
        runtime_logs_matched,
    ) = match_runtime_log_to_template(runtime_logs, generic_templates)

    create_training_data_for_ner_model(
        raw_templates_matched, processed_templates_matched, runtime_logs_matched
    )


#         # PROBLEMS
#         # LOG.info("                    Test ID: [" + (i + 1) + "]");,                    Test ID: [ + (i + 1) + ]
#         # "LOG.info(""Balancing bandwidth is "" + bandwidth + "" bytes/s"");",Balancing bandwidth is <ID> bytes/s
