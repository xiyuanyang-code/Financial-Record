import argparse
import sys
import os
import json
sys.path.append(os.getcwd())

from fin_record.utils import get_date
from fin_record.logging_info import setup_logging_config
from fin_record.record import record_money, show_json


def get_argparse():
    parser = argparse.ArgumentParser(description="parser for financial recording")
    parser.add_argument("--number", type=int, default=0, help="Receive an integer.")
    parser.add_argument(
        "--date", type=str, default=get_date(), help="The date to be counted."
    )
    parser.add_argument(
        "--command", type=str, default=None, help="Additional Commands, including ls."
    )

    args = parser.parse_args()
    return args.number, args.date, args.command


def main():
    logger = setup_logging_config()
    logger.info("Script started.")
    try:
        number, date, command = get_argparse()
        if command is not None:
            command = str(command).strip().lower()
        match command:
            case "ls":
                print(show_json())
            case None:
                logger.info(f"Parsed arguments: number={number}, date={date}")
                record_money(date, number)
                logger.info("Record money process completed successfully.")
            case _:
                logger.warning("Invalid command")
    except Exception as e:
        logger.error(f"An error occurred in main: {e}", exc_info=True)
    finally:
        logger.info("Script ended.")


if __name__ == "__main__":
    main()
