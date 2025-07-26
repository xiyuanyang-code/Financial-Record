import yaml
import os

if __name__ == "__main__":
    log_path = os.path.join(os.getcwd(), "log/financial.log")
    record_path = os.path.join(os.getcwd(), "record.json")
    log_dir = os.path.join(os.getcwd(), "log")
    print("Log path: ", log_path)
    print("Record path: ", record_path)
    print("log dir: ", log_dir)

    # write into yaml file
    config_data = {
        "log_file_path": log_path,
        "log_dir_home": log_dir,
        "record_path": record_path,
    }

    # Write to YAML file
    with open("./fin_record/config.yaml", "w") as yaml_file:
        yaml.dump(config_data, yaml_file, default_flow_style=False)

    print("Configuration written to config.yaml")
