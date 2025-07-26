import argparse
import sys
import os
sys.path.append(os.getcwd())

from fin_record.utils import get_date
from fin_record.logging_info import setup_logging_config
from fin_record.record import record_money


def get_argparse():
    parser = argparse.ArgumentParser(description="parser for financial recording")
    parser.add_argument("number", type=int, default=0, help="Receive an integer.")
    parser.add_argument(
        "--date", type=str, default=get_date(), help="The date to be counted."
    )

    args = parser.parse_args()
    return args.number, args.date


def main():
    logger = setup_logging_config()
    logger.info("Script started.")
    try:
        number, date = get_argparse()
        logger.info(f"Parsed arguments: number={number}, date={date}")
        record_money(date, number)
        logger.info("Record money process completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred in main: {e}", exc_info=True)
    finally:
        logger.info("Script ended.")


if __name__ == "__main__":
    main()
