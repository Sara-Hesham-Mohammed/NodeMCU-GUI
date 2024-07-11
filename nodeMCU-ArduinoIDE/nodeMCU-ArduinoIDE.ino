#include <ESP8266WiFi.h>

// Set these to your desired credentials.
const char *ssid = "NodeMCU_AP";
const char *password = "password";

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  //Serial.begin(9600); //written on the nodeMCU itself
  
  // Set up the Access Point
  WiFi.softAP(ssid, password);
  
  // Start the server
  server.begin();
  Serial.println("Server started");
  
  // Print the IP address
  Serial.print("AP IP address: ");
  Serial.println(WiFi.softAPIP());
}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New client");
    String currentLine = "";
    
    // Loop while the client's connected
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        // Read the HTTP request
        if (c == '\n') {
          // Send a response
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/plain");
          client.println("Connection: close");
          client.println();
          client.println("Hello from NodeMCU!");
          break;
        } else {
          currentLine += c;
        }
      }
    }
    // Close the connection
    client.stop();
    Serial.println("Client disconnected");
  }
}
