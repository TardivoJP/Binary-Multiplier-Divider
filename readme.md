# Binary Multiplication and Division Simulator
## _A simple educational tool for visualizing unsigned binary operations_

![Binary knowledge](https://i.imgur.com/w0eNx7W.jpg)

This desktop application allows the user to perform the basic multiplication and division operations with numbers they desire and actually see how the underlying process works with raw binary numbers, how they're stored in registers and shifted around to get accurate results in a reasonably efficient fashion computability wise. Users will be able to see a step by step of each process, such that they're able to acquire a better understanding about these fundamental building blocks of almost any processor.

For the purpuses of the educational simulation, we'll establish a limit of numbers represented only up to 15 bits, so inputs equal to and larger than 32767 won't be accepted. Inputs should also be equal to or larger than 0. Finally inputs should be integer numbers.

The application features the operations of multiplication and division:

_Welcome screen_

![Application welcome screen](https://i.imgur.com/TJV3IpM.png)

_Multiplication screen_

![Application multiplication input screen](https://i.imgur.com/nF46LLs.png)

_Division screen_

![Application division input screen](https://i.imgur.com/P2bKKaJ.png)

After inputting either the multiplicand and multiplier or the divisor and dividend, the application will then generate the step by step process for how the operation was performed:

_Multiplication example_

![Application multiplication log example](https://i.imgur.com/Jvf7L1E.png)

_Division example_

![Application division log example](https://i.imgur.com/daAM6rO.png)

Don't forget you can't divide by zero!

![Application divide by zero error screen](https://i.imgur.com/RQoAJQO.png)


## Usage

- Run the application and choose the desired operation in the welcome screen

**Multiplication**
  * Insert the multiplicand and multiplier in their respective input boxes.
      * Numbers must be larger or equal to 0.
      * Numbers can't be larger or equal to 32767.
      * Numbers must be integer values.
  * Click the "multiply" button above.
  * Enjoy the results!

**Division**
  * Insert the divisor and dividend in their respective input boxes.
      * Numbers must be larger or equal to 0.
      * Numbers can't be larger or equal to 32767.
      * Numbers must be integer values.
      * Divisor can't be zero!
  * Click the "divide" button above.
  * Enjoy the results!

**Miscellaneous**
  * The back button in either screen will return to the welcome screen.
  * The reset button in either screen will return that screen to its initial state.


## Packages used

This educational application was only made possible because of these amazing packages.

| Package | Link |
| ------ | ------ |
| PyQt6 | https://pypi.org/project/PyQt6/ |
| PyInstaller | https://pypi.org/project/pyinstaller/ |

## Building the application

If you want to build the application yourself from the source code:

**Windows**
1. Download Python from https://www.python.org/downloads/ and install it
2. Open a terminal and run this command to install the dependencies:
```sh
pip install PyQt6 PyInstaller
```
3. Navigate to the source code's directory and run this command to build the application:
```sh
pyInstaller main_window.py --onefile --noconsole --icon=logo.ico --add-data "resources;resources"
```
4. Run the newly created .exe in the "dist" folder

**Linux**
1. Download and install Python using the package manager from your distro:
* Ubuntu/Debian
```sh
sudo apt install python3
```
* Fedora
```sh
sudo dnf install python3
```
* CentOS/RHEL
```sh
sudo yum install centos-release-scl
sudo yum install rh-python36
scl enable rh-python36 bash
```
* Arch
```sh
sudo pacman -S python
```
2. Download and install the Package Installer for Python (pip):
```sh
python3 get-pip.py
```
3. Download and install the dependencies:
```sh
sudo pip3 install pyinstaller pyqt6
```
4. Navigate to the source code's directory and run this command to build the application:
```sh
python3 -m PyInstaller main_window.py --onefile --noconsole --icon=logo.ico --add-data "resources:resources"
```
5. Navigate to the newly created "dist" folder
6. Run this command on the main_window binary file to grant it permission to execute
```sh
chmod +x main_window
```
7. Run the application with this command:
```sh
./main_window
```

## Compatibility

This application currently runs on Windows 10 and Linux. I am looking into the possibility of adding a macOS release but I won't make any promises.

## Future development

This application does have a few possibilities for additional features which may include:

- Dynamic bit size allocation depending on inputs
- Signed variation of the operations
- Floating point variation of the operations
- Support for negative values
- More operations which use the basic ones as their core such as powers, roots, etc...