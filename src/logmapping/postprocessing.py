class EntityTemplateGenerator:
    def __init__(self, mapping_runtime_logging_statments, variable_types):
        self.mapping_runtime_logging_statments = mapping_runtime_logging_statments
        self.variable_types = variable_types
    
    def generate_gdth(self):
        runtime_log = []
        ground_truth = []
        entity_log_template = []
        variable_entity_type_array = []
        for el in self.mapping_runtime_logging_statments:
            runtime_log.append(el[1])
            ground_truth.append(el[0])
           
            el_split = el[0].split("\"")
            entity_log_template_entry = el_split[1] + "<GENERIC_VAR>"
            entity_log_template.append(entity_log_template_entry)

            if "+" in el_split[2]:
                el_split[2] = el_split[2].replace("+", "")
                if ";)" in el_split[2]:
                    el_split[2] = el_split[2].replace("+", "")
                el_split[2] = el_split[2].rstrip()
                el_split[2] = el_split[2].lstrip()

            variable_entity_type_array.append(el_split[2])
            
            # if "id" in el[0].split("\"")[2].lower():
            #     el_split = el[0].split("\"")
            #     ground_truth = el_split[1] + "<ID>"
            #     entry_entity_dataset.append()
        
        return runtime_log, ground_truth, entity_log_template, variable_entity_type_array

                
