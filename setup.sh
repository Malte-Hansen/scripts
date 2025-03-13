#!/bin/bash

echo "Initializing scripts"

mkdir -p bin

# Loop through each subdirectory, mark scripts as executable and install dependencies
for dir in $(find . -type d -not -path "*.git*" -not -path "*venv*"); do
    echo -e "\nProcessing directory: $dir"

    # Find and mark Python files with a shebang as executable
    for script in $(find "$dir" -maxdepth 1 -type f -name "*.py"); do
        chmod +x "$script";
        filename="$(basename "$script" .py)"
        ln "$script" "bin/$filename"
        echo "Processed: $filename"
    done

    # Install dependencies
    if [[ -f "$dir/requirements.txt" ]]; then
        cd $dir
        echo "Installing Python requirements for $dir"
        python -m venv venv
        pip install -r "requirements.txt"
        cd -
    fi
done

echo -e "\nAll Python scripts with a shebang have been marked as a executable and linked to bin folder."
echo "All dependencies have been installed."
