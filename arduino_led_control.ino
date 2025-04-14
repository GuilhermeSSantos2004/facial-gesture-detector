

void setup() {
  Serial.begin(9600);

  pinMode(7, OUTPUT); // Vermelho: Mão direita acima da cabeça
  pinMode(5 , OUTPUT); // Verde: Mão esquerda acima da cabeça
  pinMode(4, OUTPUT); // Azul: Olho direito fechado
  pinMode(6, OUTPUT); // Amarelo: Olho esquerdo fechado
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    switch (command) {
      // Mão direita (Vermelho)
      case 'R': digitalWrite(7, HIGH); break; // Liga LED (mão direita levantada)
      case 'r': digitalWrite(7, LOW); break;  // Desliga LED (mão direita abaixada)

      // Mão esquerda (Verde)
      case 'G': digitalWrite(5, HIGH); break; // Liga LED (mão esquerda levantada)
      case 'g': digitalWrite(5, LOW); break;  // Desliga LED (mão esquerda abaixada)

      // Olho direito (Azul)
      case 'B': digitalWrite(4, HIGH); break; // Liga LED (olho direito fechado)
      case 'b': digitalWrite(4, LOW); break;  // Desliga LED (olho direito aberto)

      // Olho esquerdo (Amarelo)
      case 'Y': digitalWrite(6, HIGH); break; // Liga LED (olho esquerdo fechado)
      case 'y': digitalWrite(6, LOW); break;  // Desliga LED (olho esquerdo aberto)
    }
  }
}

