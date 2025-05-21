# Road Rash 2D

A simple 2D Road Rash-style bike racing game built with Python and Pygame.

## Game Features

- Control your bike with arrow keys
- Avoid enemy bikers and obstacles
- Score increases as you pass enemies and obstacles
- Game over when you collide with enemies or obstacles
- Increasing difficulty as your score grows

## Controls

- **Left Arrow**: Move left
- **Right Arrow**: Move right
- **Up Arrow**: Move up
- **Down Arrow**: Move down
- **R**: Restart game after game over
- **Q**: Quit game after game over

## How to Run

Simply execute the run_game.sh script:

```bash
./run_game.sh
```

The script will automatically check if Pygame is installed and install it if needed.

## Game Elements

- **Red Bike**: Player
- **Green Bikes**: Enemy riders
- **Black Squares**: Obstacles
- **Gray Area**: Road
- **Green Areas**: Grass (off-road)

## Scoring

- +10 points for each enemy you pass
- +5 points for each obstacle you pass

## Requirements

- Python 3
- Pygame

## Custom Graphics

You can add your own graphics by placing the following files in the same directory:
- player_bike.png
- enemy_bike.png
- obstacle.png

If these files are not found, the game will use simple shapes as placeholders.
