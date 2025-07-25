import json
import os
import sys

sys.path.append(os.getcwd())

from fin_record.logging_info import setup_logging_config
from fin_record.utils import get_date

logger = setup_logging_config()
FILE_PATH = os.path.join("/home/xiyuanyang/Hodgepodge/Financial_record", "record.json")


def _open_file(file_path) -> list:
    try:
        logger.info(f"Attempting to open file: {file_path}")
        with open(file_path, "r") as file:
            data = json.load(file)
        logger.info(f"File opened and data loaded successfully: {file_path}")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}. Initializing empty data list.")
        return []
    except json.JSONDecodeError as e:
        logger.error(
            f"JSON decode error in file {file_path}: {e}. Initializing empty data list."
        )
        return []
    except Exception as e:
        logger.error(f"Unexpected error opening file {file_path}: {e}", exc_info=True)
        return []


def _find_date(date: str, data: list[dict]):
    for block in data:
        if block["time"] == date.strip():
            logger.info(f"Date found in records: {date}")
            return block
    logger.info(f"Date not found in records: {date}")
    return None


def record_money(date: str, money: int):
    logger.info(f"The record process begin: DATE {get_date()}")
    try:
        data = _open_file(FILE_PATH)
        block = _find_date(date, data)
        if block is not None:
            logger.info(
                f"Appending money to existing date: {date}, original record: {block['record']}, adding: {money}"
            )
            block["record"] += money
        else:
            logger.info(f"Creating new record for date: {date} with money: {money}")
            new_block = {"time": date, "record": money}
            data.append(new_block)

        data.sort(key=lambda x: x["time"])

        logger.info(f"Writing updated data to file: {FILE_PATH}")
        with open(FILE_PATH, "w") as file:
            json.dump(data, file, sort_keys=True, ensure_ascii=False, indent=4)
        logger.info(f"Data written successfully to {FILE_PATH}")
    except Exception as e:
        logger.error(f"An error occurred during record_money: {e}", exc_info=True)
    logger.info(f"The record process end: DATE {get_date()}")


if __name__ == "__main__":
    record_money("2025-07-01", 4)
