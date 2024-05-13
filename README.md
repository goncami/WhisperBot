# Flask Messenger Bot

Este es un bot de mensajería construido con [Flask](https://flask.palletsprojects.com/en/1.1.x/), un popular marco de trabajo minimalista para Python.

## Características

- Python
- Flask
- Twilio para el manejo de mensajes
- Transcripción de audio

## Cómo usar

1. Instala las dependencias de Python con el comando `pip install -r requirements.txt`.
2. Inicia el servidor para desarrollo con el comando `python3 main.py`.

Para ejecutar la aplicación, simplemente ejecuta el script de Python en una terminal o línea de comandos con el comando:

```$ python3 main.py```


O puedes usar gunicorn:

```$ gunicorn main:app -w 2 --threads 2 -b 0.0.0.0:8003```

La aplicación comenzará a escuchar las solicitudes POST en la URL raíz. Para probar la aplicación, puedes usar una herramienta como ngrok para crear una URL pública que dirija a tu entorno de desarrollo local. Luego, puedes configurar un número de teléfono de Twilio para usar esta URL como el webhook para los mensajes entrantes.
```$ ngrok http 5000```
o
```$ ngrok http 8003```

## Advertencias

Este proyecto utiliza urllib3 versión 2, que requiere OpenSSL 1.1.1 o posterior. Si ves un error relacionado con OpenSSL o LibreSSL, considera actualizar OpenSSL/LibreSSL en tu sistema, cambiar a una distribución de Python que esté compilada con una versión compatible de OpenSSL, o degradar urllib3 a una versión que sea compatible con tu versión de OpenSSL/LibreSSL.
