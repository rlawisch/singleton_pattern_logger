import os
import sys
import unittest
from io import StringIO

from logger_factory import LoggerFactory
from logger import LogLevel, FileLogger, ConsoleLogger


class TestLoggerFactory(unittest.TestCase):
    def test_is_singleton(self) -> None:
        first_instance = LoggerFactory()
        second_instance = LoggerFactory()
        self.assertIs(first_instance, second_instance)

    def test_get_file_logger(self) -> None:
        factory = LoggerFactory()
        logger = factory.get_file_logger()
        self.assertIsInstance(logger, FileLogger)

    def test_get_console_logger(self) -> None:
        factory = LoggerFactory()
        logger = factory.get_console_logger()
        self.assertIsInstance(logger, ConsoleLogger)


class TestFileLogger(unittest.TestCase):
    __log_filename = "log_from_testing.log"

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = FileLogger()
        cls.logger.set_log_filename(cls.__log_filename)

    def tearDown(self) -> None:
        try:
            os.remove(self.__log_filename)
        except OSError:
            pass

    def test_is_singleton(self) -> None:
        second_instance = FileLogger()
        self.assertIs(self.logger, second_instance)

    def test_log_function_level_info(self) -> None:
        self.logger.log(LogLevel.INFO, "Some information here")

        with open(self.__log_filename, "r") as logfile:
            self.assertRegex(
                logfile.readline(),
                r"\[[\d:\.\-\s]{26} - INFO\] Some information here"
            )

    def test_log_function_level_warning(self) -> None:
        self.logger.log(LogLevel.WARNING, "This is a warning")

        with open(self.__log_filename, "r") as logfile:
            self.assertRegex(
                logfile.readline(),
                r"\[[\d:\.\-\s]{26} - WARNING\] This is a warning"
            )

    def test_log_function_level_error(self) -> None:
        self.logger.log(LogLevel.ERROR, "Panic! at the logger")

        with open(self.__log_filename, "r") as logfile:
            self.assertRegex(
                logfile.readline(),
                r"\[[\d:\.\-\s]{26} - ERROR\] Panic! at the logger"
            )


class TestConsoleLogger(unittest.TestCase):
    def test_is_singleton(self) -> None:
        first_instance = ConsoleLogger()
        second_instance = ConsoleLogger()
        self.assertIs(first_instance, second_instance)

    def test_log_function_level_info(self) -> None:
        logger = ConsoleLogger()
        captured_output = StringIO()
        sys.stdout = captured_output
        logger.log(LogLevel.INFO, "Some information here")
        sys.stdout = sys.__stdout__
        self.assertRegex(
            captured_output.getvalue(),
            r"\[[\d:\.\-\s]{26} - INFO\] Some information here"
        )

    def test_log_function_level_warning(self) -> None:
        logger = ConsoleLogger()
        captured_output = StringIO()
        sys.stdout = captured_output
        logger.log(LogLevel.WARNING, "This is a warning")
        sys.stdout = sys.__stdout__
        self.assertRegex(
            captured_output.getvalue(),
            r"\[[\d:\.\-\s]{26} - WARNING\] This is a warning"
        )

    def test_log_function_level_erroe(self) -> None:
        logger = ConsoleLogger()
        captured_output = StringIO()
        sys.stdout = captured_output
        logger.log(LogLevel.ERROR, "Panic! at the logger")
        sys.stdout = sys.__stdout__
        self.assertRegex(
            captured_output.getvalue(),
            r"\[[\d:\.\-\s]{26} - ERROR\] Panic! at the logger"
        )


if __name__ == '__main__':
    unittest.main()
