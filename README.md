# Duplicate Payment Challenge - Duplid.de

This repo contains my submission for the duplicate invoice coding challenge given to me by Duplid.de. The repo is organised as follows:
* `src/` : Directory housing the source code using to complete the challenge. I made use of a makefile Template for Python I created in to enable my application be run on multiple platfroms with minimal challenges.
* `data/` : Directory housing the source data set `.csv` file and the found duplicates in a separate `.csv` file.


# Instructions to Run

1. `git clone https://github.com/pmessan/duplicate_invoice_finder.git` OR  
`gh repo clone pmessan/duplicate_invoice_finder` 
(if you have GitHub CLI installed)
2. `cd duplicate_invoice_finder/src/`.
3. `make run` to install dependencies and run the script.
4. \[Optional\]  
To clean up the virtual environment files generated, run `make clean` in `duplicate_invoice_finder/src/`.
