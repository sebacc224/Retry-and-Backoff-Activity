import time
import requests

MAX_RETRIES = 5
BASE_BACKOFF = 1  # segundos

def request_with_backoff():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"Intento {attempt}...")
            response = requests.get("http://server:5000/unstable")
            if response.status_code == 200:
                print("Respuesta exitosa:", response.text)
                return
            else:
                raise Exception(f"Código de estado: {response.status_code}")
        except Exception as e:
            wait = BASE_BACKOFF * (2 ** (attempt - 1))
            print(f"Error: {e} - reintentando en {wait} segundos...")
            time.sleep(wait)
    print("Fallo tras múltiples intentos.")

if __name__ == "__main__":
    request_with_backoff()
