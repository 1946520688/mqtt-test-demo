import json
import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "demo/iot/device/status"

def main():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)

    payload = {
        "device_id": "robot_01",
        "status": "online",
        "battery": 85,
        "timestamp": int(time.time())
    }

    message = json.dumps(payload, ensure_ascii=False)
    client.publish(TOPIC, message)
    client.disconnect()

if __name__ == "__main__":
    main()
