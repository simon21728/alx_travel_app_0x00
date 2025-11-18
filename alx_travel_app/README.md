#!/bin/bash

FILES=("README.md" "listings/models.py" "listings/serializers.py")

for FILE in "${FILES[@]}"; do
    if [ -f "$FILE" ] && [ -s "$FILE" ]; then
        echo "$FILE exists and is not empty ✅"
    else
        echo "$FILE is missing or empty ❌"
    fi
done
