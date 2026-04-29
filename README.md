# PROJECT TITLE
Dodge or Die!
## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: <URL>
https://github.com/alayaa128/Final-Project.git

## Description
Dodge or Die! is my final project of a simple dodge ball game. The player controls the character, the green circle in the bottom middle of the screen, with the arrow keys to dodge the dark blue circles raining down and get to the cyan rectangle. Once you get the green circle to the cyan rectangle you win and "You Win!" text displays along with a corresponding sound effect. If you get hit by the dark blue circles you will lose a life. You have three lives/ chances to get hit before red text reading "Game Over" displays and you have lost the game. Text displaying how many lives are left is seen in the upper right hand corner of the screen in yellow. 

class Character()
This class represents the green circle. It holds its self identities, moving it with the arrow keys, and draw function. This is the character that the player moves to win the game.

class Obstacle()
This class represents the falling obstacles. More specifically just one of them. It holds the self identities, the update funciton that allows the obstacle to move down the screen, and the draw function.

class Obstacle_Rain()
This class takes the obstacles from class Obstacle() and duplicates them so that there are multiple that rain down from random spots along the width of the screen.

def hit_obstacle(rain, character, lives, hit)
This function recognises when the character is hit by an obstacle from the Obstacle_Rain(). This reflects the life and hit count, and triggers got_hit to be True. It then returns lives, hit, and got_hit.

def is_game_over(hit, win)
This function returns true if the character has been hit 3 times by the obstacles.

def is_win(safe, character)
This function returns true if the character hit the safe rectangle.

def sound_effects(win, game_over, got_hit, win_sound, game_over_sound, hit_sound, played_win_sound, played_hit, played_game_over_sound)
This function plays the sound effects in the game. It is responsible for the win_sound, hit_sound, and game_over_sound. They play at their respectible times.

def display_text(win, game_over, screen, lives)
This function displays the "You Win!", "Game Over", and "Lives:(int)" text at the cooresponding time.

def main()
The main function initializes the game and everything in it. It contains my game loop. I also call all of my functions here so that they are implemented onto the screen. I also have the background music implemented here. 

The different files in my src folder other than my project code are sound files. The 'background music.mp3' is the background music, 'game over.mp3' is the sound that plays when the "Game Over" text displays, 'hit sound.mp3' is the sound that plays when the green circle gets hit and loses a life, and the 'win sound.mp3' is the sound that plays when the green circle enters the cyan rectangle. 

When picking the colors for everything, I wanted the character and win rectangle to stand out so I made them vibrant colors. The blue circles raining down are the enemy so they are less vibrant. The life count in the upper right corner is yellow so that it stands out against the background and the other elements in the game. The arrow keys move the circle by 600 pixels in each direction. Hold down the arrow keys to move the circle. It will move continuously, so the 600 controls the speed. I found that number to be the best combination of not too slow to win but not too fast to never lose either. I had to learn almost every feature I added to this game. I read the documentation for many different pygame features and learned how to incorporate them into my code. I worked on this project for over 30 hours to get everything to look and sound like I wanted it to. I am very happy and proud of the outcome of this game.

For improvement, I would like to add more game details. The blue circles could 'explode' on impact and have a particle animation. I could create an actual drawn character to use to control instead of it just being a circle. I could also add in drawn enemies. This would make the game look more interesting.
