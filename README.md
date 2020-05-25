# Convert Steganos CSV to Bitwarden CSV
A quick and dirty Python3 script to convert Steganos CSV files into Bitwarden CSV files. This is very useful when you want to move your passwords from Steganos to Bitwarden - just export your passwords to a CSV file on Steganos, run this script, and import the resulting CSV in Bitwarden. 

## How to use it?
Make sure you're using Python3 and you have `pandas` installed.
```shell
python steganos_to_bitwarden.py
```

## Disclaimer
This script will only consider "type 5" entries (your typical uri+username+password combo), any other entries will be left out. Take a look at your CSV to check if you have other entries, and then either manually add them or modify the script (and make a PR when you're done :) )
The CSV formats of Steganos and Bitwarden might also change in the future - in which case this script might at least be a good starting point. Godspeed.
