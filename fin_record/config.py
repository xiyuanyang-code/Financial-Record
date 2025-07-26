import importlib.resources
import yaml

with importlib.resources.files("fin_record").joinpath("config.yaml").open("r") as f:
    config = yaml.safe_load(f)