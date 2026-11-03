import random


def generate_random_bandwidth():
    """
    Génère des valeurs aléatoires pour simuler
    la taille des données et la durée de transmission.
    """

    data_size_mb = random.uniform(10, 100)
    duration_seconds = random.uniform(1, 10)

    return round(data_size_mb, 2), round(duration_seconds, 2)


def calculate_bandwidth(data_size_mb, duration_seconds):
    """
    Calcule le débit en Mbps.
    """

    if duration_seconds <= 0:
        return 0

    data_size_bits = data_size_mb * 8 * 1_000_000

    bandwidth = data_size_bits / duration_seconds / 1_000_000

    return round(bandwidth, 2)


if __name__ == "__main__":

    data_size, duration = generate_random_bandwidth()

    bandwidth = calculate_bandwidth(data_size, duration)

    print("===== ANALYSE DU DEBIT =====")
    print("Taille des données :", data_size, "MB")
    print("Durée de transmission :", duration, "secondes")
    print("Débit :", bandwidth, "Mbps")