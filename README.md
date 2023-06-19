# parcial-1-labo
Juego tetris
### 📄Documentación de la parte práctica del primer parcial para la materia Sistemas de procesamiento de datos - UTN Tecnicatura Superior en Programación.

### Nombre: Bosco Mascaro Massimo Ariel

### **Sistema de Procesamiento de Datos (SPD)**

![Arduino](https://github.com/magikboy/Parcial-1/blob/30c7b791849ce1d70de15ec52cb6a92ac3aec450/ArduinoTinkercad.jpg)

### Modelo de montacarga funcional

![Montacargas de hospital](https://github.com/magikboy/Parcial-1/blob/1a975207471b0b0f8a8c081eb3d869e3463c76a1/tinkercad1.png)
### 🦴Modelo esquematico del montacargas

![Montacargas de hospital](https://github.com/magikboy/Parcial-1/blob/7917a8768ca4b1a21c14e51af70ec9adf790448b/imagen_2023-05-18_121209060.png)

## 📄Consigna Montacargas:
Se nos pide armar un modelo de montacarga funcional como maqueta para un hospital. El
objetivo es que implementes un sistema que pueda recibir ordenes de subir, bajar o pausar
desde diferentes pisos y muestre el estado actual del montacargas en el display 7 segmentos.

### 🚀Codigo del proyecto
``` C++
#define BOTON_SUBIR 2
#define BOTON_BAJAR 3
#define BOTON_PAUSAR 4
#define led_Verde 5
#define led_Rojo 6
#define A 7
#define B 8
#define C 9
#define D 10
#define E 11
#define F 12
#define G 13
const int TIEMPO_ESPERA_BOTON = 10; // Tiempo de espera entre lecturas de botones en milisegundos.
const int TIEMPO_POR_PISO = 3000; // Tiempo que tarda el montacargas en llegar a cada piso en milisegundos.
const int TIEMPO_ESPERA_MOVIMIENTO = 3000; // Tiempo de espera después de que se mueve el montacargas en milisegundos.

boolean botonSubir = false;
boolean botonBajar = false;
boolean botonPausa = false;

int contador = 0; //INICIALIZO EL CONTADOR EN 0
String mensaje = ""; //PARA PODER ESCRIBIR EN EL MONITOR

const char* mensajesPisos[] = {
  "Llego al piso 0.",
  "Llego al piso 1.",
  "Llego al piso 2.",
  "Llego al piso 3.",
  "Llego al piso 4.",
  "Llego al piso 5.",
  "Llego al piso 6.",
  "Llego al piso 7.",
  "Llego al piso 8.",
  "Llego al piso 9."
};

void mostrarPiso(int piso) {
switch(piso) {
  case 0:
  	cero(1);
  	break;
  case 1:
  	uno(1);
  	break;
  case 2:
    dos(1);
    break;
  case 3:
    tres(1);
    break;
  case 4:
    cuatro(1);
    break;
  case 5:
    cinco(1);
    break;
  case 6:
    seis(1);
    break;
  case 7:
    siete(1);
    break;
  case 8:
    ocho(1);
    break;
  case 9:
    nueve(1);
    break;
}
mensaje = mensajesPisos[piso];
}

void cambiarPiso(String direccion) {
  if (direccion == "subir" && contador < 9) {
    contador++;
  }
  else if (direccion == "bajar" && contador > 0) {
    contador--;
  }
}

int moverPiso(String subirBajar, int tiempoDelay)
{
  digitalWrite(led_Rojo, 0);
  cambiarPiso(subirBajar);
  mostrarPiso(contador);
  digitalWrite(led_Verde, 1);
  delay(tiempoDelay);
  digitalWrite(led_Verde , 0);
  displayOff();
  Serial.println(mensaje);
  return contador;
}

// FUNCIONES
void displayOff() // Apago display al salir del switch
{
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);
}

void cero(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, LOW);
}

void uno(int on)
{
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);
}

void dos(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, LOW);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, LOW);
  digitalWrite(G, HIGH);
}

void tres(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, HIGH);
}

void cuatro(int on)
{
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void cinco(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, LOW);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void seis(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, LOW);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void siete(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);
}

void ocho(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void nueve(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void todos(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void actualizarDisplay(int piso) {
  switch (piso) {
    case 1:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(G, LOW);
      break;
    case 2:
      digitalWrite(A, LOW);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, LOW);
      digitalWrite(E, LOW);
      digitalWrite(F, LOW);
      digitalWrite(G, LOW);
      break;
    case 3:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, LOW);
      digitalWrite(F, LOW);
      digitalWrite(G, HIGH);
      break;
    case 4:
      digitalWrite(A, LOW);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, LOW);
      digitalWrite(E, LOW);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
    case 5:
      digitalWrite(A, HIGH);
      digitalWrite(B, LOW);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, LOW);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
    case 6:
      digitalWrite(A, HIGH);
      digitalWrite(B, LOW);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
    case 7:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, LOW);
      digitalWrite(E, LOW);
      digitalWrite(F, LOW);
      digitalWrite(G, LOW);
      break;
    case 8:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
    case 9:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, LOW);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
  }
}
// FIN FUNCIONES

void setup() {
pinMode(BOTON_SUBIR, INPUT_PULLUP);
pinMode(BOTON_BAJAR, INPUT_PULLUP);
pinMode(BOTON_PAUSAR, INPUT_PULLUP);
pinMode(led_Rojo, OUTPUT);
pinMode(led_Verde, OUTPUT);
pinMode(A, OUTPUT);
pinMode(B, OUTPUT);
pinMode(C, OUTPUT);
pinMode(D, OUTPUT);
pinMode(E, OUTPUT);
pinMode(F, OUTPUT);
pinMode(G, OUTPUT);
Serial.begin(9600);
mostrarPiso(contador);
}

void loop() {
// Leer el estado de los botones
botonSubir = digitalRead(BOTON_SUBIR);
botonBajar = digitalRead(BOTON_BAJAR);
botonPausa = digitalRead(BOTON_PAUSAR);

// Si se presiona el botón de subir, mover hacia arriba
if (botonSubir == LOW) {
moverPiso("subir", TIEMPO_POR_PISO);
}

// Si se presiona el botón de bajar, mover hacia abajo
if (botonBajar == LOW) {
moverPiso("bajar", TIEMPO_POR_PISO);
}

// Si se presiona el botón de pausa, detener el movimiento
if (botonPausa == LOW) {
  mensaje = "El montacargas se detuvo";
  Serial.println(mensaje);
  digitalWrite(led_Verde, 0);
  digitalWrite(led_Rojo, 1);
  delay(TIEMPO_ESPERA_MOVIMIENTO);
  mostrarPiso(contador);
}
}
```
### 🤖Funcionando
![Montacargas de hospital](https://github.com/magikboy/Parcial-1/blob/655e31a70d93ce6f4b70d06eaaaa3bd76ab51a28/2023-05-16-11-57-43.gif)

### 🧠Explicacion

``` C++
#define BOTON_SUBIR 2
#define BOTON_BAJAR 3
#define BOTON_PAUSAR 4
#define led_Verde 5
#define led_Rojo 6
#define A 7
#define B 8
#define C 9
#define D 10
#define E 11
#define F 12
#define G 13
const int TIEMPO_ESPERA_BOTON = 10; // Tiempo de espera entre lecturas de botones en milisegundos.
const int TIEMPO_POR_PISO = 3000; // Tiempo que tarda el montacargas en llegar a cada piso en milisegundos.
const int TIEMPO_ESPERA_MOVIMIENTO = 3000; // Tiempo de espera después de que se mueve el montacargas en milisegundos.

boolean botonSubir = false;
boolean botonBajar = false;
boolean botonPausa = false;
boolean enMovimiento = false;

int contador = 0; //INICIALIZO EL CONTADOR EN 0
String mensaje = ""; //PARA PODER ESCRIBIR EN EL MONITOR

const char* mensajesPisos[] = {
  "Llego al piso 0.",
  "Llego al piso 1.",
  "Llego al piso 2.",
  "Llego al piso 3.",
  "Llego al piso 4.",
  "Llego al piso 5.",
  "Llego al piso 6.",
  "Llego al piso 7.",
  "Llego al piso 8.",
  "Llego al piso 9."
};
```

Las constantes definen los pines que se usan para los botones, LEDs y segmentos de un display de siete segmentos. También define los tiempos que tarda el montacargas en llegar a cada piso y el tiempo que se espera después de que se mueve el montacargas.

Las variables booleanas son para almacenar el estado de los botones y el estado de movimiento del montacargas.

El contador se inicializa en 0 y se utiliza para indicar el piso actual en el que se encuentra el montacargas. El array de mensajes de pisos se usa para almacenar mensajes de texto que indican el piso al que se mueve el montacargas.


``` C++
// FUNCIONES
void displayOff() // Apago display al salir del switch
{
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);
}

void cero(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, LOW);
}

void uno(int on)
{
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);
}

void dos(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, LOW);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, LOW);
  digitalWrite(G, HIGH);
}

void tres(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, HIGH);
}

void cuatro(int on)
{
  digitalWrite(A, LOW);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void cinco(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, LOW);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void seis(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, LOW);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void siete(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);
}

void ocho(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void nueve(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, LOW);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void todos(int on)
{
  digitalWrite(A, HIGH);
  digitalWrite(B, HIGH);
  digitalWrite(C, HIGH);
  digitalWrite(D, HIGH);
  digitalWrite(E, HIGH);
  digitalWrite(F, HIGH);
  digitalWrite(G, HIGH);
}

void actualizarDisplay(int piso) {
  switch (piso) {
    case 1:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(G, LOW);
      break;
    case 2:
      digitalWrite(A, LOW);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, LOW);
      digitalWrite(E, LOW);
      digitalWrite(F, LOW);
      digitalWrite(G, LOW);
      break;
    case 3:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, LOW);
      digitalWrite(F, LOW);
      digitalWrite(G, HIGH);
      break;
    case 4:
      digitalWrite(A, LOW);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, LOW);
      digitalWrite(E, LOW);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
    case 5:
      digitalWrite(A, HIGH);
      digitalWrite(B, LOW);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, LOW);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
    case 6:
      digitalWrite(A, HIGH);
      digitalWrite(B, LOW);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
    case 7:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, LOW);
      digitalWrite(E, LOW);
      digitalWrite(F, LOW);
      digitalWrite(G, LOW);
      break;
    case 8:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, HIGH);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
    case 9:
      digitalWrite(A, HIGH);
      digitalWrite(B, HIGH);
      digitalWrite(C, HIGH);
      digitalWrite(D, HIGH);
      digitalWrite(E, LOW);
      digitalWrite(F, HIGH);
      digitalWrite(G, HIGH);
      break;
  }
}
// FIN FUNCIONES
```
La función **displayOff()** se utiliza para apagar todos los segmentos del display cuando se sale del switch o se necesita apagar el display.

Las funciones **cero() a nueve()**se utilizan para mostrar los dígitos del 0 al 9 en el display. Cada función enciende los segmentos necesarios para mostrar el dígito correspondiente. Por ejemplo, la función cero() enciende todos los segmentos excepto el segmento G.

La función **todos()** enciende todos los segmentos del display, lo que resulta en la visualización del número 8.

La función **actualizarDisplay()** se utiliza para mostrar el número del piso en el que se encuentra un elevador, por ejemplo. Se utiliza un switch para seleccionar el número del piso y luego se llama a esta función para actualizar el display con el número correspondiente. La función toma como argumento el número del piso y utiliza los comandos digitalWrite() para encender los segmentos necesarios para mostrar el número en el display.

``` C++
void mostrarPiso(int piso) {
switch(piso) {
  case 0:
  	cero(1);
  	break;
  case 1:
  	uno(1);
  	break;
  case 2:
    dos(1);
    break;
  case 3:
    tres(1);
    break;
  case 4:
    cuatro(1);
    break;
  case 5:
    cinco(1);
    break;
  case 6:
    seis(1);
    break;
  case 7:
    siete(1);
    break;
  case 8:
    ocho(1);
    break;
  case 9:
    nueve(1);
    break;
}
mensaje = mensajesPisos[piso];
}

void cambiarPiso(String direccion) {
  if (direccion == "subir" && contador < 9) {
    contador++;
  }
  else if (direccion == "bajar" && contador > 0) {
    contador--;
  }
}

int moverPiso(String subirBajar, int tiempoDelay)
{
  digitalWrite(led_Rojo, 0);
  cambiarPiso(subirBajar);
  mostrarPiso(contador);
  digitalWrite(led_Verde, 1);
  delay(tiempoDelay);
  digitalWrite(led_Verde , 0);
  displayOff();
  Serial.println(mensaje);
  return contador;
}
```


**las funciones principales son**

**moverPiso()** La función principal del programa es moverPiso(), que se encarga de mover el montacargas a un piso determinado. Esta función recibe dos parámetros: subirBajar, que indica si el montacargas debe subir o bajar, y tiempoDelay, que indica cuánto tiempo debe esperar el programa después de que el montacargas se mueve.

Dentro de la función, primero se apaga el led rojo, se cambia el piso actual utilizando la función cambiarPiso(), se muestra el piso actual en el display utilizando la función mostrarPiso(), se enciende el led verde y se espera el tiempo indicado por el parámetro tiempoDelay. Luego se apaga el led verde, se apaga el display y se muestra un mensaje en el monitor serie indicando el piso al que se ha llegado.

**cambiarPiso()** La función cambiarPiso() se encarga de cambiar el piso actual del montacargas en función del parámetro subirBajar. Si subirBajar es "subir" y el contador actual es menor que 9, el contador se incrementa en 1. Si subirBajar es "bajar" y el contador actual es mayor que 0, el contador se decrementa en 1.

**mostrarPiso()** La función mostrarPiso() se encarga de mostrar el piso actual en el display utilizando las funciones para encender los diferentes segmentos correspondientes al número que indica el piso actual.

``` C++
void setup() {
pinMode(BOTON_SUBIR, INPUT_PULLUP);
pinMode(BOTON_BAJAR, INPUT_PULLUP);
pinMode(BOTON_PAUSAR, INPUT_PULLUP);
pinMode(led_Rojo, OUTPUT);
pinMode(led_Verde, OUTPUT);
pinMode(A, OUTPUT);
pinMode(B, OUTPUT);
pinMode(C, OUTPUT);
pinMode(D, OUTPUT);
pinMode(E, OUTPUT);
pinMode(F, OUTPUT);
pinMode(G, OUTPUT);
Serial.begin(9600);
mostrarPiso(contador);
}

void loop() {
// Leer el estado de los botones
botonSubir = digitalRead(BOTON_SUBIR);
botonBajar = digitalRead(BOTON_BAJAR);
botonPausa = digitalRead(BOTON_PAUSAR);

// Si se presiona el botón de subir, mover hacia arriba
if (botonSubir == LOW) {
moverPiso("subir", TIEMPO_POR_PISO);
}

// Si se presiona el botón de bajar, mover hacia abajo
if (botonBajar == LOW) {
moverPiso("bajar", TIEMPO_POR_PISO);
}

// Si se presiona el botón de pausa, detener el movimiento
if (botonPausa == LOW) {
  mensaje = "El montacargas se detuvo";
  Serial.println(mensaje);
  digitalWrite(led_Verde, 0);
  digitalWrite(led_Rojo, 1);
  delay(TIEMPO_ESPERA_MOVIMIENTO);
  mostrarPiso(contador);
}
}

```

La función **setup()** es una función que se ejecuta una sola vez al inicio del programa. En ella se inicializan los pines que se van a utilizar como entradas o salidas, y se establece la velocidad de comunicación para la interfaz serial (Serial.begin(9600)). Además, se llama a la función mostrarPiso() para que muestre el piso en el que se encuentra el montacargas en ese momento.

La variable **botonSubir** es una variable que se utiliza para almacenar el estado del botón de subir. Se lee su estado utilizando la función digitalRead(), que devuelve un valor HIGH o LOW dependiendo de si el botón está pulsado o no.

La variable **botonBajar** es una variable que se utiliza para almacenar el estado del botón de bajar. Se lee su estado utilizando la función digitalRead().

la variable **botonPausa** es una variable que se utiliza para almacenar el estado del botón de pausa. Se lee su estado utilizando la función digitalRead().

---
## <img src="tinkercad.png" alt="Tinkercad" height="32px"> Link al proyecto

- [Proyecto](https://www.tinkercad.com/things/cn31fUhwE2b)

### 📄Parcial:

[Consignas](https://github.com/magikboy/Parcial-1/blob/02b8c8bd45b8f18107d74b41cb75eaca4d41e1a5/Primer%20Parcial%20SPD%20Parte%20Practica.pdf)

### 📄Fuentes

- [Youtube](https://www.youtube.com)
- [electrontools](https://www.electrontools.com/Home/WP/display-7-segmentos/)
- [Utn](http://www.sistemas-utnfra.com.ar/#/home)
