# IS218_Project1
# Advanced Python Calculator

## Overview
The Advanced Python Calculator is a sophisticated command-line application designed for real-time calculations, utilizing a plugin system for extended functionality. It emphasizes clean, maintainable code through the use of design patterns, comprehensive logging, and a structured architecture.

## Features
- Basic arithmetic operations: Addition, Subtraction, Multiplication, and Division.
- Plugin system for extended features, including:
  - Power calculations.
  - Factorial calculations.
  - Square root calculations.
  - Trigonometric functions: Sine, Cosine, Tangent.
- Calculation history management using Pandas.
- Comprehensive logging for detailed operations and error handling.

## Setup Instructions

### Prerequisites
- Python 3.8+
- `pip` (Python package manager)

### Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/IS218_Project1.git
    cd advanced-python-calculator
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables** (optional for dynamic logging configuration):
    - Create a `.env` file in the project root:
      ```plaintext
      LOG_LEVEL=INFO
      LOG_FILE=logging.log
      ```
    - The `LOG_LEVEL` can be set to `DEBUG`, `INFO`, `WARNING`, `ERROR`, etc.
    - The `LOG_FILE` specifies the path where logs will be saved.

### Usage
1. **Run the Calculator**:
    ```bash
    python main.py
    ```
   
2. **Command-Line Interface**:
   - Type `menu` to see the available commands.
   - Use arithmetic and plugin commands as needed.
   - Type `quit` to exit the REPL.

### Plugin Usage
1. **Load a Plugin**:
   ```plaintext
   >> load_plugin power
   Plugin 'power' loaded successfully.
## Usage Examples

```plaintext
>> add 10 5
Result: 15.0

>> subtract 20 7
Result: 13.0

>> load_plugin factorial_plugin
Plugin 'factorial_plugin' loaded successfully.

>> factorial 5
Result: 120

>> power 2 3
Result: 8.0  # 2^3

>> history
Calculation History:
operation    a   b   result
add          10  5   15.0
subtract     20  7   13.0
factorial    5   -   120
```

# Architectural Analysis

## Design Patterns Implemented
This project incorporates several design patterns to enhance code maintainability, flexibility, and scalability:

### **Facade Pattern**
- **Purpose**: Simplify the interface for complex operations involving data manipulation with Pandas.
- **Implementation**: The `PandasFacade` class hides the complexities of loading, saving, and manipulating data in CSV files. This allows the rest of the application to interact with a simple interface without needing to know the internal workings of Pandas.
- **Impact**: Enhances readability and maintainability by reducing the complexity of data operations, allowing changes to the underlying data processing without affecting other parts of the code.

### **Command Pattern**
- **Purpose**: Encapsulate requests as objects, allowing for parameterization of operations.
- **Implementation**: The `AddCommand`, `SubtractCommand`, `MultiplyCommand`, and `DivideCommand` classes implement specific arithmetic operations. These are dynamically created using a `CommandFactory` to ensure that the right command is executed based on user input.
- **Impact**: Simplifies the addition of new operations (like plugins) without modifying the core REPL logic, adhering to the **Open/Closed Principle**.

### **Factory Method Pattern**
- **Purpose**: Define an interface for creating an object but let subclasses alter the type of object that will be created.
- **Implementation**: The `CommandFactory` class handles the creation of command objects based on the command name (like `add`, `subtract`, etc.).
- **Impact**: Provides flexibility in object creation, making it easier to extend the application with new commands.

### **Strategy Pattern**
- **Purpose**: Define a family of algorithms, encapsulate each one, and make them interchangeable.
- **Implementation**: Different mathematical operations (like addition, subtraction, etc.) are encapsulated in their own classes, making them interchangeable based on user input.
- **Impact**: Provides flexibility to switch between different calculation strategies dynamically.

## Logging Strategy
The application employs a comprehensive logging system to track operations, errors, and debug information:

### **Levels of Logging**
- **DEBUG**: Captures detailed information for debugging.
- **INFO**: Records general information about user actions, like command executions.
- **WARNING**: Captures unusual situations that are not necessarily errors.
- **ERROR**: Records errors that occurred during command execution.

### **Dynamic Configuration**
The logging configuration is managed through environment variables in a `.env` file, allowing dynamic adjustments without modifying the code.

**Example configuration in `.env`:**
```plaintext
LOG_LEVEL=DEBUG
LOG_FILE=logging.log

## Testing

The application includes a comprehensive test suite using `pytest`. Each command, plugin, and edge case is tested to ensure proper functionality.

### Running Tests

1. **Install Test Dependencies**:
    ```bash
    pip install pytest pytest-cov
    ```

2. **Run the Tests**:
    ```bash
    pytest --pylint --cov
    ```
```

### Image
![cov](https://github.com/user-attachments/assets/65e15273-1916-4915-b202-4f6d10e97d44)

### Video
https://github.com/user-attachments/assets/92e57a1c-5ae3-4f74-ac6a-24309abc1ef9



