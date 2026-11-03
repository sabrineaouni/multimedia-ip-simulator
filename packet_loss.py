import random


def generate_random_packets(number_packets=1000):
    """
    Simule l'envoi et la réception des paquets.
    """

    sent_packets = number_packets

    # Simulation d'un taux de perte aléatoire entre 0 et 10 %
    loss_rate = random.uniform(0, 10)

    lost_packets = int(sent_packets * loss_rate / 100)

    received_packets = sent_packets - lost_packets

    return sent_packets, received_packets


def calculate_packet_loss(sent_packets, received_packets):
    """
    Calcule le taux de perte des paquets en pourcentage.
    """

    if sent_packets <= 0:
        return 0

    lost_packets = sent_packets - received_packets

    packet_loss = (lost_packets / sent_packets) * 100

    return round(packet_loss, 2)


if __name__ == "__main__":

    sent, received = generate_random_packets(1000)

    loss = calculate_packet_loss(sent, received)

    print("===== ANALYSE DE LA PERTE DE PAQUETS =====")
    print("Paquets envoyés :", sent)
    print("Paquets reçus :", received)
    print("Paquets perdus :", sent - received)
    print("Taux de perte :", loss, "%")