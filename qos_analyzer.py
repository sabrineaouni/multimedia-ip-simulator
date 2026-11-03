from backend.qos.latency import (
    generate_random_latencies,
    calculate_average_latency
)

from backend.qos.jitter import calculate_jitter

from backend.qos.bandwidth import (
    generate_random_bandwidth,
    calculate_bandwidth
)

from backend.qos.packet_loss import (
    generate_random_packets,
    calculate_packet_loss
)


def analyze_qos():

    # 1. Latence
    latencies = generate_random_latencies(100)
    average_latency = calculate_average_latency(latencies)

    # 2. Gigue
    jitter = calculate_jitter(latencies)

    # 3. Débit
    data_size, duration = generate_random_bandwidth()
    bandwidth = calculate_bandwidth(data_size, duration)

    # 4. Perte de paquets
    sent, received = generate_random_packets(1000)
    packet_loss = calculate_packet_loss(sent, received)

    # Affichage des résultats
    print("\n========== ANALYSE GLOBALE QoS ==========")

    print("\n--- Latence ---")
    print("Latence moyenne :", average_latency, "ms")

    print("\n--- Gigue ---")
    print("Gigue moyenne :", jitter, "ms")

    print("\n--- Débit ---")
    print("Taille des données :", data_size, "MB")
    print("Durée :", duration, "secondes")
    print("Débit :", bandwidth, "Mbps")

    print("\n--- Perte de paquets ---")
    print("Paquets envoyés :", sent)
    print("Paquets reçus :", received)
    print("Taux de perte :", packet_loss, "%")

    print("\n==========================================")


if __name__ == "__main__":
    analyze_qos()