class LoggingStatementsMiner:
    def __init__(self, dir_path, programming_language):
        self.dir_path = dir_path
        self.programming_language = programming_language
        self.code_files = None
        self.raw_logging_statements = None
    
    def discover_code_files(self):
        self.code_files = ["Code.java"]

    def discover_logging_statements_in_single_file(self, file_path):
        logging_statements = []
        log_example = "Runtime log."
        logging_statements.append(log_example)

        return logging_statements

    def discover_logging_statements_in_dir(self):
        logging_statements_in_dir = []
        self.discover_code_files()

        for code_file in self.code_files:
            logging_statements_in_file = self.discover_logging_statements_in_single_file(code_file)
            for logging_stmnt in logging_statements_in_file:
                logging_statements_in_dir.append(logging_stmnt)

        return logging_statements_in_dir