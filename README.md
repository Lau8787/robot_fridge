# robot_fridge

## Install

- Install dependencies:

      sudo apt-get install -y python3-pip
      sudo apt-get install -y python3-venv
      sudo apt-get install -y i2c-tools

- Activate the virtual env:

      source ./venv

- Install python packages:

      pip install -r requirements.py


- Set raspi-config settings

      sudo raspi-config nonint do_i2c 0  # Enable I2C
