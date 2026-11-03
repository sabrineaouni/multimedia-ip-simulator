import random


def simulate_without_qos():

    return {
        "voice": {
            "latency": round(random.uniform(80, 150), 2),
            "packet_loss": round(random.uniform(3, 10), 2)
        },
        "video": {
            "latency": round(random.uniform(70, 140), 2),
            "packet_loss": round(random.uniform(2, 8), 2)
        },
        "data": {
            "latency": round(random.uniform(50, 120), 2),
            "packet_loss": round(random.uniform(1, 6), 2)
        }
    }


def simulate_with_qos():

    return {
        "voice": {
            "latency": round(random.uniform(10, 30), 2),
            "packet_loss": round(random.uniform(0, 1), 2)
        },
        "video": {
            "latency": round(random.uniform(30, 60), 2),
            "packet_loss": round(random.uniform(1, 3), 2)
        },
        "data": {
            "latency": round(random.uniform(60, 100), 2),
            "packet_loss": round(random.uniform(2, 5), 2)
        }
    }


def calculate_improvement(before, after):

    if before == 0:
        return 0

    improvement = ((before - after) / before) * 100

    return round(improvement, 2)


def compare_qos():

    without_qos = simulate_without_qos()
    with_qos = simulate_with_qos()

    print("\n========== COMPARAISON QoS ==========")

    for traffic in ["voice", "video", "data"]:

        print("\nTrafic :", traffic.upper())

        for metric in ["latency", "packet_loss"]:

            before = without_qos[traffic][metric]
            after = with_qos[traffic][metric]

            improvement = calculate_improvement(before, after)

            unit = "ms" if metric == "latency" else "%"

            print(f"{metric} sans QoS : {before} {unit}")
            print(f"{metric} avec QoS : {after} {unit}")
            print(f"Amélioration : {improvement} %")


if __name__ == "__main__":
    compare_qos()