# Duplicate Payment Challenge - Duplid

This repo contains my submission for [the duplicate invoice coding challenge](challenge.pdf) given to me by [duplid.de](https://duplid.de/en-gb/main/). The repo is organised as follows:
* [src/](src/) : Directory housing the source code used to complete the challenge. I made use of a makefile template for Python I created in [this repo](https://github.com/pmessan/makefile-python-template) to enable my application be run on multiple platforms with minimal challenges.
* [data/](data/) : Directory housing the source dataset CSV file and the found duplicates in a separate CSV file.

# General Requirements

- [Python 3.x](https://www.python.org/downloads/)
- [Python virtualenv package](https://pypi.org/project/virtualenv/)
- [make](https://www.gnu.org/software/make/)

The specific package requirements for this program can be found in [src/requirements.txt](src/requirements.txt)

# Instructions to Run

1. `git clone https://github.com/pmessan/duplicate_invoice_finder.git` OR  
`gh repo clone pmessan/duplicate_invoice_finder` 
(if you have GitHub CLI installed)
2. `cd duplicate_invoice_finder/src/`
3. `make run` to install dependencies and run the script.
4. \[Optional\] To clean up the virtual environment files generated, run `make clean` in `duplicate_invoice_finder/src/`.

Thanks for viewing!
