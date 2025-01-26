#include <Adafruit_SSD1306.h>
#include <FluxGarage_RoboEyes.h>

// OLED display dimensions and setup
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// RoboEyes instance
roboEyes roboEyes;

// Button pin definitions
#define BUTTON_HAPPY 2
#define BUTTON_ANGRY 3
#define BUTTON_TIRED 4
#define BUTTON_CONFUSED 5

// Variable to track the current emotion
String currentEmotion = "DEFAULT";

void setup() {
  Serial.begin(9600);

  // Initialize OLED Display
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3C
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }
  display.clearDisplay();
  display.display();

  // Initialize RoboEyes
  roboEyes.begin(SCREEN_WIDTH, SCREEN_HEIGHT, 100);
  roboEyes.setAutoblinker(ON, 3, 2);
  roboEyes.setIdleMode(ON, 2, 2);

  // Initialize button pins as input with pull-up resistors
  pinMode(BUTTON_HAPPY, INPUT_PULLUP);
  pinMode(BUTTON_ANGRY, INPUT_PULLUP);
  pinMode(BUTTON_TIRED, INPUT_PULLUP);
  pinMode(BUTTON_CONFUSED, INPUT_PULLUP);

  Serial.println("System ready! Press buttons to change emotions.");
}

void loop() {
  // Check button states and trigger corresponding emotions
  if (digitalRead(BUTTON_HAPPY) == LOW) {
    currentEmotion = "HAPPY";
    Serial.println("Happy mode activated!");
    roboEyes.setMood(HAPPY);
  } 
  else if (digitalRead(BUTTON_ANGRY) == LOW) {
    currentEmotion = "ANGRY";
    Serial.println("Angry mode activated!");
    roboEyes.setMood(ANGRY);
  } 
  else if (digitalRead(BUTTON_TIRED) == LOW) {
    currentEmotion = "TIRED";
    Serial.println("Tired mode activated!");
    roboEyes.setMood(TIRED);
  } 
  else if (digitalRead(BUTTON_CONFUSED) == LOW) {
    currentEmotion = "CONFUSED";
    Serial.println("Confused animation activated!");
    roboEyes.anim_confused(); // Play the confused animation
  }

  // Optionally, print the current emotion on the OLED display
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Current Emotion:");
  display.println(currentEmotion);
  display.display();

  // Update RoboEyes to reflect changes
  roboEyes.update();

  delay(100); // Small delay for debouncing
}
