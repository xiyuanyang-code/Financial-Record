# Financial Record

A simple command-line interface (CLI) tool for quickly recording your financial transactions.

## Installation

To install the `fin-record` tool, navigate to your project's root directory (where `pyproject.toml` is located) and run the following command:

```bash
# clone the repo
git clone https://github.com/xiyuanyang-code/Financial-Record.git
cd Financial-Record

# run construct.py for loading config and fixing log_dir
python construct.py

# install several modules via pip
pip install .
```

Or you can simply run `bash run.sh` for simplicity.

> [!WARNING]
> Remember to run construct.py before install the package!

This will install the tool and make the `fin_record` command available in your terminal.


## Usage

Record a transaction by providing the amount. The current date will be used automatically.

```bash
fin_record amount
```

- record an expense of 1000: `fin_record 1000`

- record an expense of 1000 for specific date: `fin_record 1000 --date 2025-09-20`


## Todo List

- Optimize the construction for json file and logging files.

- Finish analysis module.

## Demo

```json
[
    {
        "record": 1,
        "time": "2025-07-23"
    },
    {
        "record": -960000,
        "time": "2025-07-26"
    }
]
```