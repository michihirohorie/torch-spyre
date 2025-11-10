#!/bin/bash
changed=0
echo "Testing..."
for file in "$@"; do
    echo "Formatting $file..."
    before_hash=$(md5sum "$file")
    clang-format --style=file -i "$file"
    after_hash=$(md5sum "$file")
    if [[ "$before_hash" != "$after_hash" ]]; then
        echo "Formatted: $file"
        changed=1
    fi
done
exit $changed
