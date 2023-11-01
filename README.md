# Infinite Runner: An AI-Integrated Adventure

"Infinite Runner" is an exhilarating, side-scrolling game that combines the thrill of an infinite runner with the power of AI. The game is built using the Pygame library and offers an engaging gameplay experience that's reminiscent of classic infinite runner games.

## Game Overview

In "Infinite Runner", you control a character that must jump over incoming obstacles to keep running. The game starts with a scrolling background and the game begins. What sets this game apart is its use of AI: it integrates hand tracking to control the character, making for a unique and interactive gaming experience.

## Gameplay Mechanics

The gameplay mechanics are simple yet addictive. You control the character using hand gestures, detected through your webcam. Showing two fingers makes the character jump over obstacles. The game features a collision detection mechanism that ends the game if your character collides with an obstacle. The longer you can keep your character running without colliding into an obstacle, the higher your score!

## Features

- **AI Integration**: The game uses hand tracking to control the character. Show open palm to the webcam to make the character jump.
- **Scoring System**: Players earn points for each second they keep the character running.
- **Game Over Screen**: When the player loses, a game over screen is displayed with their score.
- **Background Music (BGM)**: The game features background music that adds to the immersive experience.

## Code Structure

The code is structured into one main script. It starts by importing necessary libraries and initializing Pygame. It then defines several functions for different parts of the game such as displaying scores, handling events, scrolling the background, detecting collisions, and managing player movements.

## Libraries Used

"Infinite Runner" utilizes several Python libraries:
- `pygame` for creating the game window, handling events, and rendering graphics.
- `random` for generating random values used in obstacle positioning.
- `math` for mathematical functions used in collision detection.
- `os` for interacting with the operating system.
- `cv2` for capturing video from webcam.
- `cvzone.HandTrackingModule` for hand tracking.

"Infinite Runner" is an exciting and engaging Python-based game that offers hours of fun. Whether you're a fan of infinite runner games or just love innovative uses of AI, "Infinite Runner" is sure to keep you entertained! So why wait? Start your infinite run today! :)
