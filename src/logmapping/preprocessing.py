# transform a directory  that contains runtime logs in all of its files into a list of runtime logs
# runtime logs relative path src/runtime_logs/Hadoop
import os
from glob import glob
from logmapping.utils import RUNTIME_LOG_FILE_EXTENSION

class PreprocessRuntimeLogs:
    def __init__(self, runtime_logs_dir_path):
        self.runtime_logs_dir_path = runtime_logs_dir_path
        
        self.runtime_logs_files_list = None
        self.runtime_logs_in_dir = None
        self.pre_processed_runtime_logs_in_dir = None
        self.pre_processed_runtime_logs_in_dir_no_meta = None

    def list_files_in_dir(self):
        print(f"Looking for files with the '{RUNTIME_LOG_FILE_EXTENSION}' extension...")
        list_of_all_runtime_log_files_in_dir= []
        for x in os.walk(self.runtime_logs_dir_path):
            for y in glob(os.path.join(x[0], RUNTIME_LOG_FILE_EXTENSION)):
                list_of_all_runtime_log_files_in_dir.append(y)
        print(f"Found {len(list_of_all_runtime_log_files_in_dir)} runtime log files in {self.runtime_logs_dir_path}\n")
        self.runtime_logs_files_list = list_of_all_runtime_log_files_in_dir
        return self.runtime_logs_files_list

    def generate_list_of_runtime_logs_in_file(self, file_path):
        #print("Reading file: ", file_path)
        with open(file_path) as f:
            lines = f.readlines()
        return lines

    def _preprocess_runtime_log(self, runtime_log):
        runtime_log = runtime_log.rstrip()
        return runtime_log

    def generate_list_of_runtime_logs_in_dir(self):
        list_of_all_runtime_logs = []
        for file in self.runtime_logs_files_list:
            runtime_logs_in_file = self.generate_list_of_runtime_logs_in_file(file)
            for runtime_log in runtime_logs_in_file:
                list_of_all_runtime_logs.append(runtime_log)
        self.runtime_logs_in_dir = list_of_all_runtime_logs

        return self.runtime_logs_in_dir
    
    def preprocess_runtime_logs(self):
        list_of_pre_processed_runtime_logs = []
        for runtime_log in self.runtime_logs_in_dir:
            if runtime_log.startswith("2015"): # for Hadoop
                runtime_log = self._preprocess_runtime_log(runtime_log)
                list_of_pre_processed_runtime_logs.append(runtime_log)
                #
        self.pre_processed_runtime_logs_in_dir = list_of_pre_processed_runtime_logs
        return list_of_pre_processed_runtime_logs

    def preprocess_runtime_logs_dedupicate(self):
        self.pre_processed_runtime_logs_in_dir = list(set(self.pre_processed_runtime_logs_in_dir))
        return self.pre_processed_runtime_logs_in_dir

    def remove_meta_information_hadoop(self):
        runtime_logs_without_meta_information = []
        for log_with_meta_information in self.pre_processed_runtime_logs_in_dir:
            log_no_meta_information_split = log_with_meta_information.split("]")
            log_no_meta_information = ']'.join(log_no_meta_information_split[1:])
            log_no_meta_information_split = log_no_meta_information.split(":")
            log_no_meta_information = ':'.join(log_no_meta_information_split[1:])
            log_no_meta_information = log_no_meta_information.lstrip()
            runtime_logs_without_meta_information.append(log_no_meta_information)
        self.pre_processed_runtime_logs_in_dir_no_meta = runtime_logs_without_meta_information
        return runtime_logs_without_meta_information

            
