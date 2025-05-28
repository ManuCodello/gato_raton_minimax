# 🧠 El Laberinto del Gato y el Ratón 🐭😼

**Un duelo de inteligencias en Python donde solo uno sobrevivirá.**

---

## Descripción

Este es un juego estratégico tipo laberinto donde un **Gato** (depredador) intenta atrapar a un **Ratón** (presa) que busca llegar al queso 🧀 para ganar. El tablero es una matriz 10x10 con obstáculos, y el juego puede jugarse en distintos modos: jugador vs máquina, jugador vs jugador o máquina vs máquina (¡batalla épica de IA!).

El juego usa el algoritmo **Minimax** para la IA, con evaluaciones heurísticas para decidir los mejores movimientos, simulando una batalla táctica entre cazador y presa.

---

## Características Principales

- Tablero 10x10 con obstáculos colocados aleatoriamente.
- Distancias iniciales balanceadas para asegurar juego justo.
- Modos de juego:
  - Jugador vs Máquina
  - Jugador vs Jugador
  - Máquina vs Máquina
- Elección de personaje: Gato o Ratón (cuando hay jugador humano).
- IA basada en algoritmo Minimax con profundidad ajustable.
- Decoración visual del tablero con emojis para fácil lectura.
- Control de turnos y límite máximo para evitar partidas infinitas.
- Evaluaciones heurísticas para decisiones inteligentes del gato y ratón.

---

## Cómo jugar

1. Ejecuta el script en un entorno Python 3.
2. Elige el modo de juego:
   - `1` para Jugador vs Máquina
   - `2` para Jugador vs Jugador
   - `3` para Máquina vs Máquina
3. Si juegas contra la máquina, elige tu personaje: Gato o Ratón.
4. El tablero se genera aleatoriamente con obstáculos, gato, ratón y queso.
5. El juego avanza por turnos hasta que el gato atrape al ratón o el ratón llegue al queso, o se llegue al límite de turnos.

---

## Requisitos

- Python 3.x
- No requiere librerías externas.

---

## Estructura del código

- **Clase `JuegoGatoRaton`**: controla toda la lógica del juego.
- Métodos para:
  - Generar el laberinto y ubicar elementos con balance de distancias.
  - Imprimir el tablero con emojis.
  - Validar movimientos y calcular distancias Manhattan.
  - Evaluar posiciones para el gato y el ratón (funciones heurísticas).
  - Ejecutar Minimax para decisiones de IA.
  - Control de turnos y reglas de victoria.

---

## ¿Por qué este juego?

Porque la programación no es solo escribir líneas, sino pensar estrategias y anticipar movimientos. Aquí entrenas la mente para resolver problemas y aplicar algoritmos clásicos de IA, con un toque divertido y visual.

---

## Para contribuir

Este proyecto es un gran playground para estudiantes de programación e IA. Puedes contribuir:

- Mejorando la IA con poda alfa-beta.
- Añadiendo modos de dificultad.
- Optimizando la generación del laberinto.
- Mejorando la interfaz de usuario (por ejemplo, con GUI).

---

## Contacto

Si quieres compartir ideas, dudas o mejoras, ¡aquí estoy! Vamos a romperla con código, sin excusas ni vueltas.

---

**¡Prepárate para atrapar o escapar!**

---

*Código original y mantenido por: Manu, aprendiz y guerrero del código.*



