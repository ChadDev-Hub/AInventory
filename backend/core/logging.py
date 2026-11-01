import logging
import sys
from pathlib import Path


class Logger:
    def __init__(self):
        """
        #### Appication Logger

        Logs information about the application instance and routes

        Parameters
        ----------
        None

        Returns
        -------
        None

        Methods
        -------
        - loginfo(message)
        - logerror(message)
        - logdebug(message)
        - logwarning(message)
        """
        self.logger = logging.getLogger(__name__)

    def setuplogging():
        print(Path(__file__).parent.parent)
        LOG_DIR = Path(__file__).parent.parent / "logs"
        LOG_DIR.mkdir(exist_ok=True)
        LOG_FILE = LOG_DIR / "ainventory.log"
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
                logging.FileHandler(LOG_FILE, encoding="utf-8"),
                logging.StreamHandler(sys.stdout)
            ],
        )

    def loginfo(self, message):
        """
        Logs Informations

        Args:
            message (str|any): _description_
        """
        self.logger.info(message)

    def logerror(self, message):
        """
        Logs Error

        Args:
            message (_type_): _description_
        """

        self.logger.error(message)

    def logdebug(self, message):
        """
                Logs Debug

                Args:
                    message (_type_): _description_
        """
        self.logger.debug(message)

    def logwarning(self, message):
        """
                Logs Warning

                Args:
                    message (_type_): _description_
        """
        self.logger.warning(message)
