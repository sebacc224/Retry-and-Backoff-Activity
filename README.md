# Retry-and-Backoff-Activity

Cada grupo deberá:
1. Investigar el patrón o arquitectura asignada, documentar sus características
principales, ventajas, desventajas y casos de uso reales.
2. Implementar un demo funcional basado en su investigación utilizando Docker y/o
Docker Compose.
3. Subir la implementación técnica a un repositorio de GitHub, documentando
claramente los pasos necesarios para ejecutar el demo.
4. Preparar y realizar una sustentación grupal explicando tanto los conceptos teóricos
como el demo técnico.

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
