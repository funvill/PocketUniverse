#include <Adafruit_NeoPixel.h>
#include <avr/power.h>

#define PIN 6

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(32*10, PIN, NEO_GRB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
  // This is for Trinket 5V 16MHz, you can remove these three lines if you are not using a Trinket
#if defined (__AVR_ATtiny85__)
  if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif
  // End of trinket special code


  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  /*
  // Some example procedures showing how to display to the pixels:
  colorWipe(strip.Color(255, 0, 0), 10); // Red
  colorWipe(strip.Color(0, 255, 0), 10); // Green
  colorWipe(strip.Color(0, 0, 255), 10); // Blue
  // Send a theater pixel chase in...

  theaterChase(strip.Color(127, 127, 127), 50, 100); // White
  theaterChase(strip.Color(127,   0,   0), 50, 100); // Red
  theaterChase(strip.Color(  0,   0, 127), 50, 100); // Blue
  */
  /*
  for(int cycle = 0 ; cycle < 5; cycle++ ) {
    rainbow(20);
  }
  
  for(int cycle = 0 ; cycle < 5; cycle++ ) {
    theaterChaseRainbow(50);
  }
  */
  fader(10, 10, 10 ); 
  
  
}

void fader( int numOfSnakes, int lengthOfSnake, int wait ) {
  
    for(int offset=0; offset<strip.numPixels(); offset++) 
    {
      // Set everything to black. 
      for(int i=0; i<strip.numPixels(); i++) {
        strip.setPixelColor(i, strip.Color(0, 0, 0) );        
      }
      
      // Loop thought the snakes 
      for( int offsetSnake=0; offsetSnake<numOfSnakes; offsetSnake++) {
        // Each snake is lengthOfSnake long. 
        for( int offsetLengthOfSnake=0; offsetLengthOfSnake<lengthOfSnake; offsetLengthOfSnake++ ) {

          int pixelIndex = offset+offsetLengthOfSnake+(offsetSnake*(strip.numPixels()/numOfSnakes)) ;
          if( pixelIndex > strip.numPixels() ) {
            pixelIndex -= strip.numPixels(); 
          }
          
          uint32_t pixelColor = Wheel( (offsetLengthOfSnake* (255/lengthOfSnake) & 255) )  ; 
          strip.setPixelColor(pixelIndex, pixelColor );
          
        }
      }       
      strip.show();
      delay(wait);        
     }
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}

void rainbow(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256; j++) {
    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

//Theatre-style crawling lights.
void theaterChase(uint32_t c, uint8_t wait, int cycles) {
  for (int j=0; j<cycles; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();
     
      delay(wait);
     
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}

//Theatre-style crawling lights with rainbow effect
void theaterChaseRainbow(uint8_t wait) {
  for (int j=0; j < 256; j++) {     // cycle all 256 colors in the wheel
    for (int q=0; q < 3; q++) {
        for (int i=0; i < strip.numPixels(); i=i+3) {
          strip.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
        }
        strip.show();
       
        delay(wait);
       
        for (int i=0; i < strip.numPixels(); i=i+3) {
          strip.setPixelColor(i+q, 0);        //turn every third pixel off
        }
    }
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else if(WheelPos < 170) {
    WheelPos -= 85;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  }
}

