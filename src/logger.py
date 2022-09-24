from datetime import datetime
from enum import Enum
from abc import ABCMeta, abstractmethod

from singleton import Singleton


class LogLevel(Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3


class Logger(metaclass=ABCMeta):
    @abstractmethod
    def log(self, level: LogLevel, message: str):
        pass


@Singleton
class FileLogger(Logger):
    def set_log_filename(self, filename) -> None:
        self.__logfile = filename

    def log(self, level: LogLevel, message: str):
        with open(self.__logfile, "a") as logfile:
            now = datetime.now()
            logfile.write(f"[{now} - {level.name}] {message}\n")


@Singleton
class ConsoleLogger(Logger):
    def log(self, level: LogLevel, message: str):
        now = datetime.now()
        print(f"[{now} - {level.name}] {message}\n")
