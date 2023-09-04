import json
import os
import requests
import time

while True:

    if os.stat('fetch.txt').st_size != 0:
        with open('fetch.txt', 'r') as f:
            text_lines = f.readlines()[0:]
            line_1 = text_lines[0]
            f.close()

            # Check for request
            if len(text_lines) == 2 and line_1 == "run\n":
                line_2 = text_lines[1]  # Get URL from text file
                response = requests.get(line_2)  # Get request from API
                data = response.json()
                f.close()

                # Write data as string into text file
                with open('fetch.txt', 'w') as f:
                    json.dump(data, f)
                    f.close()