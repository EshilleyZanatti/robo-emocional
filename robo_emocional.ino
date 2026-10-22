#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

void setup() {
  Serial.begin(9600);

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    while (true);
  }

  display.clearDisplay();
  display.display();

  mostrarRosto("NEUTRO");
}

void loop() {
  if (Serial.available()) {
    String emocao = Serial.readStringUntil('\n');
    emocao.trim();

    mostrarRosto(emocao);
  }
}

void mostrarRosto(String emocao) {

  display.clearDisplay();

  // =========================
  // FELIZ
  // =========================
  if (emocao == "FELIZ") {

    // Olho esquerdo
    display.fillCircle(38, 27, 7, WHITE);

    // Olho direito
    display.fillCircle(90, 27, 7, WHITE);

    // Pupilas
    display.fillCircle(38, 27, 3, BLACK);
    display.fillCircle(90, 27, 3, BLACK);

    // Boca sorrindo
    display.drawCircle(64, 42, 10, WHITE);
    display.fillRect(52, 32, 24, 10, BLACK);

  }

  // =========================
  // SURPRESO
  // =========================
  else if (emocao == "SURPRESO") {

    // Olhos grandes
    display.fillCircle(38, 27, 11, WHITE);
    display.fillCircle(90, 27, 11, WHITE);

    // Pupilas
    display.fillCircle(38, 27, 5, BLACK);
    display.fillCircle(90, 27, 5, BLACK);

    // Boca aberta
    display.fillCircle(64, 48, 8, WHITE);
    display.fillCircle(64, 48, 4, BLACK);

  }

  // =========================
  // TRISTE
  // =========================
  else if (emocao == "TRISTE") {

    // Olhos
    display.fillCircle(38, 29, 7, WHITE);
    display.fillCircle(90, 29, 7, WHITE);

    // Pupilas
    display.fillCircle(38, 29, 3, BLACK);
    display.fillCircle(90, 29, 3, BLACK);

    // Sobrancelhas tristes
    display.drawLine(28, 18, 48, 23, WHITE);
    display.drawLine(80, 23, 100, 18, WHITE);

    // Boca triste
    display.drawLine(52, 49, 58, 45, WHITE);
    display.drawLine(58, 45, 64, 44, WHITE);
    display.drawLine(64, 44, 70, 45, WHITE);
    display.drawLine(70, 45, 76, 49, WHITE);

  }

  // =========================
  // BRAVO
  // =========================
  else if (emocao == "BRAVO") {

    // Sobrancelhas
    display.drawLine(27, 18, 49, 24, WHITE);
    display.drawLine(79, 24, 101, 18, WHITE);

    // Olhos
    display.fillCircle(38, 30, 7, WHITE);
    display.fillCircle(90, 30, 7, WHITE);

    // Pupilas
    display.fillCircle(38, 30, 3, BLACK);
    display.fillCircle(90, 30, 3, BLACK);

    // Boca séria
    display.drawLine(52, 48, 76, 48, WHITE);

  }

  // =========================
  // NEUTRO
  // =========================
  else {

    // Olhos
    display.fillCircle(38, 27, 7, WHITE);
    display.fillCircle(90, 27, 7, WHITE);

    // Pupilas
    display.fillCircle(38, 27, 3, BLACK);
    display.fillCircle(90, 27, 3, BLACK);

    // Boca neutra
    display.drawLine(52, 47, 76, 47, WHITE);
  }

  display.display();
}