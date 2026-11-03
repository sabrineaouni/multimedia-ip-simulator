import random


def generate_loaded_scenario():

    latency = random.uniform(40, 80)
    jitter = random.uniform(5, 20)
    bandwidth = random.uniform(40, 80)
    packet_loss = random.uniform(1, 5)

    return {
        "scenario": "Loaded",
        "latency": round(latency, 2),
        "jitter": round(jitter, 2),
        "bandwidth": round(bandwidth, 2),
        "packet_loss": round(packet_loss, 2)
    }


if __name__ == "__main__":

    results = generate_loaded_scenario()

    print("===== SCENARIO CHARGE =====")

    for indicator, value in results.items():
        print(indicator, ":", value)