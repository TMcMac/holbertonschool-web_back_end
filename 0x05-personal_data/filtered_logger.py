#!/usr/bin/env python3
"""
    Write a function called filter_datum that
    returns the log message obfuscated:

    Arguments:
    * fields: a list of strings representing all fields
    to obfuscate
    * redaction: a string representing by what the field
    will be obfuscated
    * message: a string representing the log line
    * separator: a string representing by which character is
    separating all fields in the log line (message)

    The function should use a regex to replace occurrences of
    certain field values.
    filter_datum should be less than 5 lines long and use re.sub
    to perform the substitution with a single regex.
"""
import re
import logging
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        method to filter values in incoming log records using filter_datum.
        Values for fields in fields should be filtered.
        """
        return filter_datum(
            self.fields, self.REDACTION, super().format(record),
            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Implement a get_logger function that takes no arguments
    and returns a logging.Logger object.

    The logger should be named "user_data" and only log up to
    logging.INFO level. It should not propagate messages to other loggers.
    It should have a StreamHandler with RedactingFormatter as formatter.

    Create a tuple PII_FIELDS constant at the root of the module containing the
    fields from user_data.csv that are considered PII. PII_FIELDS can contain
    only 5 fields - choose the right list of fields that can are considered as
    “important” PIIs or information that you must hide in your logs. Use it to
    parameterize the formatter.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    # Create console handler (ch) set level info
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # streamhandler with redacting formatter
    ch.setFormatter(RedactingFormatter)
    # add handler to logger
    logger.addHandler(ch)

    return logger


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Takes in a message and obsficates indicated fields"""
    for field in fields:
        message = re.sub(field + '=' + '.+?' + separator,
                         field + '=' + redaction + separator,
                         message)
    return message
