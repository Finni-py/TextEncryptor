import logging
from colorama import init, Fore, Style

init(autoreset=True)

class ColorFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        msg = super().format(record)
        if record.levelno >= logging.ERROR:
            return Fore.RED + msg + Style.RESET_ALL
        elif record.levelno == logging.INFO:
            return Fore.GREEN + msg + Style.RESET_ALL
        elif record.levelno == logging.DEBUG:
            return Fore.CYAN + msg + Style.RESET_ALL
        return msg

logger = logging.getLogger('textencryptor')
logger.setLevel(logging.DEBUG)  # Можно поменять на INFO для менее подробных логов

formatter = ColorFormatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)