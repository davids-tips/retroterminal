# RetroTerminal

RetroTerminal is a Python library for simulating the printing like old terminals.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install RetroTerminal.

```bash
pip install RetroTerminal
```

## Usage

```python
from RetroTerminal import delay_print

# Prints text character by character
#At the default rate of .25 sec per character
delay_print('Hello World')


# Prints text character by character
#At custom rate

delay_print('Hello World', .03)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)