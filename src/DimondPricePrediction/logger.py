import logging
import os
from datetime import datetime


LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs")

os.makedirs(log_path, exist_ok=True) #If folder does not exist it will create a new one else it will ignore

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelno)s - %(message)s"
)


if __name__ == '__main__':
    logging.info("Here again i am testing")