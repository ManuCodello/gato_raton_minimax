# gato_raton_minimax
🧠 El Laberinto del Gato y el Ratón 🐭😼
¡Bienvenido a El Laberinto del Gato y el Ratón!
Un juego estratégico donde la astucia, la inteligencia artificial y la supervivencia se cruzan en un tablero de 10x10. Programado en Python.

🎮 Modos de Juego
👤 Jugador vs 🤖 Máquina: Elegí ser el gato (cazador) o el ratón (escapista) y enfrentate a una IA despiadada.

👤 Jugador vs 👤 Jugador: Dos mentes humanas se enfrentan. ¿Quién dominará el tablero?

🤖 Máquina vs 🤖 Máquina: Observá cómo dos inteligencias artificiales se enfrentan en una batalla táctica.

🧩 Reglas del Juego
El ratón (🐭) debe alcanzar el queso (🧀) para ganar.

El gato (😼) debe atrapar al ratón para ganar.

El tablero tiene obstáculos aleatorios (🧱), por lo que cada partida es única.

Las posiciones iniciales son colocadas con distancias mínimas controladas para garantizar una partida justa.

La partida tiene un límite de 50 turnos.

🤖 Inteligencia Artificial
El Gato y el Ratón pueden ser controlados por IA con heurísticas y algoritmo Minimax, que evalúan la mejor posición en función de distancias y puntuaciones.

Evaluaciones incluyen:

Proximidad al objetivo (queso o presa).

Penalizaciones por estar cerca del enemigo.

Bonificaciones por estar cerca del objetivo.

📦 Estructura del Proyecto
bash
Copiar
Editar
gato_raton/
│
├── juego_gato_raton.py     # Lógica principal del juego
├── README.md               # Este archivo
🚀 ¿Cómo Ejecutarlo?
Asegurate de tener Python 3 instalado.

Cloná el repositorio:

bash
Copiar
Editar
git clone https://github.com/tuusuario/gato-raton-juego.git
cd gato-raton-juego
Ejecutá el juego:

bash
Copiar
Editar
python juego_gato_raton.py
¡Elegí el modo de juego y empezá la batalla de cerebros!

📷 Ejemplo Visual del Tablero
matlab
Copiar
Editar
╔════════════════════════════════════════════════════╗
║ 🌿 🌿 🌿 🧀 🌿 🧱 🌿 🌿 🌿 🌿 ║
║ 🌿 🌿 🧱 🌿 🌿 🌿 🌿 🧱 🌿 🌿 ║
║ 🌿 🐭 🌿 🌿 🌿 🧱 🌿 🌿 🐱 🌿 ║
║ 🌿 🌿 🌿 🌿 🌿 🌿 🌿 🌿 🌿 🌿 ║
║ ...                                               ║
╚════════════════════════════════════════════════════╝
🎲 Turno 3 | ¡El ratón se acerca al queso!
⚙️ Funciones Clave
generar_laberinto(): Genera el mapa con obstáculos y coloca estratégicamente al gato, ratón y queso.

verificar_balance_juego(): Asegura que la partida sea justa.

minimax_gato(): Calcula el mejor movimiento del gato simulando escenarios futuros.

evaluar_posicion_*(): Evalúa la calidad de una posición según distancias y contexto.

🛠 Posibles Mejoras Futuras
GUI con pygame o tkinter.

Sistema de puntajes y estadísticas.

Dificultades ajustables para las IAs.

Más personajes y poderes especiales.

💡 Filosofía del Juego
Este proyecto fue diseñado para aprender y aplicar:

Programación orientada a objetos

Algoritmos de inteligencia artificial (Minimax)

Lógica de tableros

Diseño de sistemas balanceados

¡Si te gustó el juego, dejá una estrella y compartilo! ⭐

Hecho con pasión por el aprendizaje y la programación.
Manu 👨‍💻
