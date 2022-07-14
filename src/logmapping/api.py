from logmapping.discover import LoggingStatementsMiner, LoggingVariablesMiner
from logmapping.preprocessing import PreprocessRuntimeLogs
from logmapping.logmapping import LoggingStatementsProcessor, LogMapper
from logmapping.postprocessing import EntityTemplateGenerator



class LogMappingApi:
    def __init__(self, source_code_dir_path, runtime_logs_dir_path, programming_language):
        self.source_code_dir_path = source_code_dir_path
        self.runtime_logs_dir_path = runtime_logs_dir_path
        self.programming_language = programming_language

        self.logging_statements_mined = None
        self.logging_variables_mined = None
        self.preprocessed_runtime_logs = None

    def mine_statements(self):
        logging_statement_miner = LoggingStatementsMiner(self.source_code_dir_path, self.programming_language)
        self.logging_statements_mined = logging_statement_miner.discover_logging_statements_in_dir()
        return self.logging_statements_mined

    def mine_variables(self):
        logging_variables_miner = LoggingVariablesMiner(self.logging_statements_mined)
        self.logging_variables_mined = logging_variables_miner.discover_logging_variables_in_list()
        return self.logging_variables_mined

    def preprocess_runtime_logs(self):
        preprocess_logs = PreprocessRuntimeLogs(self.runtime_logs_dir_path)
        list_of_log_files = preprocess_logs.list_files_in_dir()
        self.preprocessed_runtime_logs = preprocess_logs.generate_list_of_runtime_logs_in_dir()
        print("No. of logs before preprocessing:", len(self.preprocessed_runtime_logs))
        
        self.preprocessed_runtime_logs = preprocess_logs.preprocess_runtime_logs()
        print("No. of logs after preprocessing:", len(self.preprocessed_runtime_logs))

        self.preprocessed_runtime_logs = preprocess_logs.preprocess_runtime_logs_dedupicate()
        print("No. of logs after preprocessing initial deduplication:", len(self.preprocessed_runtime_logs))

        self.preprocessed_runtime_logs = preprocess_logs.remove_meta_information_hadoop()
        print("No. of logs after removing meta information:", len(self.preprocessed_runtime_logs))

        self.preprocessed_runtime_logs = list(set(self.preprocessed_runtime_logs))
        print("No. of logs after preprocessing deduplication:", len(self.preprocessed_runtime_logs))

        return self.preprocessed_runtime_logs
    
    def set_preprocessed_runtime_logs(self, runtimelogs):
        self.preprocessed_runtime_logs = runtimelogs
    
    def get_preprocessed_runtime_logs(self):
        return self.preprocessed_runtime_logs

    def process_logging_statements_level_1(self, logging_statements_mined):
        logging_statements_processor = LoggingStatementsProcessor(logging_statements_mined)
        processed_logging_statements_level_1, unprocessed_logs_level_1 = logging_statements_processor.process_logging_statements_level_1()
        return processed_logging_statements_level_1, unprocessed_logs_level_1
    
    def process_logging_statements_level_2(self, logging_statements_mined):
        logging_statements_processor = LoggingStatementsProcessor(logging_statements_mined)
        processed_logging_statements_level_2, unprocessed_logs_level_2 = logging_statements_processor.process_logging_statements_level_2()
        return processed_logging_statements_level_2, unprocessed_logs_level_2

    def map_runtime_logs_to_logging_statements_level_1(self, logging_statements):
        log_mapper_level_1 = LogMapper(logging_statements, self.preprocessed_runtime_logs)
        mapped_runtime_logs_to_loggging_statements_level_1, runtime_logs_mapped_level_1 = log_mapper_level_1.log_mapping_level_1()
        return mapped_runtime_logs_to_loggging_statements_level_1, runtime_logs_mapped_level_1

    def map_runtime_logs_to_logging_statements_level_2(self, logging_statements, runtime_logs):
        log_mapper_level_2 = LogMapper(logging_statements, runtime_logs)
        mapped_runtime_logs_to_loggging_statements_level_2, runtime_logs_mapped_level_2 = log_mapper_level_2.log_mapping_level_2()
        return mapped_runtime_logs_to_loggging_statements_level_2, runtime_logs_mapped_level_2

