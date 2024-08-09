# Description: This script upgrades all outdated packages in the current Python environment.

"""
import json
import subprocess

try:
    # Execute the pip command and capture the output
    output = subprocess.check_output(["pip", "list", "--outdated", "--format=json"])
    output_string = output.decode("utf-8")
    data = json.loads(output_string)

    # Extract package names
    packages = [package["name"] for package in data]

    # Upgrade all packages in one command
    if packages:
        print(f"Upgrading packages: {' '.join(packages)}")
        subprocess.check_call(["pip", "install", "--upgrade"] + packages)
    else:
        print("All packages are up-to-date.")

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
"""
import json
import subprocess

try:
    # Execute the pip command and capture the output
    output = subprocess.check_output(
        ["pip", "list", "--outdated", "--format=json", "--user"]
    )
    output_string = output.decode("utf-8")
    data = json.loads(output_string)

    # Extract package names
    packages = [package["name"] for package in data]

    # Upgrade all packages in one command
    if packages:
        print(f"Upgrading packages: {' '.join(packages)}")
        subprocess.check_call(
            [
                "pip",
                "install",
                "--upgrade",
                "--user",
                "--no-dependencies",
                "--upgrade-strategy",
                "eager",
            ]
            + packages
        )
    else:
        print("All packages are up-to-date.")

except subprocess.CalledProcessError as e:
    print(f"Error occurred: {e}")
