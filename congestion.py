import random


def generate_congestion_scenario():

    latency = random.uniform(100, 200)
    jitter = random.uniform(25, 60)
    bandwidth = random.uniform(5, 30)
    packet_loss = random.uniform(5, 15)

    return {
        "scenario": "Congestion",
        "latency": round(latency, 2),
        "jitter": round(jitter, 2),
        "bandwidth": round(bandwidth, 2),
        "packet_loss": round(packet_loss, 2)
    }


if __name__ == "__main__":

    results = generate_congestion_scenario()

    print("===== SCENARIO CONGESTIONNE =====")

    for indicator, value in results.items():
        print(indicator, ":", value)