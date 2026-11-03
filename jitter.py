import random


def generate_random_latencies(number_packets=100):
    """
    Génère des valeurs aléatoires de latence.
    """

    latencies = []

    for i in range(number_packets):
        latency = random.uniform(10, 150)
        latencies.append(round(latency, 2))

    return latencies


def calculate_jitter(latencies):
    """
    Calcule la gigue moyenne entre les paquets successifs.
    """

    if len(latencies) < 2:
        return 0

    variations = []

    for i in range(1, len(latencies)):
        difference = abs(latencies[i] - latencies[i - 1])
        variations.append(difference)

    average_jitter = sum(variations) / len(variations)

    return round(average_jitter, 2)


if __name__ == "__main__":

    latencies = generate_random_latencies(100)

    jitter = calculate_jitter(latencies)

    print("===== ANALYSE DE LA GIGUE =====")
    print("Nombre de paquets :", len(latencies))
    print("Gigue moyenne :", jitter, "ms")