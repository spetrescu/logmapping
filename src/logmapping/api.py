from logmapping.discover import LoggingStatementsMiner, LoggingVariablesMiner
from logmapping.openstack import LogMapperOpenStack
from logmapping.preprocessing import PreprocessRuntimeLogs
from logmapping.logmapping import LoggingStatementsProcessor, LogMapper
from logmapping.postprocessing import EntityTemplateGenerator
from logmapping.spark import LogMapperSpark
from logmapping.zookeeper import LogMapperZookeeper
from logmapping.openstack import LogMapperOpenStack
from logmapping.linux import LogMapperLinux
from logmapping.apache import LogMapperApache
from logmapping.spark import LogMapperSpark


class LogMappingApi:
    def __init__(
        self, source_code_dir_path, runtime_logs_dir_path, programming_language
    ):
        self.source_code_dir_path = source_code_dir_path
        self.runtime_logs_dir_path = runtime_logs_dir_path
        self.programming_language = programming_language

        self.logging_statements_mined = None
        self.logging_variables_mined = None
        self.preprocessed_runtime_logs = None

    def mine_statements(self):
        logging_statement_miner = LoggingStatementsMiner(
            self.source_code_dir_path, self.programming_language
        )
        self.logging_statements_mined = (
            logging_statement_miner.discover_logging_statements_in_dir()
        )
        return self.logging_statements_mined

    def mine_variables(self):
        logging_variables_miner = LoggingVariablesMiner(self.logging_statements_mined)
        self.logging_variables_mined = (
            logging_variables_miner.discover_logging_variables_in_list()
        )
        return self.logging_variables_mined

    def preprocess_runtime_logs_spark(self):
        pass

    def preprocess_runtime_logs(self):
        preprocess_logs = PreprocessRuntimeLogs(self.runtime_logs_dir_path)
        list_of_log_files = preprocess_logs.list_files_in_dir()
        self.preprocessed_runtime_logs = (
            preprocess_logs.generate_list_of_runtime_logs_in_dir()
        )
        print("No. of logs before preprocessing:", len(self.preprocessed_runtime_logs))

        self.preprocessed_runtime_logs = preprocess_logs.preprocess_runtime_logs()
        print("No. of logs after preprocessing:", len(self.preprocessed_runtime_logs))

        self.preprocessed_runtime_logs = (
            preprocess_logs.preprocess_runtime_logs_dedupicate()
        )
        print(
            "No. of logs after preprocessing initial deduplication:",
            len(self.preprocessed_runtime_logs),
        )

        self.preprocessed_runtime_logs = (
            preprocess_logs.remove_meta_information_hadoop()
        )
        print(
            "No. of logs after removing meta information:",
            len(self.preprocessed_runtime_logs),
        )

        self.preprocessed_runtime_logs = list(set(self.preprocessed_runtime_logs))
        print(
            "No. of logs after preprocessing deduplication:",
            len(self.preprocessed_runtime_logs),
        )

        return self.preprocessed_runtime_logs

    def set_preprocessed_runtime_logs(self, runtimelogs):
        self.preprocessed_runtime_logs = runtimelogs

    def get_preprocessed_runtime_logs(self):
        return self.preprocessed_runtime_logs

    def process_logging_statements_level_1(self, logging_statements_mined):
        logging_statements_processor = LoggingStatementsProcessor(
            logging_statements_mined
        )
        (
            processed_logging_statements_level_1,
            unprocessed_logs_level_1,
        ) = logging_statements_processor.process_logging_statements_level_1()
        return processed_logging_statements_level_1, unprocessed_logs_level_1

    def process_logging_statements_level_2(self, logging_statements_mined):
        logging_statements_processor = LoggingStatementsProcessor(
            logging_statements_mined
        )
        (
            processed_logging_statements_level_2,
            unprocessed_logs_level_2,
        ) = logging_statements_processor.process_logging_statements_level_2()
        return processed_logging_statements_level_2, unprocessed_logs_level_2

    def process_logging_statements_level_3(self, logging_statements_mined):
        logging_statements_processor = LoggingStatementsProcessor(
            logging_statements_mined
        )
        (
            processed_logging_statements_level_3,
            unprocessed_logs_level_3,
        ) = logging_statements_processor.process_logging_statements_level_3()
        return processed_logging_statements_level_3, unprocessed_logs_level_3

    def map_runtime_logs_to_logging_statements_level_1(self, logging_statements):
        log_mapper_level_1 = LogMapper(
            logging_statements, self.preprocessed_runtime_logs
        )
        (
            mapped_runtime_logs_to_loggging_statements_level_1,
            runtime_logs_mapped_level_1,
        ) = log_mapper_level_1.log_mapping_level_1()
        return (
            mapped_runtime_logs_to_loggging_statements_level_1,
            runtime_logs_mapped_level_1,
        )

    def map_runtime_logs_to_logging_statements_level_2(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_2 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_2,
            runtime_logs_mapped_level_2,
        ) = log_mapper_level_2.log_mapping_level_2()
        return (
            mapped_runtime_logs_to_loggging_statements_level_2,
            runtime_logs_mapped_level_2,
        )

    def map_runtime_logs_to_logging_statements_level_3(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_3 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_3,
            runtime_logs_mapped_level_3,
        ) = log_mapper_level_3.log_mapping_level_3()
        return (
            mapped_runtime_logs_to_loggging_statements_level_3,
            runtime_logs_mapped_level_3,
        )

    def map_runtime_logs_to_logging_statements_level_4(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_4 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_4,
            runtime_logs_mapped_level_4,
        ) = log_mapper_level_4.log_mapping_level_4()
        return (
            mapped_runtime_logs_to_loggging_statements_level_4,
            runtime_logs_mapped_level_4,
        )

    def map_runtime_logs_to_logging_statements_level_5(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_5 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_5,
            runtime_logs_mapped_level_5,
        ) = log_mapper_level_5.log_mapping_level_5()
        return (
            mapped_runtime_logs_to_loggging_statements_level_5,
            runtime_logs_mapped_level_5,
        )

    def map_runtime_logs_to_logging_statements_level_6(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_6 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_6,
            runtime_logs_mapped_level_6,
        ) = log_mapper_level_6.log_mapping_level_6()
        return (
            mapped_runtime_logs_to_loggging_statements_level_6,
            runtime_logs_mapped_level_6,
        )
    
    def map_runtime_logs_to_logging_statements_level_7(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_7 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_7,
            runtime_logs_mapped_level_7,
        ) = log_mapper_level_7.log_mapping_level_7()
        return (
            mapped_runtime_logs_to_loggging_statements_level_7,
            runtime_logs_mapped_level_7,
        )
    
    def map_runtime_logs_to_logging_statements_level_8(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_8 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_8,
            runtime_logs_mapped_level_8,
        ) = log_mapper_level_8.log_mapping_level_8()
        return (
            mapped_runtime_logs_to_loggging_statements_level_8,
            runtime_logs_mapped_level_8,
        )

    def map_runtime_logs_to_logging_statements_level_9(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_9 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_9,
            runtime_logs_mapped_level_9,
        ) = log_mapper_level_9.log_mapping_level_9(9)
        return (
            mapped_runtime_logs_to_loggging_statements_level_9,
            runtime_logs_mapped_level_9,
        )

    def map_runtime_logs_to_logging_statements_level_10(
        self, logging_statements, runtime_logs
    ):
        log_mapper_level_10 = LogMapper(logging_statements, runtime_logs)
        (
            mapped_runtime_logs_to_loggging_statements_level_10,
            runtime_logs_mapped_level_10,
        ) = log_mapper_level_10.log_mapping_level_10(10)
        return (
            mapped_runtime_logs_to_loggging_statements_level_10,
            runtime_logs_mapped_level_10,
        )



