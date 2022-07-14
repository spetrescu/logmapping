import os
from glob import glob
from logmapping.utils import CODE_EXTENSIONS_SPECIFIC_LANGUAGE, FORMULAE_LOGGING_STATEMENTS_SPECIFIC_LANGUAGE, LINE_TERMINATOR_SPECIFIC_LANGUAGE

class LoggingStatementsMiner:
    def __init__(self, dir_path, programming_language):
        self.dir_path = dir_path
        self.programming_language = programming_language
        self.code_files = None
        self.raw_logging_statements = None
        self.language_code_file_extension = None
    
    def discover_code_files(self):
        self.language_code_file_extension = CODE_EXTENSIONS_SPECIFIC_LANGUAGE[self.programming_language]
        print(f"Looking for code files with the {self.language_code_file_extension} extension...")
        list_of_all_files = []
        for x in os.walk(self.dir_path):
            for y in glob(os.path.join(x[0], self.language_code_file_extension)):
                list_of_all_files.append(y)
        print(f"Found {len(list_of_all_files)} code files with the {self.language_code_file_extension} extension\n")
        self.code_files = list_of_all_files

    def discover_logging_statements_in_single_file(self, file_path):
        logging_statements_found = []
        warnings_found = []

        with open(file_path) as f:
            lines = f.readlines()
            for line, i in zip(lines, range(len(lines))):
                for formula in FORMULAE_LOGGING_STATEMENTS_SPECIFIC_LANGUAGE[self.programming_language]:
                    save_i = i
                    if formula in line:
                        entire_line = []
                        if not line.endswith(LINE_TERMINATOR_SPECIFIC_LANGUAGE[self.programming_language]):
                            entire_line.append(line.strip())
                            while True:
                                i += 1
                                warning_line = lines[i]
                                if not warning_line.endswith(LINE_TERMINATOR_SPECIFIC_LANGUAGE[self.programming_language]):
                                    entire_line.append(warning_line.strip())
                                else:
                                    entire_line.append(warning_line.strip())
                                    break
                            warnings_found.append([entire_line, file_path.split("/")[-1]])
                            i = save_i
                        else:
                            logging_statements_found.append([line.strip(), file_path.split("/")[-1]])
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
            entire_line = ' '.join(entire_line)

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
        return list(set(logging_statements))

    def discover_logging_statements_in_dir(self):
        logging_statements_in_dir = []
        self.discover_code_files()
        for code_file in self.code_files:
            logging_statements_in_file = self.discover_logging_statements_in_single_file(code_file)
            for logging_stmnt in logging_statements_in_file:
                logging_statements_in_dir.append(logging_stmnt)

        print("Total logging statements found: ", len(logging_statements_in_dir))
        print("Unique logging statements found: ", len(list(set(logging_statements_in_dir))), "\n")
        return list(set(logging_statements_in_dir))

class LoggingVariablesMiner:
    def __init__(self, logging_statements):
        self.logging_statements = logging_statements


    def discover_logging_variables_in_list(self):
        variables_found = []
        for stmnt in self.logging_statements:
            
            #contains {} but no +
            if "{" in stmnt and "+" not in stmnt:
                #contains only simple variables #example: LOG.info("POST: createService = {} user = {}", service, userUgi);
                if "\"," in stmnt:
                    split_log = stmnt.split("\",")
                    after_comma = ''.join(split_log[1:])
                    if "." in after_comma or "(" in after_comma or "?" in after_comma or "/" in after_comma or "{" in after_comma or "}" in after_comma or "[" in after_comma:
                        print("XXX Complicated")
                    else:
                        # processing simple found variables
                        after_comma = after_comma.replace(");", "")
                        after_comma = after_comma.strip()
                        if ")" in after_comma:
                            after_comma = after_comma.replace(")", "")

                        if "," not in after_comma:
                            variables_found.append(after_comma)
                        else:
                            variables_in_current_line = after_comma.split(",")
                            for var in variables_in_current_line:
                                if var == "":
                                    continue
                                else:
                                    var = var.strip()
                                    variables_found.append(var)
                        print(f"XXX Simple logged variable -{after_comma}-")
                else:
                    print(stmnt)
            elif "{" in stmnt and "+" in stmnt:
                print("XXX +++")
            else:
                stmnt_split_info = stmnt.split(".info(\"")
                stmnt_split_info = ''.join(stmnt_split_info[1:])
                
                variables_current = []

                if "+" in stmnt_split_info:
                    stmnt_split_info = stmnt_split_info.split("+")
                    for splt in stmnt_split_info:
                        if "\""in splt:
                            continue
                        else:
                            #append only simple variables, namely that do not contain any functions/symbols
                            if "." in splt or "(" in splt or "?" in splt or "/" in splt or "{" in splt or "}" in splt or "[" in splt or "," in splt:
                                continue
                            else:
                                variables_current.append(splt.strip())
                    
                    #processing found variables and appending to list
                    if len(variables_current) > 0:
                        for vrb in variables_current:
                            if vrb == "":
                                continue
                            else:
                                vrb = vrb.strip()
                                if ")" in vrb:
                                    vrb = vrb.replace(")", "")
                                if ";" in vrb:
                                    vrb = vrb.replace(";", "")
                                variables_found.append(vrb)
                        print(f"No curly simple -{variables_current}-")
                    else:
                        print("XXX Complicated")
                else:
                    continue
                    print("XXX Simple log") #Simple log, without + in logging statement
        return variables_found