import logging
from operator import index
import yaml
import json
import os


def read_yaml(path_of_yaml: str) -> dict:
    with open(path_of_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info("yaml files: {path_of_yaml} successfully loaded")
    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok =True)
        logging.info(f"reports are saved at {dir_path}")


def save_local_df(data,data_path, index_status = False):
    data.to_csv(data_path,index = index_status)
    logging.info(f"reports are saved at {data_path}")

def save_reports(reports: dict(),report_path: str,indentation =4):
    with open (report_path ,'w') as f:
        json.dump(reports,f,indent = indentation)
    logging.info(f"reports are saved at {report_path}")