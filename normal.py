import random


def generate_normal_scenario():

    latency = random.uniform(10, 30)
    jitter = random.uniform(1, 5)
    bandwidth = random.uniform(80, 150)
    packet_loss = random.uniform(0, 1)

    return {
        "scenario": "Normal",
        "latency": round(latency, 2),
        "jitter": round(jitter, 2),
        "bandwidth": round(bandwidth, 2),
        "packet_loss": round(packet_loss, 2)
    }


if __name__ == "__main__":

    results = generate_normal_scenario()

    print("===== SCENARIO NORMAL =====")

    for indicator, value in results.items():
        print(indicator, ":", value)