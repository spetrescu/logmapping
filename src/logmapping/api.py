from logmapping.discover import LoggingStatementsMiner

class LogMappingApi:
    def __init__(self, source_code_dir_path, runtime_logs_file_path, programming_language):
        self.source_code_dir_path = source_code_dir_path
        self.runtime_logs_file_path = runtime_logs_file_path
        self.programming_language = runtime_logs_file_path

        self.logging_statements_mined = None

    def mine_statements(self):
        logging_statement_miner = LoggingStatementsMiner(self.source_code_dir_path, self.programming_language)
        self.logging_statements_mined = logging_statement_miner.discover_logging_statements_in_dir()
        return self.logging_statements_mined

def mine_logging_statements(source_code_dir_path, runtime_logs_file_path, programming_language):
    api = LogMappingApi(source_code_dir_path, runtime_logs_file_path, programming_language)
    logging_statements_mined = api.mine_statements()
    
    print("Logging statements discovered: ")
    for logging_statement in logging_statements_mined:
        print(logging_statement)
    return logging_statements_mined

def mine_variables():
    pass

def map_runtime_to_logging_statements():
    pass
