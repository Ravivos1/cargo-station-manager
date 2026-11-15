# Cargo Station Manager

A command-line Python app for managing the cargo of a space station. You can add, remove, and find cargo items, see station statistics, and save the station to a text file or load it back. Every action and error is written to a log file.

## Features

- **Two cargo types**
  - `CargoItem`: a regular item with an id, name, weight, and origin planet.
  - `SpecialCargo`: extends `CargoItem` with a danger level (1–5) and a requires-cooling flag.
- **Validation** of every field:
  - Name must be at least 2 characters.
  - Weight must be a positive number.
  - Danger level must be a whole number from 1 to 5.
  - Requires-cooling must be `True` or `False`.
- **Station operations:** add, remove, and find items by id. Total weight. Count of dangerous cargo (danger level 3 or higher).
- **Custom exceptions:** `CargoNotFoundError` and `DuplicateCargoError`.
- **Save and load:** the station is saved to a `.txt` file and can be rebuilt from it later. The app asks before overwriting an existing file.
- **Logging:**
  - `Cargo_Station_Actions.txt` records every action.
  - `Cargo_Station_Errors.txt` records every error, with its type and location.

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Interactive menu, the entry point of the app |
| `cargo_item.py` | `CargoItem` class with validated properties |
| `special_cargo.py` | `SpecialCargo` class, which inherits from `CargoItem` |
| `cargo_station.py` | `CargoStation` class that holds and manages the items |
| `file_helper.py` | Saves a station to a file and loads it back |
| `exception_func.py` | Custom exceptions and a helper that raises them |
| `error_action_logger.py` | Writes to the actions log and the errors log |
| `test_cargo_system.py` | Unit tests (`unittest`) |
| `test.py` | Manual test script |

## Requirements

- Python 3.10 or newer (the menu uses `match` / `case`)
- Standard library only, nothing to install

## Running

Run `main.py` from the project folder:

```bash
python main.py
```

In PyCharm, open the project folder and run `main.py`.

The log files and saved stations are created in the folder you run the app from.

## Menu

```
1 - Add a cargo (regular or special)
2 - Remove a cargo
3 - Find a specific cargo
4 - Show the total weight
5 - Show the number of dangerous cargo (danger level 3+)
6 - Save and exit
```

When the app starts, you can either create a new station or load one from a saved file.

## Running the tests

From the project folder:

```bash
python -m unittest test_cargo_system -v
```

## Save file format

```
Item number 1
item_id: 1
name: dss
weight: 43
origin_planet: Mars
Danger level: 4
Requires-cooling: True
Item number 2
item_id: 2
name: lala
weight: 50
origin_planet: Earth
```
