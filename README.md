# RandomCoffee
Python Script to match people in groups of 2 from a list. (In this case for coffee pairs in slack)

# Prerequisites

- Python must be installed on the system.

# Setup

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

## Error Handling
If it does not work, try executing the script via the terminal `./randomCoffee.py`. It should display an error message if it fails. One possible error is that it cannot find "python3". If that is the case, you can try changing the first line in the script to `#!/usr/bin/env python`

# How to use
1. If the setup worked, simply double click the application. A terminal window will open up with instructions:
  ```
  Export Members by typing /who in the slack channel
  Enter members:
  ```
2. Go to the desired slack channel and type in `/who` in the message field and hit ENTER.
3. The slackbot will output a list of all the members that are currently in the channel. Highlight and copy the comma-separated list of tags.
4. Paste the list into a text field (for example the message field of slack).
   > !! Pasting the list directly into the terminal window will not work, due to faulty line breaks!!
5. Now copy the list you just pasted into the message field and paste it into the terminal and hit ENTER.
6. The terminal outputs the number of members (useful for double checking if you missed someone when copying the usernames) and the list of matches
   ```
   Enter Members:
   R, A, T, P, SP, TA, G
   Number of Members 7

    - A ☕️ T
    - G ☕️ R
    - P ☕️ TA ☕️ SP
   ```
7. You can copy the list of matches and close the terminal window afterwards.
