# Tic-Tac-Toe

## Descripción

Este proyecto es una implementación del juego clásico de Tic-Tac-Toe (Tres en Línea) en Python. Utiliza la biblioteca `tkinter` para crear una interfaz gráfica de usuario (GUI) y proporciona funcionalidades para jugar contra otro jugador en un tablero de 3x3. Además, el proyecto incluye un análisis avanzado que evalúa las posibles jugadas y determina las mejores estrategias utilizando un algoritmo de búsqueda.

### Funcionalidades

- **Interfaz Gráfica**: Una ventana con un tablero de 3x3 donde los jugadores pueden hacer clic en los botones para colocar "X" o "O".
- **Detección de Ganador**: El juego detecta automáticamente cuando un jugador gana o cuando hay un empate.
- **Evaluación de Jugadas**: Incluye un análisis exhaustivo de posibles movimientos futuros, evaluando cada jugada en términos de puntos y mostrando la solución.
- **Puntuación**: El sistema utiliza un esquema de puntuación para evaluar el impacto de cada jugada, tanto presente como futura.

### Esquema de Puntuación

- **WIN_SCORE**: 10 puntos - El jugador gana en la jugada actual.
- **FUTURE_WIN_SCORE**: 5 puntos - El jugador ganaría en una jugada futura.
- **NEUTRAL_SCORE**: 0 puntos - La jugada no cambia el estado del juego.
- **FUTURE_LOSE_SCORE**: -5 puntos - El jugador perdería en una jugada futura.
- **LOSE_SCORE**: -10 puntos - El jugador pierde en la jugada actual.

### Funcionalidades del Código

1. **Chequeo de Victoria**: La función `check_win` verifica si un jugador ha ganado el juego al completar una fila, columna o diagonal.
2. **Generación de Árbol de Jugadas**: La función `generate_tree` crea un árbol de posibles movimientos futuros y evalúa cada uno.
3. **Evaluación de Movimientos**: La función `evaluate_move` calcula una puntuación para cada movimiento basado en el estado actual y futuro del tablero.
4. **Impresión del Tablero**: La función `print_board` muestra el tablero en la consola con "X" y "O".
5. **Evaluación y Visualización**: La función `evaluate_and_print` muestra las posibles jugadas y sus resultados futuros.
6. **Interfaz Gráfica**: La clase `TicTacToeGUI` proporciona la interfaz gráfica y maneja la lógica del juego, incluyendo el cambio de jugadores, detección de ganadores y reinicio del juego.

## Instalación

Este proyecto requiere Python 3.x. Asegúrate de tener `tkinter` instalado, que generalmente se incluye con la instalación estándar de Python.

## Ejecución

Para ejecutar el juego, utiliza el siguiente comando en tu terminal:

python tic_tac_toe.py

# Sustentacion Taller TicTac
https://youtu.be/RG6DxBBzkJ4?si=KW2i_Pk9_lVdsSRq
