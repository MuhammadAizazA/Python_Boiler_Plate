# Project-Name

This repository contains the source code for (Project-Name). To get started, follow the instructions below:

## Installation

* Clone the repository to your local machine:

  ```
  git clone https://github.com/MuhammadAizazA/Python_Boiler_Plate.git
  ```
* Navigate to the project directory:

  ```
  cd Python_Boiler_Plate
  ```
* Open a terminal in the project directory.
* Install dependencies and set up the virtual environment by running the following command:

  ```
  python . or py .
  ```

## Usage

Now that the dependencies are installed and the virtual environment is set up, you can run the code from the `src` directory. To do this, execute the following command:

```
python src/example_module.py
```

## Logging

Logging is a crucial aspect of any application to capture and track information about its runtime behavior. This project utilizes the Python logging module to configure and manage logging settings. The logging configuration is designed to be flexible, allowing developers to customize it based on their requirements.

### Setup

To set up logging in your Python script or application, you can use the provided setup_logging function. This function configures the logging system based on a YAML file containing logging settings. If the file is not found, it defaults to a basic configuration with the specified default logging level.

```
import logging
from your_module import setup_logging, test_logging_working

# Set up logging with default configuration
setup_logging()

# Example of logging in your script or application
test_logging_working()
# or
logging.debug("Testing logging")
```

#### Custom Configuration File

You can specify a custom configuration file by setting the 'LOG_CFG' environment variable:

`export LOG_CFG=/path/to/your/custom/logging_config.yaml `

### Logging Levels

The logging levels used in this project are:

* **DEBUG**: Detailed information, typically of interest only when diagnosing problems.
* **INFO**: Confirmation that things are working as expected.
* **ERROR**: Indicates a more serious problem or error in the application.
* **WARNING**: Indicates a warning that might need attention.
* **CRITICAL**: A very serious error that may prevent the program from continuing.

### Handlers

This project includes several logging handlers, including:



* **Console Handler**: Outputs log messages to the console.
* **File Handler**: Writes log messages to a file.
* **Email Handler**: Sends log messages via email for critical errors.

To configure additional handlers or customize existing ones, you can modify the logging configuration file (logs/logging.yaml by default).

### Customization

Feel free to customize the logging configuration based on your project's needs. Update the logging levels, handlers, and formatters to suit your application's requirements.
