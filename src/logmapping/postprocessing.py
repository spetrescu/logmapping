class EntityTemplateGenerator:
    def __init__(self, mapping_runtime_logging_statments, variable_types):
        self.mapping_runtime_logging_statments = mapping_runtime_logging_statments
        self.variable_types = variable_types
    
    def generate_gdth(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[1])
            ground_truth.append(el[0])
           
            el_split = el[0].split("\"")
            if "Id" in el_split[2] or "ID" in el_split[2]:
                entity_log_template_entry = el_split[1] + "<ID>"
            else:
                entity_log_template_entry = el_split[1] + "<GENERIC_VAR>"
            
            generic_var_log_template_entry = el_split[1] + "<GENERIC_VAR>"
            entity_log_template.append(entity_log_template_entry)
            generic_var_log_template.append(generic_var_log_template_entry)
            el_split[2] = el_split[2].replace(" + ", "")
            el_split[2] = el_split[2].replace(");", "")
            variable_entity_type_array.append(el_split[2])
        
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array

    def generate_ground_truth_level_3(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array
    def generate_ground_truth_level_4(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array
    
    def generate_ground_truth_level_5(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array
    
    def generate_ground_truth_level_6(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array
    

    def generate_ground_truth_level_7(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array


    def generate_ground_truth_level_8(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array

    def generate_ground_truth_level_9(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array

    def generate_ground_truth_level_10(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        generic_var_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[0])
            ground_truth.append(el[1])
            entity_log_template.append(el[2])
            generic_var_log_template.append(el[3])
            variable_entity_type_array.append(el[4])
        return runtime_log, ground_truth, entity_log_template, generic_var_log_template, variable_entity_type_array
