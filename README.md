# Listener

## Overview
"Listener" is a Python script that serves as a basic reverse shell listener. It allows you to set up a network listener on your machine, which can be used to control and send commands to a remote computer when combined with a reverse shell payload.


## Usage
To use the "Listener" script, follow these steps:

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. 3. Open a terminal and execute the script with the following command:

   ```bash
   python3 Listener.py

   
 1. The script will start listening on the specified IP address and port (configured in the script itself). It will display output from the remote computer and allow you to send commands to it.

 2. On the remote computer, you will need to run a reverse shell payload or script to establish a connection with the listener. The specific payload will depend on your use case and goals. Ensure you have proper authorization to use the reverse shell.

 3. Once the connection is established, you can interact with the remote computer through the listener's terminal interface.

Disclaimer
This project is intended for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal and unethical. Use this script responsibly and with the appropriate permissions.

Happy coding!

