import pyautogui
import time
import keyboard
# Esperar 10 segundos para abrir la ventana
print("Esperando 10 segundos para que abras la ventana de Recraft...")
time.sleep(10)
# Función para mover y hacer clic con delay
def move_and_click(x, y, button='left'):
    if keyboard.is_pressed('esc'):
        print("ESC presionado. Finalizando script.")
        exit()
    pyautogui.moveTo(x, y, duration=0.2)
    time.sleep(1)
    pyautogui.click(button=button)
    time.sleep(1)
while True:
    if keyboard.is_pressed('esc'):
        print("ESC presionado. Finalizando script.")
        break
    # Primer set
    move_and_click(500, 650, 'left')
    move_and_click(1000, 750, 'right')
    move_and_click(1109, 837, 'left')
    move_and_click(1880, 743, 'left')
    move_and_click(35, 700, 'left')
    # Segundo set
    move_and_click(1245, 650, 'left')
    move_and_click(1000, 750, 'right')
    move_and_click(1109, 837, 'left')
    move_and_click(1880, 743, 'left')
    move_and_click(35, 700, 'left')
    # Tercer set
    move_and_click(2058, 650, 'left')
    move_and_click(1000, 750, 'right')
    move_and_click(1109, 837, 'left')
    move_and_click(1880, 743, 'left')
    move_and_click(35, 700, 'left')
    # Scroll hacia abajo
    pyautogui.scroll(-1000)
    time.sleep(1)