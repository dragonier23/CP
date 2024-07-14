#!/bin/bash

# Check if both arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <path_to_base> <problem_name>"
    exit 1
fi

# Assign the arguments to variables
base_path="$1"
problem_name="$2"

text_file="$base_path/data/kattis_$problem_name.txt"
cpp_file="$base_path/kattis_$problem_name.cpp"
output_file="$base_path/bin/kattis_$problem_name"

g++ -o "$output_file" "$cpp_file"

if [ $? -eq 0 ]; then
    echo "Compilation successful. Executable created at: $output_file"
else
    echo "Compilation failed."
    exit 1
fi

cat "$text_file" | ./"$output_file"