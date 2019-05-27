# Python environment setup guideline
This is the Python environment setup guideline. To properly launch the project in Jupyter Notebook, follow these instructions.
These guideline is targeted for Fedora distribution. The guideline content is using Python 3.0 release or higher.

The machine learning development guideline is located in development_examples directory.

The script dependencies_extracter_script.sh was used to obtain all the correctly included dependencies from Fedora RPM repository.
The obtained dependencies were then saved to dependencies_extracted_from_specs folder.

The url of the official GitHub repository is https://github.com/xtuchyna/bachelor_thesis.git

# Python and pip tool
First we need to make sure that Python is installed on our system.

```sh
$ dnf install python3
```

Then we need to also make sure the pip package manager is installed.

```sh
$ dnf install python3-pip
```

# Libraries installation
We can start installing our desired libraries that we need for machine learning project development.

```sh
$ pip3 install --user --upgrade jupyter matplotlib numpy scipy scikit-learn
```

Next we also need to install custom libraries from PyPi used in association rule learning approaches.
```sh
$ pip3 install --user --upgrade apyori pyfpgrowth
```

To install any other libraries, just use the pip command in previously mentioned manner like this:
```sh
$ pip3 install --user <desired_library>
```

# Launch the guideline content written in Jupyter Notebook.
To launch the Jupyter Notebook, simply run this command from this directory

```sh
$ jupyter notebook
```

The jupyter should automatically open a web browser with project in it. If not, the default url for that Jupyter uses is
http://localhost:8888/