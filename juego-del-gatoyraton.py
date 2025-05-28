import random

class JuegoGatoRaton:
    def __init__(self):
        self.filas = 10
        self.columnas = 10
        self.num_obstaculos = 8
        self.tablero = []
        self.pos_gato = None
        self.pos_raton = None
        self.pos_queso = None
        self.turno = 0
        self.max_turnos = 50
        self.modo_juego = None
        self.jugador_personaje = None

        """Muestra el título del juego al inicio."""
        print("=" * 60)
        print("      🧠 EL LABERINTO DEL GATO Y EL RATÓN 🐭😼     ")
        print("      Un Duelo de Inteligencias en Python         ")
        print("=" * 60)
        print("\n¡Bienvenido, aprendiz de estratega!")
        print("Solo uno sobrevivirá en este laberinto de decisiones.")

    def elegir_modo_juego(self):
        """Permite elegir el modo de juego."""
        while True:
            print("\n🎮 SELECCIONA EL MODO DE JUEGO:")
            print("1. 👤 Jugador vs 🤖 Máquina")
            print("2. 👤 Jugador vs 👤 Jugador")
            print("3. 🤖 Máquina vs 🤖 Máquina (¡Duelo de IAs!)")

            eleccion = input("Elige 1, 2 o 3: ")

            if eleccion == "1":
                self.modo_juego = "jugador_vs_maquina"
                self.elegir_personaje_jugador()
                break
            elif eleccion == "2":
                self.modo_juego = "jugador_vs_jugador"
                break
            elif eleccion == "3":
                self.modo_juego = "maquina_vs_maquina"
                print("🤖 ¡Prepárate para ver una batalla épica entre dos IAs!")
                break
            else:
                print("❌ ¡Elección inválida! Por favor, ingresa '1', '2' o '3'.")

    def elegir_personaje_jugador(self):
        """Permite al jugador elegir su personaje en modo jugador vs máquina."""
        while True:
            print("\n¿Qué personaje quieres controlar?")
            print("1. Gato 😼 (Depredador: Quiere atrapar al Ratón)")
            print("2. Ratón 🐭 (Presa: Quiere escapar y llegar al queso)")

            eleccion = input("Elige 1 o 2: ")

            if eleccion == "1":
                self.jugador_personaje = "Gato"
                print("🐱 Elegiste el Gato. ¡A cazar!")
                break
            elif eleccion == "2":
                self.jugador_personaje = "Raton"
                print("🐭 Elegiste el Ratón. ¡A escapar!")
                break
            else:
                print("❌ ¡Elección inválida! Por favor, ingresa '1' o '2'.")

    def generar_laberinto(self):
        """Genera un laberinto aleatorio con obstáculos y distancias mínimas justas."""
        # Definir distancias mínimas para una batalla justa
        DISTANCIA_MIN_GATO_RATON = 6  # El gato no debe estar muy cerca del ratón
        DISTANCIA_MIN_GATO_QUESO = 4  # El gato no debe estar muy cerca del queso
        DISTANCIA_MIN_RATON_QUESO = 6  # El ratón debe tener una ventaja mínima
        MAX_INTENTOS = 1000  # Evitar bucles infinitos
        
        # Crear matriz vacía
        self.tablero = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]

        # Colocar obstáculos
        obstaculos_colocados = 0
        while obstaculos_colocados < self.num_obstaculos:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = "X"
                obstaculos_colocados += 1

        # Colocar queso primero (posición base)
        intentos = 0
        while intentos < MAX_INTENTOS:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = "Q"
                self.pos_queso = (fila, columna)
                break
            intentos += 1

        # Colocar ratón con distancia adecuada al queso
        intentos = 0
        while intentos < MAX_INTENTOS:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] == 0:
                pos_temporal = (fila, columna)
                distancia_queso = self.calcular_distancia(pos_temporal, self.pos_queso)
                
                # El ratón debe estar a una distancia razonable del queso
                if DISTANCIA_MIN_RATON_QUESO <= distancia_queso <= DISTANCIA_MIN_RATON_QUESO + 3:
                    self.tablero[fila][columna] = "R"
                    self.pos_raton = pos_temporal
                    break
            intentos += 1
        
        # Si no se pudo colocar el ratón con distancia ideal, colocar en cualquier lugar libre
        if intentos >= MAX_INTENTOS:
            while True:
                fila = random.randint(0, self.filas - 1)
                columna = random.randint(0, self.columnas - 1)
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = "R"
                    self.pos_raton = (fila, columna)
                    break

        # Colocar gato respetando distancias mínimas
        intentos = 0
        while intentos < MAX_INTENTOS:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] == 0:
                pos_temporal = (fila, columna)
                distancia_raton = self.calcular_distancia(pos_temporal, self.pos_raton)
                distancia_queso = self.calcular_distancia(pos_temporal, self.pos_queso)
                
                # Verificar que las distancias sean adecuadas para una batalla justa
                if (distancia_raton >= DISTANCIA_MIN_GATO_RATON and 
                    distancia_queso >= DISTANCIA_MIN_GATO_QUESO):
                    self.tablero[fila][columna] = "G"
                    self.pos_gato = pos_temporal
                    break
            intentos += 1
        
        # Si no se pudo colocar el gato con distancias ideales, colocar en cualquier lugar libre
        if intentos >= MAX_INTENTOS:
            while True:
                fila = random.randint(0, self.filas - 1)
                columna = random.randint(0, self.columnas - 1)
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = "G"
                    self.pos_gato = (fila, columna)
                    break

    def verificar_balance_juego(self):
        """Verifica si el juego tiene un balance justo basado en las distancias."""
        dist_gato_raton = self.calcular_distancia(self.pos_gato, self.pos_raton)
        dist_gato_queso = self.calcular_distancia(self.pos_gato, self.pos_queso)
        dist_raton_queso = self.calcular_distancia(self.pos_raton, self.pos_queso)
        
        # El ratón debe tener ventaja para llegar al queso
        raton_tiene_ventaja = dist_raton_queso < dist_gato_queso
        
        # El gato no debe estar demasiado cerca del ratón inicialmente
        gato_no_muy_cerca = dist_gato_raton >= 4
        
        # El juego es balanceado si se cumplen las condiciones
        es_balanceado = raton_tiene_ventaja and gato_no_muy_cerca
        
        return {
            'balanceado': es_balanceado,
            'raton_ventaja': raton_tiene_ventaja,
            'gato_distancia_ok': gato_no_muy_cerca,
            'distancias': {
                'gato_raton': dist_gato_raton,
                'gato_queso': dist_gato_queso,
                'raton_queso': dist_raton_queso
            }
        }

    def imprimir_tablero(self, mensaje=""):
        """Imprime el tablero con decoración."""
        print("\n" + "╔" + "═" * (self.columnas * 3) + "╗")

        for fila in self.tablero:
            linea = "║"
            for celda in fila:
                if celda == 0:
                    linea += " 🌿"
                elif celda == "G":
                    linea += " 🐱"
                elif celda == "R":
                    linea += " 🐭"
                elif celda == "Q":
                    linea += " 🧀"
                elif celda == "X":
                    linea += " 🧱"
            linea += " ║"
            print(linea)

        print("╚" + "═" * (self.columnas * 3) + "╝")
        print(f"\n🎲 Turno {self.turno} | {mensaje}")

    def es_posicion_valida(self, fila, columna):
        """Verifica si una posición está dentro del tablero."""
        return 0 <= fila < self.filas and 0 <= columna < self.columnas

    def obtener_movimientos_posibles(self, fila, columna):
        """Obtiene todos los movimientos posibles desde una posición (solo 4 direcciones)."""
        movimientos = []
        # Solo movimientos ortogonales: arriba, abajo, izquierda, derecha
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for df, dc in direcciones:
            nueva_fila = fila + df
            nueva_columna = columna + dc

            if (
                self.es_posicion_valida(nueva_fila, nueva_columna)
                and self.tablero[nueva_fila][nueva_columna] != "X"
            ):
                movimientos.append((nueva_fila, nueva_columna))

        return movimientos

    def calcular_distancia(self, pos1, pos2):
        """Calcula la distancia Manhattan entre dos posiciones."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def evaluar_posicion_gato(self):
        """Evalúa qué tan buena es la posición actual para el gato."""
        distancia_a_raton = self.calcular_distancia(self.pos_gato, self.pos_raton)

        # El gato quiere estar cerca del ratón
        puntuacion = 100 - distancia_a_raton * 10

        # Bonificación si está muy cerca
        if distancia_a_raton <= 1:
            puntuacion += 50

        return puntuacion

    def evaluar_posicion_raton(self):
        """Evalúa qué tan buena es la posición actual para el ratón."""
        distancia_a_gato = self.calcular_distancia(self.pos_raton, self.pos_gato)
        distancia_a_queso = self.calcular_distancia(self.pos_raton, self.pos_queso)

        # El ratón quiere estar lejos del gato y cerca del queso
        puntuacion = distancia_a_gato * 15 - distancia_a_queso * 20

        # Bonificación por estar cerca del queso
        if distancia_a_queso <= 1:
            puntuacion += 100

        # Penalización por estar cerca del gato
        if distancia_a_gato <= 2:
            puntuacion -= 50

        return puntuacion

    def minimax_gato(self, profundidad, es_maximizando):
        """Algoritmo Minimax para el gato."""
        if profundidad == 0 or self.pos_gato == self.pos_raton:
            return self.evaluar_posicion_gato(), None

        movimientos = self.obtener_movimientos_posibles(
            self.pos_gato[0], self.pos_gato[1]
        )

        if not movimientos:
            return self.evaluar_posicion_gato(), None

        mejor_movimiento = None

        if es_maximizando:
            mejor_valor = float("-inf")
            for movimiento in movimientos:
                # Simular movimiento
                pos_original = self.pos_gato
                self.pos_gato = movimiento
        
                valor, _ = self.minimax_gato(profundidad - 1, False)

                # Deshacer movimiento
                self.pos_gato = pos_original

                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = movimiento

            return mejor_valor, mejor_movimiento
        else:
            peor_valor = float("inf")
            for movimiento in movimientos:
                # Simular movimiento del ratón (oponente)
                pos_original = self.pos_raton
                movimientos_raton = self.obtener_movimientos_posibles(
                    self.pos_raton[0], self.pos_raton[1]
                )

                if movimientos_raton:
                    # El ratón elige su mejor movimiento
                    for mov_raton in movimientos_raton:
                        self.pos_raton = mov_raton
                        valor, _ = self.minimax_gato(profundidad - 1, True)
                        peor_valor = min(peor_valor, valor)

                # Deshacer movimiento
                self.pos_raton = pos_original

            return peor_valor, mejor_movimiento

    def minimax_raton(self, profundidad, es_maximizando):
        """Algoritmo Minimax para el ratón."""
        if (
            profundidad == 0
            or self.pos_raton == self.pos_queso
            or self.pos_gato == self.pos_raton
        ):
            return self.evaluar_posicion_raton(), None

        movimientos = self.obtener_movimientos_posibles(
            self.pos_raton[0], self.pos_raton[1]
        )

        if not movimientos:
            return self.evaluar_posicion_raton(), None

        mejor_movimiento = None

        if es_maximizando:
            mejor_valor = float("-inf")
            for movimiento in movimientos:
                # Simular movimiento
                pos_original = self.pos_raton
                self.pos_raton = movimiento

                valor, _ = self.minimax_raton(profundidad - 1, False)

                # Deshacer movimiento
                self.pos_raton = pos_original

                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = movimiento

            return mejor_valor, mejor_movimiento
        else:
            peor_valor = float("inf")
            for movimiento in movimientos:
                # Simular movimiento del gato (oponente)
                pos_original = self.pos_gato
                movimientos_gato = self.obtener_movimientos_posibles(
                    self.pos_gato[0], self.pos_gato[1]
                )

                if movimientos_gato:
                    for mov_gato in movimientos_gato:
                        self.pos_gato = mov_gato
                        valor, _ = self.minimax_raton(profundidad - 1, True)
                        peor_valor = min(peor_valor, valor)

                # Deshacer movimiento
                self.pos_gato = pos_original

            return peor_valor, mejor_movimiento

    def mover_gato_ia(self):
        """Mueve el gato usando."""
        print("🤖 El Gato está pensando...")

        _, mejor_movimiento = self.minimax_gato(profundidad=6, es_maximizando=True)

        if mejor_movimiento:
            # Borra la posición anterior
            self.tablero[self.pos_gato[0]][self.pos_gato[1]] = 0

            # Verificar si hay queso en la nueva posición
            if self.tablero[mejor_movimiento[0]][mejor_movimiento[1]] == "Q":
                self.tablero[mejor_movimiento[0]][mejor_movimiento[1]] = "G"
                # Recolocar el queso en una posición aleatoria
                self.recolocar_queso()
            else:
                self.tablero[mejor_movimiento[0]][mejor_movimiento[1]] = "G"

            self.pos_gato = mejor_movimiento
            print(f"🐱 Gato se mueve a {mejor_movimiento}")
        else:
            print("🐱 El Gato no puede moverse")

    def mover_raton_ia(self):
        """Mueve el ratón usando."""
        print("🤖 El Ratón está pensando...")

        _, mejor_movimiento = self.minimax_raton(profundidad=6, es_maximizando=True)

        if mejor_movimiento:
            # Limpiar posición anterior
            self.tablero[self.pos_raton[0]][self.pos_raton[1]] = 0
            self.tablero[mejor_movimiento[0]][mejor_movimiento[1]] = "R"
            self.pos_raton = mejor_movimiento
            print(f"🐭 Ratón se mueve a {mejor_movimiento}")
        else:
            print("🐭 El Ratón no puede moverse")

    def recolocar_queso(self):
        """Recoloca el queso en una nueva posición aleatoria."""
        while True:
            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)
            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = "Q"
                self.pos_queso = (fila, columna)
                break

    def mover_jugador(self, personaje):
        """Permite al jugador hacer un movimiento con las flechas del teclado."""
        print(f"\n🎮 Tu turno ({personaje}):")

        if personaje == "Gato":
            pos_actual = self.pos_gato
            simbolo = "🐱"
        else:
            pos_actual = self.pos_raton
            simbolo = "🐭"

        print("Usa las siguientes teclas para moverte:")
        print("W/w = Arriba")
        print("S/s = Abajo")
        print("A/a = Izquierda")
        print("D/d = Derecha")

        while True:
            movimiento = input("Ingresa tu movimiento (W/A/S/D): ").lower()

            nueva_fila = pos_actual[0]
            nueva_columna = pos_actual[1]

            # Mapear teclas a movimientos (solo 4 direcciones)
            if movimiento == "w":  # Arriba
                nueva_fila -= 1
            elif movimiento == "s":  # Abajo
                nueva_fila += 1
            elif movimiento == "a":  # Izquierda
                nueva_columna -= 1
            elif movimiento == "d":  # Derecha
                nueva_columna += 1
            else:
                print("❌ Tecla inválida. Usa solo W/A/S/D")
                continue

            # Verificar si el movimiento es válido
            if (
                self.es_posicion_valida(nueva_fila, nueva_columna)
                and self.tablero[nueva_fila][nueva_columna] != "X"
            ):
                nuevo_mov = (nueva_fila, nueva_columna)
                break
            else:
                print(
                    "❌ Movimiento inválido. Hay un obstáculo o estás fuera del tablero."
                )

        # Realizar el movimiento
        if personaje == "Gato":
            self.tablero[self.pos_gato[0]][self.pos_gato[1]] = 0
            if self.tablero[nuevo_mov[0]][nuevo_mov[1]] == "Q":
                self.tablero[nuevo_mov[0]][nuevo_mov[1]] = "G"
                self.recolocar_queso()
            else:
                self.tablero[nuevo_mov[0]][nuevo_mov[1]] = "G"
            self.pos_gato = nuevo_mov
        else:
            self.tablero[self.pos_raton[0]][self.pos_raton[1]] = 0
            self.tablero[nuevo_mov[0]][nuevo_mov[1]] = "R"
            self.pos_raton = nuevo_mov

        print(f"{simbolo} Te mueves a {nuevo_mov}")

    def verificar_fin_juego(self):
        """Verifica si el juego ha terminado."""
        if self.pos_gato == self.pos_raton:
            return "gato"
        elif self.pos_raton == self.pos_queso:
            return "raton"
        elif self.turno >= self.max_turnos:
            return "empate"
        return None

    def jugar(self):
        """Función principal del juego."""

        self.elegir_modo_juego()
        self.generar_laberinto()

        print("\n🎮 ¡COMIENZA EL JUEGO!")
        self.imprimir_tablero("¡La batalla ha comenzado!")

        while True:
            self.turno += 1

            # Turno del Gato
            if (
                self.modo_juego == "jugador_vs_maquina"
                and self.jugador_personaje == "Gato"
            ):
                self.mover_jugador("Gato")
            elif self.modo_juego == "jugador_vs_jugador":
                self.mover_jugador("Gato")
            else:
                self.mover_gato_ia()

            resultado = self.verificar_fin_juego()
            if resultado:
                break

            self.imprimir_tablero("Después del movimiento del Gato")

            # Turno del Ratón
            if (
                self.modo_juego == "jugador_vs_maquina"
                and self.jugador_personaje == "Raton"
            ):
                self.mover_jugador("Raton")
            elif self.modo_juego == "jugador_vs_jugador":
                self.mover_jugador("Raton")
            else:
                self.mover_raton_ia()

            resultado = self.verificar_fin_juego()
            if resultado:
                break

            self.imprimir_tablero("Después del movimiento del Ratón")

            if self.modo_juego == "maquina_vs_maquina":
                input("Presiona Enter para continuar...")  # Pausa para ver la batalla

        # Mostrar resultado final
        self.imprimir_tablero("¡JUEGO TERMINADO!")

        if resultado == "gato":
            print("🏆 ¡EL GATO GANA! Ha atrapado al ratón.")
        elif resultado == "raton":
            print("🏆 ¡EL RATÓN GANA! Ha llegado al queso.")
        else:
            print("🤝 ¡EMPATE! Se acabó el tiempo.")

        print("\n" + "=" * 60)
        print("           🎮 FIN DEL JUEGO 🎮          ")
        print("=" * 60)
        print("¡Gracias por jugar!")


# Ejecutar el juego
juego = JuegoGatoRaton()
juego.jugar()