def mine_logging_statements(source_code_dir_path, runtime_logs_file_path, programming_language):
    api = LogMappingApi(source_code_dir_path, runtime_logs_file_path, programming_language)
    logging_statements_mined = api.mine_statements()
    
    print("Logging statements discovered: ")
    # for logging_statement in logging_statements_mined:
    #     print(logging_statement)
    # return logging_statements_mined

def mine_variables(source_code_dir_path, runtime_logs_file_path, programming_language):
    api = LogMappingApi(source_code_dir_path, runtime_logs_file_path, programming_language)
    logging_statements_mined = api.mine_statements()
    logging_variables_mined = api.mine_variables()

    print("Logging variables discovered: ")
    # for logging_variable in logging_variables_mined:
    #     print(logging_variable)

def map_runtime_to_logging_statements(source_code_dir_path, runtime_logs_file_path, programming_language):
    api = LogMappingApi(source_code_dir_path, runtime_logs_file_path, programming_language)
    logging_statements_mined = api.mine_statements()
    logging_variables_mined = api.mine_variables()
    runtime_logs = api.preprocess_runtime_logs()

    processed_logging_statements_level_1, raw_logging_statements_level_1 = api.process_logging_statements_level_1(logging_statements_mined)

    mapped_runtime_logs_to_loggging_statements_level_1, runtime_logs_mapped_level_1 = api.map_runtime_logs_to_logging_statements_level_1(processed_logging_statements_level_1)

    for el in mapped_runtime_logs_to_loggging_statements_level_1:
        print(el)

    for el in runtime_logs_mapped_level_1:
        print(el)
    
    runtime_logs_before_level_1_mapping = api.get_preprocessed_runtime_logs()
    print("Before level 1 mapping: ", len(runtime_logs_before_level_1_mapping))

    runtime_logs_after_level_1_mapping = list(set(runtime_logs_before_level_1_mapping)^set(runtime_logs_mapped_level_1))
    api.set_preprocessed_runtime_logs(runtime_logs_after_level_1_mapping)
    print("After level 1 mapping: ", len(api.get_preprocessed_runtime_logs()))
    print("Number of matches found for level 1: ", len(mapped_runtime_logs_to_loggging_statements_level_1))
    # print("Len initial", len(logging_statements_mined))
    # print("Len proc", len(processed_logging_statements_level_1))
    # print("Len unproc", len(unprocessed_logs_level_1))
    
    processed_logging_statements_level_2, raw_logging_statements_level_2 = api.process_logging_statements_level_2(raw_logging_statements_level_1)
    print("Level 2 templates considered: ", len(processed_logging_statements_level_2))
    for el in processed_logging_statements_level_2:
        print(el)
        break

    mapped_runtime_logs_to_loggging_statements_level_2, runtime_logs_mapped_level_2 = api.map_runtime_logs_to_logging_statements_level_2(processed_logging_statements_level_2, runtime_logs_after_level_1_mapping)
    azmnsjdf = 0
    for el in mapped_runtime_logs_to_loggging_statements_level_2:
        print(el)
        azmnsjdf += 1
        if azmnsjdf == 1000:
            break
    print("Level 2 templates found:", len(mapped_runtime_logs_to_loggging_statements_level_2))
 
    entity_template_generator = EntityTemplateGenerator(mapped_runtime_logs_to_loggging_statements_level_2, "")
    runtime_log, ground_truth, entity_log_template, variable_entity_type_array = entity_template_generator.generate_gdth()
    
    import os
    with open('entity_dataset_hadoop_level_2.csv', 'w') as file:
        #file.write(f"runtime_log,ground_truth,entity_log_template,variable_entity_type_array{os.linesep}")
        for r, g, e, v in zip(runtime_log, ground_truth, entity_log_template, variable_entity_type_array):
        #el in mapped_runtime_logs_to_loggging_statements_level_2:
            file.write(f"{r},{g},{e},{v}{os.linesep}")
            print(f"{g},{e}")
    
    # azmnsjdf = 0
    # for temp in processed_logging_statements_level_2:
    #     print(temp)
    #     azmnsjdf += 1
        # if azmnsjdf == 200:
        #     break
    # for el in processed_logging_statements_level_2:

    #map level 1 complexity logs



    # preprocess logs in dir
    # process logs 
    # return list of logs /Users/stefanpetrescu/DELFT/Thesis/reeerm/hadoop_all.txt
    return 0
