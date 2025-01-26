# ROBOBUDDY🎯


## Basic Details
### Team Name: [DARSHANA]


### Team Members
- Member 1: Gopika S - saintgits college of engineering
- Member 2: Navya Theresa Chacko -  saintgits college of engineering
- Member 3: Swetha Rachel Ninan-  saintgits college of engineering

### Hosted Project Link
[mention your project hosted project link here]

### Project Description

The primary goal of Robo Buddy is to create an engaging, interactive, and customizable robotic eye system that can display a variety of emotional expressions with fluid animation and smooth transitions. This is achieved through the development of the FluxGarage RoboEyes Arduino library, which simplifies the process of programming and controlling the robot's eyes. By designing a configuration board (a simple breadboard circuit), users can explore and test the library's capabilities in a hands-on, playful way.


### The Problem statement
The problem-solving aim of your project could be summarized as follows:
Through this project, we aim to solve the challenge of creating expressive and dynamic robotic eyes that are easy to customize for different designs and applications, while also providing an accessible tool for others to experiment and build upon the system.Robo buddy also offers a companionship to the user like when a sad person wants a companion to be sad with him/her they can toggle to sad mode in robo buddy. 


### The Solution
Creating an Engaging, Interactive Robotic Eye System.
Simplifying Programming and Control: The library would act as a high-level abstraction over hardware, making it easier for users to control eye movements. You would need to create functions for setting eye positions, controlling the animation speed, and adding expressions.


## Technical Details
Used both hardware and software.
### Technologies/Components Used
For Software:
Arduino IDE(C program)
For Hardware:
Fullsize breadboard
Arduino uno 
An I2C oled display with 1306 or 1309 driver chip
4 pushbuttons
Jumper wires
A USB cable to upload sketches to your controller
Some adhesive (washi-)tape to label the buttons (optional)

### Implementation
For Software: Arduino IDE
# Installation
Attach the Arduino, the display and the buttons to the breadboard. use similar positions for each component..
Connect the Arduino's 5V out to the breadboard's plus-line and the Arduino's GND to the breadboard's minus line.
It's helpful to also wire the just connected plus and minus lines with the respective plus and minus lines on the opposite side of the breadboard.
Connect the display's...
... GND to the breadboard's minus line
... VCC to the breadboard'S plus line
... SCL/SCK to the controller's I2C serial clock pin (=A5 on Arduino Uno or Nano R3)
... SDA to the controller's I2C serial data pin (=A4 on Arduino Uno or Nano R3)
Connect each pushbutton's upper right leg to the breadboard's minus line (see picture for reference), then connect each pushbutton's upper left leg to the following Arduino pin (no resistors needed, we'll use the Arduino's internal pullup resistors):
laugh button t0 D2
sad button to D3
angry button to D4
confused button to D5


Step 2: Upload Sketch
Once the hardware is ready to go, connect your arduino to your computer. In the Arduino IDE, go to "file > examples > FluxGarage RoboEyes for OLED Displays" and open the "ConfigurationBoard" example.

Then upload this sketch to your Arduino.

Step 3: Play Around
Now it's time to play around with the board and to create your custom eye shapes, if you want to. Initially, the eyes start with the "autoblinker" and the "idle mode" turned on, meaning the eyes will blink and reposition automatically.


Mood Button

By pushing the mood button, you can switch between the different mood types. Currently, "tired, angry, happy and default" are available.

Trigger Animations

Pressing "laugh, confused or flicker" triggers the respective animations, while laugh and confused are oneshot animations and flicker is an infinite loop animation that will be "played" as long as you hold the button (the library allows to set the flicker on or off, as well as setting a pixel value for the amplitude).

Eyes Configuration Buttons

The "mode" button allows you to switch between the eye manipulation modes listed below. Use the plus or minus button to increase or decrease the values inside of each "mode". Behind each mode title that will be displayed shortly, there is the current value of the width, height, border radius and the space between. This can be helpful if you want to write down the values for later use, since the configuration won't be saved when unpowering your arduino.

Step 4: Post Pictures or Videos of Your Robots With RoboEyes
You have now everything at hand to equip your own robot with smoothly animated eyes.


# Run
[commands]

### Project Documentation
FluxGarage RoboEyes is an Arduino library for controlling expressive robotic eyes.
The library enables smooth eye movements, emotional expressions, and animations using servos.
Key functions include setEyePosition(x, y), setEmotion(emotion), and setSpeed(speed).
Install via Arduino IDE by searching for "FluxGarage RoboEyes" or importing a .zip file.
Supports emotions like happy, sad, surprised, and angry with customizable transitions.
Requires Servo and Ease libraries for servo control and smooth animations.
Example code provided for basic eye movement and emotional display.
Allows dynamic control via potentiometers or buttons for interactive adjustments.
Open-source under the MIT License, encouraging contributions and modifications.
Full setup instructions and code examples available in the documentation.

# Screenshots (Add at least 3)

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
![Workflow](Add your workflow/architecture diagram here)
*Add caption explaining your workflow*

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Team](Add photo of your team here)


![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Name 1]: [Specific contributions]
- [Name 2]: [Specific contributions]
- [Name 3]: [Specific contributions]

---
Made with ❤️ at TinkerHub
