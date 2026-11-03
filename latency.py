import random


def generate_random_latencies(number_packets=100):
    """
    Génère des valeurs aléatoires de latence pour les paquets.
    Les valeurs sont exprimées en millisecondes.
    """

    latencies = []

    for i in range(number_packets):
        latency = random.uniform(10, 150)
        latencies.append(round(latency, 2))

    return latencies


def calculate_average_latency(latencies):
    """
    Calcule la latence moyenne des paquets.
    """

    if len(latencies) == 0:
        return 0

    average = sum(latencies) / len(latencies)

    return round(average, 2)


if __name__ == "__main__":

    # Génération de 100 valeurs aléatoires
    latencies = generate_random_latencies(100)

    # Calcul de la latence moyenne
    average_latency = calculate_average_latency(latencies)

    print("===== ANALYSE DE LA LATENCE =====")
    print("Nombre de paquets :", len(latencies))
    print("Latences générées :", latencies)
    print("Latence moyenne :", average_latency, "ms")