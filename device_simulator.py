import json
import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "demo/iot/device/robot_01"

def build_payload(status, battery, location):
    return {
        "device_id": "robot_01",
        "device_type": "sweeping_robot",
        "status": status,
        "battery": battery,
        "location": location,
        "timestamp": int(time.time())
    }

def main():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)

    scenario = [
        build_payload("online", 100, "dock"),
        build_payload("cleaning", 92, "living_room"),
        build_payload("cleaning", 86, "bedroom"),
        build_payload("returning_to_charge", 25, "hallway"),
        build_payload("charging", 24, "dock")
    ]

    for payload in scenario:
        message = json.dumps(payload, ensure_ascii=False)
        print(message)
        client.publish(TOPIC, message)
        time.sleep(2)

    client.disconnect()

if __name__ == "__main__":
    main()
