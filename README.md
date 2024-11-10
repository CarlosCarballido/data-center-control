# Project Name

## Description

This project is a rule-based data center control system built using Python and CLIPS. It uses a combination of Python scripts and CLIPS files to manage events, define rules, and execute a control mechanism. The project integrates the CLIPS expert system environment to manage facts and rules, creating a powerful tool for automating decision-making processes.

## Features

- **Rule-based Control**: Uses CLIPS to define and manage rules for controlling various components of a data center, such as sensors and actuators.
- **Python Integration**: Python scripts interact with the CLIPS environment, loading facts and rules and executing them.
- **Testing**: Unit tests provided using `pytest` to verify the correct functioning of rules execution and system behavior.

## Structure

The project contains the following key components:

- **Python Scripts**:
  - `main.py`: The main execution script for integrating CLIPS and running the data center control logic.
  - `zona.py`: Handles data related to different zones within the data center.
  - `events.py`: Manages events that occur in the system and loads them into the CLIPS environment.
  - `test_0.py`: Contains unit tests to verify the behavior of the rule execution.

- **Compiled Python Files** (`.pyc` files):
  - Precompiled versions of `main.py` and `events.py` for optimization.

- **CLIPS Files**:
  - `hechos_iniciales.clp`: Defines the initial facts for the rule engine.
  - `control_reglas.clp`: Contains the rules for controlling the data center.

## Prerequisites

- **Python 3.12**
- **CLIPS**
- **Pytest**

Make sure to install all necessary dependencies before running the project. The Python CLIPS library is used for integration between Python and CLIPS.

## Setup and Installation

1. Clone the repository.
2. Install the required Python dependencies using pip:

   ```sh
   pip install -r requirements.txt
   ```

3. Make sure CLIPS is installed and accessible from your environment.

## Running the Project

1. Load the initial facts and control rules:

   ```sh
   python main.py
   ```

2. To test the rule execution, run the tests using pytest:

   ```sh
   pytest test_0.py
   ```

## Testing

The project uses `pytest` for unit testing. The test file (`test_0.py`) is designed to load facts and rules, execute the rule engine, and validate the results. Modify the assertions based on the expected behavior for your specific rules.

## Contribution

Contributions are welcome! Please create a pull request or open an issue if you have suggestions for improvements.

## License

This project is licensed under the MIT License.
