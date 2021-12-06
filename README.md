# DinoPlay
Computer playing Chrome Dino Game by itself


# Considerations
This extension brings Google's Dinosaur Game, also known as T-Rex Game and Dino Runner to your browser toolbar area. Simply press the action button and play it inside the popup area. You can press the Escape key to close the popup and stop the game.

How to access:

Just type chrome://dino/ in your chrome address bar

How to play:

Click on the action button to launch the game in which the player controls a running dinosaur by pressing space or down arrow key to avoid obstacles, including cactus and pterodactyls. When the player reaches 700 points, the game begins to switch between day (white background, black lines, and shapes) and night (black background, white lines, and shapes).

# Code considerations (here to be changed)
- It uses screenshots, so you have to split screen and activate chromewindows after start to run
- The obstacles comes ahead randomly, so don't try to memorize them
- Use of cropped area to identify obstacles
- As is used the number of pixels with same color, don't need to check background everytime. This reduced number of code lines and the gradient of colors when transitioning between day and night
- 
