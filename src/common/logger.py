import logging
import time
import os

class Logger(object):
    """
    set logger format
    """

    def __init__(self, name, level) -> None:
        self.logger = logging.getLogger(f"{name}")
        self._setup_logger(level)

    # def get_logger(self, level):
    #     self._setup_logger(level)
    #     return self.logger

    def _setup_logger(self,level):
        if self.logger.handlers:
            return
        
        self.logger.setLevel(level)
        self.logger.propagate = False

        fmtfmt = "%(asctime)s %(pathname)s %(lineno)d [%(levelname)s]: %(message)s" 
        datefmt="%Y/%m/%d %H:%M:%S"
        formatter = logging.Formatter(fmt=fmtfmt, datefmt=datefmt)
        
        # console handler
        shell_header = logging.StreamHandler()
        shell_header.setFormatter(formatter)
        shell_header.setLevel(level)
        self.logger.addHandler(shell_header)

        # ensure log directory exists
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        log_dir = os.path.join(project_root, "log")
        os.makedirs(log_dir, exist_ok=True)

        # file handler (daily file)
        filename = os.path.join(log_dir, "{}.log".format(time.strftime("%Y%m%d", time.localtime())))
        file_header = logging.FileHandler(filename=filename, encoding="utf8")
        file_header.setFormatter(formatter)
        file_header.setLevel(level)
        self.logger.addHandler(file_header)