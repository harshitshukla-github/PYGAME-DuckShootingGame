# DUCK SHOOTING GAME IN PYGAME
Imports and Initialization:

The program starts by importing necessary modules, such as os, random, sys, and pygame.
<code>pygame.init()</code> initializes all the pygame modules.
The mouse cursor is made invisible to replace it with a custom crosshair for aiming.
Setup Variables and Constants:

Screen dimensions and frames per second (FPS) are set.
The color for the sky is defined.
A clock is created for controlling the game's frames per second.
Fonts and Text:

Two different fonts are initialized for displaying text on the screen.
Classes Creation:

The game includes several classes to manage different game elements:
Font for showing text.
Cloud for floating clouds in the background.
Ducks for the ducks that need to be shot.
These classes contain methods for drawing themselves on the screen and updating their positions.
Game Application (App) Class:

This is the main controller class for the game.
It initializes the game window, loads background images, manages the crosshair image, tracks the score, and holds the game timer.
It controls the game loop, handling user input, updating game state, and rendering the graphics.
It decides the game's end condition if the time is up (defeat) or all ducks are shot (victory), showing appropriate messages from messages.py.
Game Loop (control method):

The loop runs as long as the game is active.
It handles quit events and mouse movement to position the crosshair.
It updates and draws clouds and ducks, moves the land and water backgrounds, and updates the score and timer.
When the player shoots, the corresponding duck is removed from the list, incrementing the score.
When time is up or all ducks are shot, the game displays a defeat or victory message and stops updating the game elements.
Main Game Execution:

Clouds are instantiated at various positions.
Ducks are created and placed randomly on the screen.
An instance of the App class is created, which starts the game when its control method is called.
In essence, running main.py starts a duck shooting game where you aim with a crosshair controlled by the mouse, trying to shoot all ducks before time runs out. The screen displays a live score and a countdown timer, and the game concludes with a victory or defeat message based on the outcome.