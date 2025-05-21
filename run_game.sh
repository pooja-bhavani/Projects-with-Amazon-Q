#!/bin/bash

# Check if pygame is installed
python3 -c "import pygame" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Pygame is not installed. Installing now..."
    pip3 install pygame
fi

# Run the game
python3 roadrash.py
