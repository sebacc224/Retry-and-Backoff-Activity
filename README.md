# Arquitectura Asignada: Retry with Backoff

El patrón **Retry with Backoff** mejora la estabilidad de una aplicación al reintentar automáticamente operaciones que fallan por errores transitorios, como problemas de red, servicios temporalmente no disponibles o sobrecarga del sistema.

---

## Motivación

En arquitecturas distribuidas, los errores transitorios son comunes debido a:

- Pérdida momentánea de conectividad  
- Saturación del servicio (throttling)  
- Caídas o reinicios breves de servicios  

El uso de reintentos controlados, junto con tiempos de espera crecientes (*backoff*), mejora la resiliencia y la experiencia del usuario, evitando sobrecargar los servicios con múltiples reintentos simultáneos.

---

## Características Principales

- Automatiza reintentos: opera sin intervención humana.  
- Control del tiempo de espera: puede ser fijo, exponencial o con jitter.  
- Evita fallos en cascada: reduce la presión sobre servicios fallidos.  
- Configuración de límites: permite definir un número máximo de intentos y un tiempo total de espera.  
- Flexible por tipo de error: se adapta a condiciones o códigos de error específicos.

---

## Aplicabilidad

Este patrón es útil cuando:

- El servicio devuelve HTTP 429 (Too Many Requests) u otros errores por sobrecarga.  
- Hay problemas de red temporales.  
- El servicio está inactivo de manera transitoria y los reintentos sin control podrían empeorar la situación.

---

## Problemas y Consideraciones

### Idempotencia

Las operaciones deben ser idempotentes: múltiples ejecuciones no deben modificar el estado del sistema de forma inesperada.

### Ancho de Banda

Demasiados reintentos simultáneos pueden saturar la red y degradar el rendimiento.  
Se recomienda usar *backoff* exponencial con jitter para distribuir mejor la carga.

### Escenarios de "Fail Fast"

Si se detecta un error no transitorio, es más eficiente fallar rápidamente.  
En estos casos, es preferible aplicar el patrón **Circuit Breaker**.

### Tiempos de Espera

El uso de backoff exponencial puede aumentar la latencia de respuesta.  
Es importante encontrar un equilibrio entre resiliencia y experiencia de usuario.

---

## Ventajas

- Mejora la resiliencia frente a errores temporales.  
- Reduce la necesidad de intervención manual.  
- Ayuda a estabilizar el sistema tras fallos.  
- Es fácil de implementar en la mayoría de lenguajes y frameworks.  
- Compatible con otros patrones como Circuit Breaker y Timeout.

---

## Desventajas

- Puede ocultar errores graves si se aplica sin criterios claros.  
- Un mal uso puede generar tormentas de reintentos.  
- Aumenta la latencia en operaciones fallidas.  
- Si no se limita correctamente, puede sobrecargar los recursos del sistema.

# **PASOS A SEGUIR PARA LA INSTALACION DEL DEMO**

# Demo de Retry with Backoff con Docker y Flask

Este repositorio contiene un demo funcional del patrón **Retry with Backoff** implementado con **Docker** y **Flask**. El propósito de esta demostración es simular un servicio que falla aleatoriamente con un código de error 503 (Servicio Temporalmente No Disponible) y reintentar con una política de backoff exponencial.

## Requisitos previos

Antes de ejecutar este demo, necesitas tener instalado lo siguiente:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Estructura del proyecto

Este repositorio tiene la siguiente estructura:

```
.
├── client/
│   └── Dockerfile
│   └── app.py
├── docker-compose.yml
├── server/
│   └── Dockerfile
│   └── requirements.txt
│   └── server.py
└── README.md
```

### `client/`
Contiene el código del cliente que realiza peticiones al servidor Flask.

### `server/`
Contiene el servidor Flask que maneja las solicitudes y responde con un error aleatorio (503) o una respuesta exitosa.

### `docker-compose.yml`
Archivo de configuración para orquestar los contenedores de Docker.

## Pasos para ejecutar el demo

### 1. Clona el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/sebacc224/Retry-and-Backoff-Activity.git
cd Retry-and-Backoff-Activity
```

### 2. Construye los contenedores Docker

Usa Docker Compose para construir los contenedores definidos en el archivo `docker-compose.yml`:

```bash
docker-compose build
```

### 3. Levanta los contenedores

Inicia los contenedores de Docker con el siguiente comando:

```bash
docker-compose up
```

Esto iniciará tanto el servidor Flask como el cliente. El servidor Flask estará escuchando en el puerto `5000` y el cliente realizará solicitudes a dicho servidor.

### 4. Realiza una petición al servidor

Una vez que los contenedores estén en ejecución, abre tu navegador y navega a:

```
http://localhost:5000/process
```

El servidor procesará la solicitud y, debido a la implementación del patrón Retry with Backoff, el cliente intentará automáticamente volver a realizar la solicitud si recibe un error 503 (Servicio Temporalmente No Disponible).

### 5. Detener los contenedores

Para detener los contenedores, puedes usar el siguiente comando:

```bash
docker-compose down
```

Esto detendrá y eliminará los contenedores, redes y volúmenes creados por Docker Compose.

## Explicación del código

### `server/server.py`

Este archivo contiene un servidor Flask que simula un servicio que falla aleatoriamente con un código de error 503 o responde con un mensaje de éxito. Este comportamiento simula un servicio que no está disponible temporalmente, lo que es útil para probar el patrón Retry with Backoff.

### `client/app.py`

El cliente hace peticiones al servidor Flask y, si el servidor responde con un error 503, reintenta la solicitud siguiendo una política de backoff exponencial.

### `docker-compose.yml`

Este archivo orquesta los contenedores de Docker. Incluye el contenedor para el servidor Flask (`server`) y el cliente (`client`), así como la configuración para la red y los puertos.
