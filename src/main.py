from logger_factory import LoggerFactory
from logger import LogLevel


if __name__ == '__main__':
    print("Creating logger factory...")
    logger_factory = LoggerFactory()
    print(f"Created logger factory with ID {id(logger_factory)}")
    print("Creating a second instance of the logger factory")
    logger_factory_2 = LoggerFactory()
    print(f"Created second logger factory with ID {id(logger_factory_2)}")
    if id(logger_factory) == id(logger_factory_2):
        print("IDs match, meaning they are from the same instance (Singleton)")

    print("\nFrom logger factory, getting a ConsoleLogger instance")
    console_logger = logger_factory.get_console_logger()
    print(f"Created console logger with ID {id(console_logger)}")
    print("Creating a second instance of the console logger")
    console_logger_2 = logger_factory.get_console_logger()
    print(f"Created second console logger with ID {id(console_logger_2)}")
    if id(console_logger) == id(console_logger_2):
        print("IDs match, meaning they are from the same instance (Singleton)")

    print("\nLogging 3 messages with ConsoleLogger, one with each level")
    console_logger.log(LogLevel.INFO, "First, an info")
    console_logger.log(LogLevel.WARNING, "Then, a warning")
    console_logger.log(LogLevel.ERROR, "At last, an error")
    print("3 messages were logged in the console")

    print("\nFrom logger factory, getting a FileLogger instance")
    file_logger = logger_factory.get_file_logger()
    print(f"Created file logger with ID {id(file_logger)}")
    print("Creating a second instance of the file logger")
    file_logger_2 = logger_factory.get_file_logger()
    print(f"Created second file logger with ID {id(file_logger_2)}")
    if id(file_logger) == id(file_logger_2):
        print("IDs match, meaning they are from the same instance (Singleton)")

    print("\nLogging 3 messages with FileLogger, one with each level")
    file_logger.log(LogLevel.INFO, "First, an info")
    file_logger.log(LogLevel.WARNING, "Then, a warning")
    file_logger.log(LogLevel.ERROR, "At last, an error")
    print("3 messages were logged in 'log.txt'")
