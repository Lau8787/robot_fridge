# robot_fridge

## Install

- Set-up ssh:

      cat << EOF >> "${HOME}/.ssh/config"

      Host pi
            User pi
            HostName 192.168.2.200
      EOF

- Install dependencies:

      sudo apt-get update
      sudo apt-get install -y python3-pip
      sudo apt-get install -y python3-venv
      sudo apt-get install -y i2c-tools
      sudo apt-get install build-essential python3-dev git

- Create the virtual env:

    python3 -m venv .venv

- Activate the virtual env:

      source ./venv

- Install python packages:

      pip install -r requirements.txt


- Set raspi-config settings

      sudo raspi-config nonint do_i2c 0  # Enable I2C
