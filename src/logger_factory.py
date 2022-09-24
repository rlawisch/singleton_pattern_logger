from singleton import Singleton
from logger import FileLogger, ConsoleLogger


@Singleton
class LoggerFactory:
    def get_file_logger(self, filename="log.txt") -> FileLogger:
        file_logger = FileLogger()
        file_logger.set_log_filename(filename)
        return file_logger

    def get_console_logger(self) -> ConsoleLogger:
        return ConsoleLogger()
