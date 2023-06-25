## Project Title

### Fake data generator using python

## Project Description

This repository contains the source code for a Python console app, using the Faker library to generate an arbitrary length of columnar data. This generator creates a CSV file.

## Assumptions

I assume you are developing this project on a Microsoft Windows PC. A built-in Windows tool like notepad.exe is used in this project to create and edit files. If you are developing on Linux, you can use vim.

```
notepad .gitignore
```

On Linux:

```
vim .gitignore
```


You can also use a modern code editor like VSCode to follow along.


## How to Use the Project

You can clone this project.

```
 git clone https://github.com/dareljohnson/fake-data-generator-app.git
```


## Project Requirements

Requirements:

- Python 3.10.0
- Faker==18.11.1

# How to install python packages

Create a custom python environment for your project:

```
conda create --name faker python=3.10
```

If you are using the PowerShell command line interface, you may need to initialize a shell for the conda environment.

To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - cmd.exe
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell
  
  
I'm going to use cmd.exe:

```
conda init cmd.exe
```

Activate the environment:

```
conda activate faker
```

# Clone the repo

Clone repo to current directory

```
git clone https://github.com/dareljohnson/fake-data-generator-app.git .
```

## Install the packages

```
pip install -r requirements.txt
```

## How to Run the Project

Run the local application:

```
python main.py filename # You don't need to add a file extension
```


## How to Build the Project for production

N/A

## Include Credits

TBA

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

