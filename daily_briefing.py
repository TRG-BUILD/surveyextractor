import logging
import argparse
from easemail import logger
import json
import os
from teams_logger import TeamsHandler


def read_job_config(filename: str) -> dict:
    """
    Converts JSON config to dictionary. Secure info like email sender and
    pass are obtained from environmental variables EMAIL_USER and EMAIL_PASS
    """
    cfg = {
        "webhook_url": ""
    }

    with open(filename, "r") as fin:
        cfg.update(json.load(fin))
    return cfg


#logging.basicConfig(handlers=[th])
def main(cfg : dict):
    survey_db_url = cfg["survey_db_url"]
    log_name = cfg["log_name"]
    log_folder = cfg["log_dir"]

    jlogger = logger.Logger(log_name, log_folder)
    th = TeamsHandler(url=cfg["webhook_url"], level=logging.INFO)

    jlogger.logger.addHandler(th)
    jlogger.logger.error("hej med dig\t jidosf")

    #jlogger.log_email_pass("frøst", 2)


if __name__ == "__main__":
    ag = argparse.ArgumentParser("How many have completed")
    ag.add_argument("-c", "--config", default='../easemailing/jobcfg.json', type=str, help="configuration file")
    args = ag.parse_args()
    cfg = read_job_config(args.config)

    main(cfg)