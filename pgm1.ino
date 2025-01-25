#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Define the OLED screen dimensions
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

// I2C address of the SSD1306 OLED display (commonly 0x3C)
#define OLED_I2C_ADDRESS 0x3C

// Create an SSD1306 display object
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  // Initialize the display
  if (!display.begin(OLED_I2C_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;); // Stay here if initialization fails
  }

  display.clearDisplay();
  display.setTextSize(1); // Text size
  display.setTextColor(SSD1306_WHITE); // Text color
  display.setCursor(0, 0); // Set the starting position
  Serial.begin(9600);      // Start serial communication
  display.display();
}

void loop() {
  if (Serial.available() > 0) {
    String text = Serial.readStringUntil('\n'); // Read
    display.clearDisplay(); // Clear the screen
    display.setCursor(0, 0); // Reset cursor
    display.println(text);   // Display the text
    display.display();      // Update the display
  }
}
