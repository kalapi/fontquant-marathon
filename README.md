### FontQuant Marathon

#### Warning

This project is a work in progress and none of the tools are production ready. Please use them at your own risk.

#### Installation and use

1. Start by setting up a Python 3.8 virtual environment using `venv`.
2. Install `fontquant` using the instructions on the [FontQuant repository](https://github.com/googlefonts/fontquant).
3. Clone the [google/fonts](https://github.com/google/fonts) repository to get access to all the Google Fonts binaries
4. Run the script as follows:
```
python marathon.py <path to google/fonts/ofl directory> <path to output .csv file>
```

#### Notes

- The script takes approximately 1.2 mins per font file (on a 2019 Intel Core i9 2.4 GHz 8-core MacBook Pro; could be faster on an M1/2 Mac), so to run all 1650 fonts will take almost 2 days per attribute. You can run it on a smaller set of fonts to debug and check results

