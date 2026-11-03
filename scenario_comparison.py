from backend.scenarios.normal import generate_normal_scenario
from backend.scenarios.loaded import generate_loaded_scenario
from backend.scenarios.congestion import generate_congestion_scenario


def compare_scenarios():

    # Exécution des trois scénarios
    normal = generate_normal_scenario()
    loaded = generate_loaded_scenario()
    congestion = generate_congestion_scenario()

    scenarios = [normal, loaded, congestion]

    # Affichage du tableau comparatif
    print("\n========== COMPARAISON DES SCENARIOS QoS ==========")

    print(
        f"{'Indicateur':<20}"
        f"{'Normal':<15}"
        f"{'Charge':<15}"
        f"{'Congestion':<15}"
    )

    print("-" * 65)

    indicators = ["latency", "jitter", "bandwidth", "packet_loss"]

    for indicator in indicators:

        normal_value = normal[indicator]
        loaded_value = loaded[indicator]
        congestion_value = congestion[indicator]

        print(
            f"{indicator:<20}"
            f"{normal_value:<15}"
            f"{loaded_value:<15}"
            f"{congestion_value:<15}"
        )

    print("=" * 65)


if __name__ == "__main__":
    compare_scenarios()