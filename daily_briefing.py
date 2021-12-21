import logging
import argparse
from easemail import logger
import json
from teams_logger import TeamsHandler
from typing import Dict
from sqlalchemy import create_engine

def read_job_config(filename: str) -> dict:
    """
    Converts JSON config to dictionary. Secure info like email sender and
    pass are obtained from environmental variables EMAIL_USER and EMAIL_PASS
    """
    cfg = {
    }

    with open(filename, "r") as fin:
        cfg.update(json.load(fin))
    return cfg

def db_query(db_url : str)->Dict:
    engine = create_engine(db_url)
    with engine.connect() as conn:
        result = conn.execute('SELECT * FROM answer_stats')
        out = []
        out.append('<table>')
        for idx, row in enumerate(result):
            row = dict(row)
            out.append('<tr>')
            if idx == 0:
                out.append('<tr>')
                for value in row.keys():
                    out.append(f'<td>{value}</td>')
                else:
                    out.append('</tr>')

            for key, value in row.items():
                value = value if value is not None else ""
                out.append(f'<td>{value}</td>')
            else:
                out.append('</tr>')
        else:
            out.append('</table>')
        return out

def main(cfg : dict):
    survey_db_url = cfg["survey_db_url"]
    log_name = cfg["log_name"]
    log_folder = cfg["log_dir"]

    out = db_query(cfg['survey_db_url'])

    jlogger = logger.Logger(log_name, log_folder)
    th = TeamsHandler(url=cfg["teams_webhook"], level=logging.INFO)

    jlogger.logger.addHandler(th)
    jlogger.logger.info("\n".join(out))



if __name__ == "__main__":
    ag = argparse.ArgumentParser("How many have completed")
    ag.add_argument("-c", "--config", type=str, help="configuration file")
    args = ag.parse_args()
    cfg = read_job_config(args.config)

    main(cfg)
