import os
import pyautogui
import time
import keyboard

# Set display for Raspberry Pi
os.environ['DISPLAY'] = ':0'

# Enable failsafe
pyautogui.FAILSAFE = True

# Set a small pause between actions
pyautogui.PAUSE = 0.5

# Verify if we can access the display
try:
    screen_width, screen_height = pyautogui.size()
    print(f"Screen resolution: {screen_width}x{screen_height}")
except Exception as e:
    print(f"Error accessing display: {e}")
    print("Please make sure you're running this script in a graphical environment")
    exit(1)

# Esperar 10 segundos para abrir la ventana
print("Esperando 10 segundos para que abras la ventana de Recraft...")
time.sleep(10)

# Función para mover y hacer clic con delay
def download_image(x, y):
    move_and_click(x, y, 'left')    # select first image
    move_and_click(800, 600, 'right')  # right click on it
    move_and_click(853, 659, 'left') #save to...
    move_and_click(1575, 1032, 'left') #save
    move_and_click(55, 681, 'left') #close

def move_and_click(x, y, button='left'):
    if keyboard.is_pressed('esc'):
        print("ESC presionado. Finalizando script.")
        exit()
    try:
        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(1)
        pyautogui.click(button=button)
        time.sleep(1)
    except Exception as e:
        print(f"Error during mouse action: {e}")
        exit(1)

while True:
    if keyboard.is_pressed('esc'):
        print("ESC presionado. Finalizando script.")
        break
    # Primer set
    download_image(300,600)    # select first image
    download_image(900,600)
    download_image(1500,600)
    # Scroll hacia abajo
    pyautogui.scroll(-1000)
    time.sleep(1)