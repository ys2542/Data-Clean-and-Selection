# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)

# Problem

Read a CSV file without any libraries to specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.


# Approach

Use Python dictionary to store the information and its sorted() function to get top 10 values.

# Run Instructions

For example, python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt 2 5 24 50

[0] ./src/h1b_counting.py (source file path)
[1] ./input/h1b_input.csv (input csv file path)
[2] ./output/top_10_occupations.txt (output file path)
[3] ./output/top_10_states.txt (output file path)
[4] 2 (column index of visa status)
[5] 5 (column index of visa type)
[6] 24 (column index of occupation)
[7] 50 (column index of state)