def mine_logging_statements(
    source_code_dir_path, runtime_logs_file_path, programming_language
):
    api = LogMappingApi(
        source_code_dir_path, runtime_logs_file_path, programming_language
    )
    logging_statements_mined = api.mine_statements()

    print("Logging statements discovered: ")
    # for logging_statement in logging_statements_mined:
    #     print(logging_statement)
    # return logging_statements_mined

def mine_variables(source_code_dir_path, runtime_logs_file_path, programming_language):
    api = LogMappingApi(
        source_code_dir_path, runtime_logs_file_path, programming_language
    )
    logging_statements_mined = api.mine_statements()
    logging_variables_mined = api.mine_variables()

def map_runtime_to_logging_statements(
    source_code_dir_path, runtime_logs_file_path, programming_language
):
    
        
    # SPARK
    #map_runtime_to_logging_statements("", "src/runtime_logs/Spark_logs", "Scala")
    spark = LogMapperSpark(runtime_logs_file_path)
    runtime_logs_spark= spark.get_runtime_logs()
    runtime_logs_spark = spark.remove_meta_information()
    for el in runtime_logs_spark:
        print(el)
        break
    level = 1
    print(f"Mapping level {level} Spark...")
    print(f"Total logs before level {level} mapping:", len(spark.runtime_logs_no_meta))
    spark_mapped_level_1, runtime_mapped_level_1 = spark.log_mapping_spark(level=level)
    # spark.extra_split_in_level(rule=" ")
    spark.write_mapping_to_file(level=level, type="entity")
    spark.write_mapping_to_file(level=level, type="generic")
    spark.remove_mapped_logs(mapped_logs=runtime_mapped_level_1)
    print(f"Total logs after level {level} mapping:", len(spark.runtime_logs_no_meta))

    level = 2
    print(f"Mapping level {level} Spark...")
    print(f"Total logs before level {level} mapping:", len(spark.runtime_logs_no_meta))
    spark_mapped_level_2, runtime_mapped_level_2 = spark.log_mapping_spark(level=level)
    # spark.extra_split_in_level(rule=" ")
    spark.write_mapping_to_file(level=level, type="entity")
    spark.write_mapping_to_file(level=level, type="generic")
    spark.remove_mapped_logs(mapped_logs=runtime_mapped_level_2)
    print(f"Total logs after level {level} mapping:", len(spark.runtime_logs_no_meta))
    

    level = 3
    print(f"Mapping level {level} Spark...")
    print(f"Total logs before level {level} mapping:", len(spark.runtime_logs_no_meta))
    spark_mapped_level_3, runtime_mapped_level_3 = spark.log_mapping_spark(level=level)
    # spark.extra_split_in_level(rule=" ")
    spark.write_mapping_to_file(level=level, type="entity")
    spark.write_mapping_to_file(level=level, type="generic")
    spark.remove_mapped_logs(mapped_logs=runtime_mapped_level_3)
    print(f"Total logs after level {level} mapping:", len(spark.runtime_logs_no_meta))
    
    # # APACHE
    # #map_runtime_to_logging_statements("", "src/runtime_logs/Apache.log", "C")
    # apache = LogMapperApache(runtime_logs_file_path)
    # runtime_logs_apache= apache.get_runtime_logs()
    # runtime_logs_apache = apache.remove_meta_information()
    # level = 1
    # print(f"Mapping level {level} Apache...")
    # print(f"Total logs before level {level} mapping:", len(apache.runtime_logs_no_meta))
    # apache_mapped_level_1, runtime_mapped_level_1 = apache.log_mapping_apache(level=level)
    # # apache.extra_split_in_level(rule=" ")
    # apache.write_mapping_to_file(level=level, type="entity")
    # apache.write_mapping_to_file(level=level, type="generic")
    # apache.remove_mapped_logs(mapped_logs=runtime_mapped_level_1)
    # print(f"Total logs after level {level} mapping:", len(apache.runtime_logs_no_meta))

    ## LINUX
    # map_runtime_to_logging_statements("", "src/runtime_logs/Linux.log", "C")
    # linux = LogMapperLinux(runtime_logs_file_path)
    # runtime_logs_linux= linux.get_runtime_logs()
    # runtime_logs_linux = linux.remove_meta_information()
    # level = 1
    # print(f"Mapping level {level} Linux...")
    # print(f"Total logs before level {level} mapping:", len(linux.runtime_logs_no_meta))
    # linux_mapped_level_1, runtime_mapped_level_1 = linux.log_mapping_linux(level=level)
    # linux.extra_split_in_level(rule=" ")
    # linux.write_mapping_to_file(level=level, type="entity")
    # linux.write_mapping_to_file(level=level, type="generic")
    # linux.remove_mapped_logs(mapped_logs=runtime_mapped_level_1)
    # print(f"Total logs after level {level} mapping:", len(linux.runtime_logs_no_meta))


    # ## OPENSTACK
    # # map_runtime_to_logging_statements("", "src/runtime_logs/openstack_runtime_logs.log", "PYTHON")
    # openstack = LogMapperOpenStack(runtime_logs_file_path)
    # runtime_logs_openstack= openstack.get_runtime_logs()
    # runtime_logs_openstack = openstack.remove_meta_information()
    # level = 1
    # print(f"Mapping level {level} OpenStack...")
    # print(f"Total logs before level {level} mapping:", len(openstack.runtime_logs_no_meta))
    # openstack_mapped_level_1, runtime_mapped_level_1 = openstack.log_mapping_openstack(level=level)
    # openstack.extra_split_in_level(rule="]")
    # openstack.write_mapping_to_file(level=level, type="entity")
    # openstack.write_mapping_to_file(level=level, type="generic")
    # openstack.remove_mapped_logs(mapped_logs=runtime_mapped_level_1)
    # print(f"Total logs after level {level} mapping:", len(openstack.runtime_logs_no_meta))

    # level = 2
    # print(f"Mapping level {level} OpenStack...")
    # print(f"Total logs before level {level} mapping:", len(openstack.runtime_logs_no_meta))
    # openstack_mapped_level_2, runtime_mapped_level_2 = openstack.log_mapping_openstack(level=level)
    # openstack.extra_split_in_level(rule="]")
    # openstack.write_mapping_to_file(level=level, type="entity")
    # openstack.write_mapping_to_file(level=level, type="generic")
    # openstack.remove_mapped_logs(mapped_logs=runtime_mapped_level_2)
    # print(f"Total logs after level {level} mapping:", len(openstack.runtime_logs_no_meta))

    # level = 3
    # print(f"Mapping level {level} OpenStack...")
    # print(f"Total logs before level {level} mapping:", len(openstack.runtime_logs_no_meta))
    # openstack_mapped_level_3, runtime_mapped_level_3 = openstack.log_mapping_openstack(level=level)
    # openstack.extra_split_in_level(rule="]")
    # openstack.write_mapping_to_file(level=level, type="entity")
    # openstack.write_mapping_to_file(level=level, type="generic")
    # openstack.remove_mapped_logs(mapped_logs=runtime_mapped_level_3)
    # print(f"Total logs after level {level} mapping:", len(openstack.runtime_logs_no_meta))

    # level = 4
    # print(f"Mapping level {level} OpenStack...")
    # print(f"Total logs before level {level} mapping:", len(openstack.runtime_logs_no_meta))
    # openstack_mapped_level_4, runtime_mapped_level_4 = openstack.log_mapping_openstack(level=level)
    # openstack.extra_split_in_level(rule="]")
    # openstack.write_mapping_to_file(level=level, type="entity")
    # openstack.write_mapping_to_file(level=level, type="generic")
    # openstack.remove_mapped_logs(mapped_logs=runtime_mapped_level_4)
    # print(f"Total logs after level {level} mapping:", len(openstack.runtime_logs_no_meta))

    # amsdf = 0
    # for el in openstack.runtime_logs_no_meta:
    #     amsdf += 1
    #     print(el)
    #     if amsdf == 5000:
    #         break

    ## ZOOKEEPER
    #map_runtime_to_logging_statements("", "src/runtime_logs/Zookeeper.log", "JAVA")
    # zookeeper = LogMapperZookeeper(runtime_logs_file_path)
    # runtime_logs_zookeeper = zookeeper.get_runtime_logs()
    # runtime_logs_zookeeper = zookeeper.remove_meta_information()
    
    # print("Mapping level 1 Zookeeper...")
    # print("Total logs before level 1 mapping:", len(zookeeper.runtime_logs_no_meta))
    # zookeper_mapped_level_1, runtime_mapped_level_1 = zookeeper.log_mapping_zookeeper(level=1)
    # zookeeper.write_mapping_to_file(level=1, type="entity")
    # zookeeper.write_mapping_to_file(level=1, type="generic")
    # zookeeper.remove_mapped_logs(mapped_logs=runtime_mapped_level_1)
    # print("Total logs after level 1 mapping:", len(zookeeper.runtime_logs_no_meta))

    # print("Mapping level 2 Zookeeper...")
    # print("Total logs before level 2 mapping:", len(zookeeper.runtime_logs_no_meta))
    # zookeper_mapped_level_2, runtime_mapped_level_2 = zookeeper.log_mapping_zookeeper(level=2)
    # zookeeper.write_mapping_to_file(level=2, type="entity")
    # zookeeper.write_mapping_to_file(level=2, type="generic")
    # zookeeper.remove_mapped_logs(mapped_logs=runtime_mapped_level_2)
    # print("Total logs after level 2 mapping:", len(zookeeper.runtime_logs_no_meta))

    # print("Mapping level 3 Zookeeper...")
    # print("Total logs before level 3 mapping:", len(zookeeper.runtime_logs_no_meta))
    # zookeper_mapped_level_3, runtime_mapped_level_3 = zookeeper.log_mapping_zookeeper(level=3)
    # zookeeper.write_mapping_to_file(level=3, type="entity")
    # zookeeper.write_mapping_to_file(level=3, type="generic")
    # zookeeper.remove_mapped_logs(mapped_logs=runtime_mapped_level_3)
    # print("Total logs after level 3 mapping:", len(zookeeper.runtime_logs_no_meta))

    # print("Mapping level 4 Zookeeper...")
    # print("Total logs before level 4 mapping:", len(zookeeper.runtime_logs_no_meta))
    # zookeper_mapped_level_4, runtime_mapped_level_4 = zookeeper.log_mapping_zookeeper(level=4)
    # zookeeper.write_mapping_to_file(level=4, type="entity")
    # zookeeper.write_mapping_to_file(level=4, type="generic")
    # zookeeper.remove_mapped_logs(mapped_logs=runtime_mapped_level_4)
    # print("Total logs after level 4 mapping:", len(zookeeper.runtime_logs_no_meta))

    # print("Mapping level 5 Zookeeper...")
    # print("Total logs before level 5 mapping:", len(zookeeper.runtime_logs_no_meta))
    # zookeper_mapped_level_5, runtime_mapped_level_5 = zookeeper.log_mapping_zookeeper(level=5)
    # zookeeper.write_mapping_to_file(level=5, type="entity")
    # zookeeper.write_mapping_to_file(level=5, type="generic")
    # zookeeper.remove_mapped_logs(mapped_logs=runtime_mapped_level_5)
    # print("Total logs after level 5 mapping:", len(zookeeper.runtime_logs_no_meta))

    # print("Mapping level 6 Zookeeper...")
    # print("Total logs before level 6 mapping:", len(zookeeper.runtime_logs_no_meta))
    # zookeper_mapped_level_6, runtime_mapped_level_6 = zookeeper.log_mapping_zookeeper(level=6)
    # zookeeper.write_mapping_to_file(level=6, type="entity")
    # zookeeper.write_mapping_to_file(level=6, type="generic")
    # zookeeper.remove_mapped_logs(mapped_logs=runtime_mapped_level_6)
    # print("Total logs after level 6 mapping:", len(zookeeper.runtime_logs_no_meta))

    # print("Mapping level 7 Zookeeper...")
    # print("Total logs before level 7 mapping:", len(zookeeper.runtime_logs_no_meta))
    # zookeper_mapped_level_7, runtime_mapped_level_7 = zookeeper.log_mapping_zookeeper(level=7)
    # zookeeper.write_mapping_to_file(level=7, type="entity")
    # zookeeper.write_mapping_to_file(level=7, type="generic")
    # zookeeper.remove_mapped_logs(mapped_logs=runtime_mapped_level_7)
    # print("Total logs after level 7 mapping:", len(zookeeper.runtime_logs_no_meta))

    # level = 8
    # print(f"Mapping level {level} Zookeeper...")
    # print(f"Total logs before level {level} mapping:", len(zookeeper.runtime_logs_no_meta))
    # zookeper_mapped_level_8, runtime_mapped_level_8 = zookeeper.log_mapping_zookeeper(level=level)
    # zookeeper.write_mapping_to_file(level=level, type="entity")
    # zookeeper.write_mapping_to_file(level=level, type="generic")
    # zookeeper.remove_mapped_logs(mapped_logs=runtime_mapped_level_8)
    # print(f"Total logs after level {level} mapping:", len(zookeeper.runtime_logs_no_meta))

    # for el in zookeeper.runtime_logs_no_meta:
    #     print(el)



    ## HADOOP
    #     api = LogMappingApi(
    #     source_code_dir_path, runtime_logs_file_path, programming_language
    # )
    
    # logging_statements_mined = api.mine_statements()
    # # logging_variables_mined = api.mine_variables()
    # runtime_logs = api.preprocess_runtime_logs()
    # import csv
    #map_runtime_to_logging_statements("src/dirs/", "src/runtime_logs/Hadoop", "JAVA")
    # print("\nLEVEL 1 MAPPING...")
    # (
    #     processed_logging_statements_level_1,
    #     raw_logging_statements_level_1,
    # ) = api.process_logging_statements_level_1(logging_statements_mined)
    # print(
    #     "Level 1 templates considered for creating mapping: ",
    #     len(processed_logging_statements_level_1),
    # )
    # print("Total no. of mined templates: ", len(logging_statements_mined))
    # (
    #     mapped_runtime_logs_to_loggging_statements_level_1,
    #     runtime_logs_mapped_level_1,
    # ) = api.map_runtime_logs_to_logging_statements_level_1(
    #     processed_logging_statements_level_1
    # )
    # runtime_logs_before_level_1_mapping = api.get_preprocessed_runtime_logs()
    # print("Before level 1 mapping: ", len(runtime_logs_before_level_1_mapping))
    # runtime_logs_after_level_1_mapping = list(
    #     set(runtime_logs_before_level_1_mapping) ^ set(runtime_logs_mapped_level_1)
    # )
    # api.set_preprocessed_runtime_logs(runtime_logs_after_level_1_mapping)
    # print("After level 1 mapping: ", len(api.get_preprocessed_runtime_logs()))
    # print(
    #     "Number of matches found for level 1:",
    #     len(mapped_runtime_logs_to_loggging_statements_level_1),
    # )

    # print("\nLEVEL 2 MAPPING...")
    # (
    #     processed_logging_statements_level_2,
    #     raw_logging_statements_level_2,
    # ) = api.process_logging_statements_level_2(raw_logging_statements_level_1)
    # print(
    #     "Level 2 templates considered for creating mapping: ",
    #     len(processed_logging_statements_level_2),
    # )
    # print("Total no. of mined templates: ", len(raw_logging_statements_level_1))
    # (
    #     mapped_runtime_logs_to_loggging_statements_level_2,
    #     runtime_logs_mapped_level_2,
    # ) = api.map_runtime_logs_to_logging_statements_level_2(
    #     processed_logging_statements_level_2, runtime_logs_after_level_1_mapping
    # )
    # entity_template_generator = EntityTemplateGenerator(
    #     mapped_runtime_logs_to_loggging_statements_level_2, ""
    # )
    # (
    #     runtime_log_level_2,
    #     ground_truth_level_2,
    #     entity_log_template_level_2,
    #     generic_var_log_template_level_2,
    #     variable_entity_type_array_level_2,
    # ) = entity_template_generator.generate_gdth()
    # runtime_logs_before_level_2_mapping = runtime_logs_after_level_1_mapping
    # print("Before level 2 mapping: ", len(runtime_logs_before_level_2_mapping))
    # runtime_logs_after_level_2_mapping = list(
    #     set(runtime_logs_before_level_2_mapping) ^ set(runtime_logs_mapped_level_2)
    # )
    # print("After level 2 mapping: ", len(runtime_logs_after_level_2_mapping))
    # print(
    #     "Number of matches found for level 2: ",
    #     len(mapped_runtime_logs_to_loggging_statements_level_2),
    # )

    # err_count = 0
    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_2.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_2,
    #     ground_truth_level_2,
    #     entity_log_template_level_2,
    #     variable_entity_type_array_level_2,
    # ):
    #     if r.startswith("Processing the event EventType:"):
    #         err_count += 1
    #         continue
    #     elif r.startswith("Stopping IPC Server listener"):
    #         err_count += 1
    #         continue
    #     spamWriter.writerow([r, g, e, v])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_2.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_2,
    #     ground_truth_level_2,
    #     generic_var_log_template_level_2,
    #     variable_entity_type_array_level_2,
    # ):
    #     if r.startswith("Processing the event EventType:"):
    #         continue
    #     elif r.startswith("Stopping IPC Server listener"):
    #         continue
    #     spamWriter.writerow([r, g, e, v])

    # print("\nLEVEL 3 MAPPING...")
    # (
    #     mapped_runtime_logs_to_loggging_statements_level_3,
    #     runtime_logs_mapped_level_3,
    # ) = api.map_runtime_logs_to_logging_statements_level_3(
    #     raw_logging_statements_level_2, runtime_logs_after_level_2_mapping
    # )
    # runtime_logs_before_level_3_mapping = runtime_logs_after_level_2_mapping
    # print("Before level 3 mapping: ", len(runtime_logs_before_level_3_mapping)-err_count)
    # runtime_logs_after_level_3_mapping = list(
    #     set(runtime_logs_before_level_3_mapping) ^ set(runtime_logs_mapped_level_3)
    # )
    # print("After level 3 mapping: ", len(runtime_logs_after_level_3_mapping)-err_count)
    # print(
    #     "Number of matches found for level 3: ",
    #     len(mapped_runtime_logs_to_loggging_statements_level_3),
    # )
    # entity_template_generator = EntityTemplateGenerator(
    #     mapped_runtime_logs_to_loggging_statements_level_3, ""
    # )
    # (
    #     runtime_log_level_3,
    #     ground_truth_level_3,
    #     entity_log_template_level_3,
    #     generic_var_log_template_level_3,
    #     variable_entity_type_array_level_3,
    # ) = entity_template_generator.generate_ground_truth_level_3()

    # print("Still to be matched: ", +len(runtime_logs_after_level_3_mapping))
    # print(
    #     "Total number of runtime logs mapped (total no. of matches): ",
    #     +len(mapped_runtime_logs_to_loggging_statements_level_3)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_2)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_1),
    # )

    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_3.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_3,
    #     ground_truth_level_3,
    #     entity_log_template_level_3,
    #     variable_entity_type_array_level_3,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_3.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_3,
    #     ground_truth_level_3,
    #     generic_var_log_template_level_3,
    #     variable_entity_type_array_level_3,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # print("\nLEVEL 4 MAPPING...")
    # (
    #     mapped_level_4,
    #     runtime_mapped_level_4,
    # ) = api.map_runtime_logs_to_logging_statements_level_4(
    #     raw_logging_statements_level_2, runtime_logs_after_level_3_mapping
    # )
    # # zz = 0
    # # for el in mapped_level_4:
    # #     zz += 1
    # #     print(el)
    # #     if zz == 10:
    # #         break

    # runtime_logs_before_level_4_mapping = runtime_logs_after_level_3_mapping
    # print("Before level 4 mapping: ", len(runtime_logs_before_level_4_mapping))
    # runtime_logs_after_level_4_mapping = list(
    #     set(runtime_logs_before_level_4_mapping) ^ set(runtime_mapped_level_4)
    # )
    # print("After level 4 mapping: ", len(runtime_logs_after_level_4_mapping))
    # print("Number of matches found for level 4: ", len(mapped_level_4))

    # entity_template_generator = EntityTemplateGenerator(mapped_level_4, "")
    # (
    #     runtime_log_level_4,
    #     ground_truth_level_4,
    #     entity_log_template_level_4,
    #     generic_var_log_template_level_4,
    #     variable_entity_type_array_level_4,
    # ) = entity_template_generator.generate_ground_truth_level_4()

    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_4.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_4,
    #     ground_truth_level_4,
    #     entity_log_template_level_4,
    #     variable_entity_type_array_level_4,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_4.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_4,
    #     ground_truth_level_4,
    #     generic_var_log_template_level_4,
    #     variable_entity_type_array_level_4,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # print("Still to be matched: ", +len(runtime_logs_after_level_4_mapping))
    # print(
    #     "Total number of runtime logs mapped (total no. of matches): ",
    #     len(mapped_level_4)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_3)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_2)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_1),
    # )

    # print("\nLEVEL 5 MAPPING...")
    # (
    #     mapped_level_5,
    #     runtime_mapped_level_5,
    # ) = api.map_runtime_logs_to_logging_statements_level_5(
    #     raw_logging_statements_level_2, runtime_logs_after_level_4_mapping
    # )
    # # zz = 0
    # # for el in mapped_level_5:
    # #     zz += 1
    # #     print(el)
    # #     if zz == 10:
    # #         break
    # runtime_logs_before_level_5_mapping = runtime_logs_after_level_4_mapping
    # print("Before level 5 mapping: ", len(runtime_logs_before_level_5_mapping))
    # runtime_logs_after_level_5_mapping = list(
    #     set(runtime_logs_before_level_5_mapping) ^ set(runtime_mapped_level_5)
    # )
    # print("After level 5 mapping: ", len(runtime_logs_after_level_5_mapping))
    # print("Number of matches found for level 5: ", len(mapped_level_5))

    # entity_template_generator = EntityTemplateGenerator(mapped_level_5, "")
    # (
    #     runtime_log_level_5,
    #     ground_truth_level_5,
    #     entity_log_template_level_5,
    #     generic_var_log_template_level_5,
    #     variable_entity_type_array_level_5,
    # ) = entity_template_generator.generate_ground_truth_level_5()

    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_5.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_5,
    #     ground_truth_level_5,
    #     entity_log_template_level_5,
    #     variable_entity_type_array_level_5,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_5.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_5,
    #     ground_truth_level_5,
    #     generic_var_log_template_level_5,
    #     variable_entity_type_array_level_5,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # print("Still to be matched: ", +len(runtime_logs_after_level_5_mapping))
    # print(
    #     "Total number of runtime logs mapped (total no. of matches): ",
    #     len(mapped_level_5)
    #     + len(mapped_level_4)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_3)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_2)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_1),
    # )





    # print("\nLEVEL 6 MAPPING...")
    # (
    #     mapped_level_6,
    #     runtime_mapped_level_6,
    # ) = api.map_runtime_logs_to_logging_statements_level_6(
    #     raw_logging_statements_level_2, runtime_logs_after_level_5_mapping
    # )
    # # zz = 0
    # # for el in mapped_level_6:
    # #     zz += 1
    # #     print(el)
    # #     if zz == 10:
    # #         break
    # runtime_logs_before_level_6_mapping = runtime_logs_after_level_5_mapping
    # print("Before level 6 mapping: ", len(runtime_logs_before_level_6_mapping))
    # runtime_logs_after_level_6_mapping = list(
    #     set(runtime_logs_before_level_6_mapping) ^ set(runtime_mapped_level_6)
    # )
    # print("After level 6 mapping: ", len(runtime_logs_after_level_6_mapping))
    # print("Number of matches found for level 6: ", len(mapped_level_6))

    # entity_template_generator = EntityTemplateGenerator(mapped_level_6, "")
    # (
    #     runtime_log_level_6,
    #     ground_truth_level_6,
    #     entity_log_template_level_6,
    #     generic_var_log_template_level_6,
    #     variable_entity_type_array_level_6,
    # ) = entity_template_generator.generate_ground_truth_level_6()

    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_6.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_6,
    #     ground_truth_level_6,
    #     entity_log_template_level_6,
    #     variable_entity_type_array_level_6,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_6.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_6,
    #     ground_truth_level_6,
    #     generic_var_log_template_level_6,
    #     variable_entity_type_array_level_6,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # print("Still to be matched: ", +len(runtime_logs_after_level_6_mapping))
    # print(
    #     "Total number of runtime logs mapped (total no. of matches): ",
    #     len(mapped_level_6)
    #     + len(mapped_level_5)
    #     + len(mapped_level_4)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_3)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_2)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_1),
    # )



    # print("\nLEVEL 7 MAPPING...")
    # (
    #     mapped_level_7,
    #     runtime_mapped_level_7,
    # ) = api.map_runtime_logs_to_logging_statements_level_7(
    #     raw_logging_statements_level_2, runtime_logs_after_level_6_mapping
    # )
    # # print("Mapped elements level 7")
    # # zz = 0
    # # for el in mapped_level_7:
    # #     zz += 1
    # #     print(el)
    # #     if zz == 10:
    # #         break

    # runtime_logs_before_level_7_mapping = runtime_logs_after_level_6_mapping
    # print("Before level 7 mapping: ", len(runtime_logs_before_level_7_mapping))
    # runtime_logs_after_level_7_mapping = list(
    #     set(runtime_logs_before_level_7_mapping) ^ set(runtime_mapped_level_7)
    # )
    # print("After level 7 mapping: ", len(runtime_logs_after_level_7_mapping))
    # print("Number of matches found for level 7: ", len(mapped_level_7))

    # entity_template_generator = EntityTemplateGenerator(mapped_level_7, "")
    # (
    #     runtime_log_level_7,
    #     ground_truth_level_7,
    #     entity_log_template_level_7,
    #     generic_var_log_template_level_7,
    #     variable_entity_type_array_level_7,
    # ) = entity_template_generator.generate_ground_truth_level_7()

    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_7.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_7,
    #     ground_truth_level_7,
    #     entity_log_template_level_7,
    #     variable_entity_type_array_level_7,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_7.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_7,
    #     ground_truth_level_7,
    #     generic_var_log_template_level_7,
    #     variable_entity_type_array_level_7,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])




    # print("\nLEVEL 8 MAPPING...")
    # (mapped_level_8,runtime_mapped_level_8,) = api.map_runtime_logs_to_logging_statements_level_8(raw_logging_statements_level_2, runtime_logs_after_level_7_mapping)
    
    # # print("Mapped elements level 8")
    # # zz = 0
    # # for el in mapped_level_8:
    # #     zz += 1
    # #     print(el)
    # #     if zz == 10:
    # #         break

    # runtime_logs_before_level_8_mapping = runtime_logs_after_level_7_mapping
    # print("Before level 8 mapping: ", len(runtime_logs_before_level_8_mapping))
    # runtime_logs_after_level_8_mapping = list(
    #     set(runtime_logs_before_level_8_mapping) ^ set(runtime_mapped_level_8)
    # )
    # print("After level 8 mapping: ", len(runtime_logs_after_level_8_mapping))
    # print("Number of matches found for level 8: ", len(mapped_level_8))

    # entity_template_generator = EntityTemplateGenerator(mapped_level_8, "")
    # (
    #     runtime_log_level_8,
    #     ground_truth_level_8,
    #     entity_log_template_level_8,
    #     generic_var_log_template_level_8,
    #     variable_entity_type_array_level_8,
    # ) = entity_template_generator.generate_ground_truth_level_8()

    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_8.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_8,
    #     ground_truth_level_8,
    #     entity_log_template_level_8,
    #     variable_entity_type_array_level_8,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_8.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_8,
    #     ground_truth_level_8,
    #     generic_var_log_template_level_8,
    #     variable_entity_type_array_level_8,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # print("Still to be matched: ", +len(runtime_logs_after_level_8_mapping))
    # print(
    #     "Total number of runtime logs mapped (total no. of matches): ",
    #     len(mapped_level_8)
    #     + len(mapped_level_7)
    #     + len(mapped_level_6)
    #     + len(mapped_level_5)
    #     + len(mapped_level_4)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_3)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_2)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_1),
    # )


    # print("\nLEVEL 9 MAPPING...")
    # (mapped_level_9,runtime_mapped_level_9,) = api.map_runtime_logs_to_logging_statements_level_9(raw_logging_statements_level_2, runtime_logs_after_level_8_mapping)

    # runtime_logs_before_level_9_mapping = runtime_logs_after_level_8_mapping
    # print("Before level 9 mapping: ", len(runtime_logs_before_level_9_mapping))
    # runtime_logs_after_level_9_mapping = list(
    #     set(runtime_logs_before_level_9_mapping) ^ set(runtime_mapped_level_9)
    # )
    # print("After level 9 mapping: ", len(runtime_logs_after_level_9_mapping))
    # print("Number of matches found for level 9: ", len(mapped_level_9))

    # entity_template_generator = EntityTemplateGenerator(mapped_level_9, "")
    # (
    #     runtime_log_level_9,
    #     ground_truth_level_9,
    #     entity_log_template_level_9,
    #     generic_var_log_template_level_9,
    #     variable_entity_type_array_level_9,
    # ) = entity_template_generator.generate_ground_truth_level_9()

    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_9.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_9,
    #     ground_truth_level_9,
    #     entity_log_template_level_9,
    #     variable_entity_type_array_level_9,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_9.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_9,
    #     ground_truth_level_9,
    #     generic_var_log_template_level_9,
    #     variable_entity_type_array_level_9,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # print("Still to be matched: ", +len(runtime_logs_after_level_9_mapping))
    # print(
    #     "Total number of runtime logs mapped (total no. of matches): ",
    #     len(mapped_level_9)
    #     + len(mapped_level_8)
    #     + len(mapped_level_7)
    #     + len(mapped_level_6)
    #     + len(mapped_level_5)
    #     + len(mapped_level_4)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_3)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_2)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_1),
    # )


    # print("\nLEVEL 10 MAPPING...")
    # (mapped_level_10,runtime_mapped_level_10,) = api.map_runtime_logs_to_logging_statements_level_10(raw_logging_statements_level_2, runtime_logs_after_level_9_mapping)

    # runtime_logs_before_level_10_mapping = runtime_logs_after_level_9_mapping
    # print("Before level 10 mapping: ", len(runtime_logs_before_level_10_mapping))
    # runtime_logs_after_level_10_mapping = list(
    #     set(runtime_logs_before_level_10_mapping) ^ set(runtime_mapped_level_10)
    # )
    # print("After level 10 mapping: ", len(runtime_logs_after_level_10_mapping))
    # print("Number of matches found for level 10: ", len(mapped_level_10))

    # # print("Mapped elements level 10")
    # # zz = 0
    # # for el in mapped_level_10:
    # #     zz += 1
    # #     print(el)
    # #     if zz == 10:
    # #         break

    # entity_template_generator = EntityTemplateGenerator(mapped_level_10, "")
    # (
    #     runtime_log_level_10,
    #     ground_truth_level_10,
    #     entity_log_template_level_10,
    #     generic_var_log_template_level_10,
    #     variable_entity_type_array_level_10,
    # ) = entity_template_generator.generate_ground_truth_level_10()

    # spamWriter = csv.writer(
    #     open("entity_dataset/entity_dataset_hadoop_level_10.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_10,
    #     ground_truth_level_10,
    #     entity_log_template_level_10,
    #     variable_entity_type_array_level_10,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # spamWriter = csv.writer(
    #     open("generic_var_dataset/generic_var_dataset_hadoop_level_10.csv", "w")
    # )
    # for r, g, e, v in zip(
    #     runtime_log_level_10,
    #     ground_truth_level_10,
    #     generic_var_log_template_level_10,
    #     variable_entity_type_array_level_10,
    # ):
    #     spamWriter.writerow([r, g, e, v[0]])

    # print("Still to be matched: ", +len(runtime_logs_after_level_10_mapping))
    # print(
    #     "Total number of runtime logs mapped (total no. of matches): ",
    #     len(mapped_level_10)
    #     + len(mapped_level_9)
    #     + len(mapped_level_8)
    #     + len(mapped_level_7)
    #     + len(mapped_level_6)
    #     + len(mapped_level_5)
    #     + len(mapped_level_4)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_3)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_2)
    #     + len(mapped_runtime_logs_to_loggging_statements_level_1),
    # )




