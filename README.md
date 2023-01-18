# RandomCoffee
Python Script to match people in groups of 2 from a list. (In this case for coffee pairs in slack)

# Prerequisites

- Python must be installed on the system.

# How to use

1. Download the randomCoffee.py file and put it into a folder of your choice
2. If you are the organizer and want to participate in the randomCoffee matching, feel free to edit the script by including the commented out lines and adding your own slack username in the script.
   ```python
    if '@YourSlackTag' not in members_list:
        members_list.append('@YourSlackTag')
    ```
3. Open a terminal at that folder (on mac rightclick on folder -> "New Terminal at Folder")
4. Make the file executable by running the following command
   ```shell
    chmod +x randomCoffee.py
    ```
5. Now you should be able to run the script by double-clicking it in the finder.

# Error Handling
If it does not work, try executing the script via the terminal `./randomCoffee.py`. It should display an error message if it fails. One possible error is that it cannot find "python3". If that is the case, you can try changing the first line in the script to `#!/usr/bin/env python`