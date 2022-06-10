from easemail import logger
from teams_logger import TeamsHandler,Office365CardFormatter
from decouple import config, Csv


def main():
    log_name = "nice.log"
    log_folder = "./"
    jlogger = logger.Logger(log_name, log_folder)

    th = TeamsHandler(url=config('teams_webhook', cast=str), level=logger.logging.INFO)
    #cf = Office365CardFormatter(facts=[])
    #th.setFormatter(cf)
    jlogger.logger.addHandler(th)
    jlogger.logger.info("he\njdsfjfdsf<br />sadsdd")

if __name__ == "__main__":

    #main()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        f"%(asctime)s{self.delimiter}%(levelname)s{self.delimiter}%(message)s",
        "%Y-%m-%d %H:%M:%S")

    file_handler = logging.FileHandler("./tester.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
