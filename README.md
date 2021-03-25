# Makefile Python Template
A template you can use for your python projects to enable cross-platform compatibilty using `make`.

## Details
There are different sub commands you can run using this template. The default is just `make`
* `make`: Default command with no arguments. Creates the virtual environment, and installs dependencies from the requirements.txt
* `make run`: Runs the script you specify in place of `<YOUR-SCRIPT>.py`. You can also create multiple run arguments in case you need to run separate scripts. Just copy-paste the run block, change the name from run to something like `run2`, and specify the script you want in place of `<YOUR-SCRIPT>.py`
* `make clean`: Cleans up the virtual environment files in case you need to tear down or you want to ship out the package.

Happy Coding ;)
