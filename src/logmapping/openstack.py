import os
from glob import glob
from logmapping.utils import OPENSTACK_MAPPING_LEVELS, OPENSTACK_MAPPING_TEMPLATE_GENERIC_VAR, OPENSTACK_MAPPING_TEMPLATE_ENTITY, OPENSTACK_MAPPING_TEMPLATE_UNDERLYING_STATEMENT, OPENSTACK_VARIBLE_TUPLES
import csv

class LogMapperOpenStack:
    def __init__(self, runtime_logs_path):
        self.runtime_logs_path = runtime_logs_path
        self.runtime_logs = None
        self.runtime_logs_no_meta = None

        self.mapped_runtime_logs_to_loggging_statements = None
        self.runtime_logs_mapped = None
    
    def get_runtime_logs(self):
        with open(self.runtime_logs_path) as f:
            lines = f.readlines()
        self.runtime_logs = lines
        return self.runtime_logs

    def remove_meta_information(self):
        runtime_logs_no_meta = []
        for runtime_log in self.runtime_logs:
            if "]" in runtime_log:
                runtime_log = "- - -]".join(runtime_log.split("- - -]")[1:]).lstrip().rstrip()
                runtime_logs_no_meta.append(runtime_log)
        self.runtime_logs_no_meta = runtime_logs_no_meta
        return runtime_logs_no_meta

    def log_mapping_openstack(self, level):
        mapped_runtime_logs_to_loggging_statements = []
        runtime_logs_mapped = []

        matches_runtime = []
        matches_logging_statements = []

        for el in self.runtime_logs_no_meta:
            match = True
            for constant_part in OPENSTACK_MAPPING_LEVELS[f"LEVEL_{level}"]:
                if constant_part in el:
                    continue
                else:
                    match = False
            if match == True:
                matches_runtime.append(el)
                runtime_logs_mapped.append(el)

        gdth_simple = OPENSTACK_MAPPING_TEMPLATE_GENERIC_VAR[f"LEVEL_{level}"]
        gdth_rich = OPENSTACK_MAPPING_TEMPLATE_ENTITY[f"LEVEL_{level}"]

        underlying_logging_statement = OPENSTACK_MAPPING_TEMPLATE_UNDERLYING_STATEMENT[f"LEVEL_{level}"]

        for runtime_log in matches_runtime:
            mapped_runtime_logs_to_loggging_statements.append([runtime_log, underlying_logging_statement, gdth_rich, gdth_simple, OPENSTACK_VARIBLE_TUPLES[f"LEVEL_{level}"]])
        
        self.mapped_runtime_logs_to_loggging_statements = mapped_runtime_logs_to_loggging_statements
        self.runtime_logs_mapped = runtime_logs_mapped

        return mapped_runtime_logs_to_loggging_statements, runtime_logs_mapped

    def generate_ground_truth(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapped_runtime_logs_to_loggging_statements:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array

    def write_mapping_to_file(self, level, type):
        runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array = self.generate_ground_truth()
        if type == "entity":
            templates = entity_log_template
        else:
            templates = generic_var_log_template

        spamWriter = csv.writer(
            open(f"{type}_dataset/{type}_dataset_openstack_level_{level}.csv", "w")
        )
        for r, g, e, v in zip(
            runtime_log,
            ground_truth,
            templates,
            variable_entity_type_array,
        ):
            spamWriter.writerow([r, g, e, v[0]])

    def remove_mapped_logs(self, mapped_logs):
        print(len(self.runtime_logs_no_meta))
        print(len(set(self.runtime_logs_no_meta)))
        self.runtime_logs_no_meta = list(set(self.runtime_logs_no_meta) ^ set(mapped_logs))
        print(len(self.runtime_logs_no_meta))

    def extra_split_in_level(self, rule):
        mapped_split = []
        for r, g, e, s, v in self.mapped_runtime_logs_to_loggging_statements:
              mapped_split.append([rule.join(r.split(rule)[1:]).lstrip(), g, e, s, v])
        self.mapped_runtime_logs_to_loggging_statements = mapped_split