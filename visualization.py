import matplotlib.pyplot as plt
from pathlib import Path

from backend.scenarios.normal import generate_normal_scenario
from backend.scenarios.loaded import generate_loaded_scenario
from backend.scenarios.congestion import generate_congestion_scenario

from backend.qos.qos_prioritization import (
    simulate_without_qos,
    simulate_with_qos
)


# Dossier pour enregistrer les graphiques
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


# ==========================================
# GRAPHIQUE 1 : COMPARAISON DES SCENARIOS
# ==========================================

def plot_scenario_comparison():

    normal = generate_normal_scenario()
    loaded = generate_loaded_scenario()
    congestion = generate_congestion_scenario()

    scenarios = [normal, loaded, congestion]

    names = ["Normal", "Chargé", "Congestion"]

    indicators = [
        ("latency", "Latence (ms)"),
        ("jitter", "Gigue (ms)"),
        ("bandwidth", "Débit (Mbps)"),
        ("packet_loss", "Perte de paquets (%)")
    ]

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    fig.suptitle(
        "Comparaison des scénarios réseau",
        fontsize=16,
        fontweight="bold"
    )

    for ax, (key, title) in zip(axes.flat, indicators):

        values = [scenario[key] for scenario in scenarios]

        bars = ax.bar(names, values)

        ax.set_title(title)
        ax.set_ylabel(title)
        ax.grid(axis="y", linestyle="--", alpha=0.4)

        for bar in bars:
            height = bar.get_height()

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{height:.2f}",
                ha="center",
                va="bottom"
            )

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "scenario_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ==========================================
# GRAPHIQUE 2 : AVEC ET SANS QoS
# ==========================================

def plot_qos_comparison():

    without_qos = simulate_without_qos()
    with_qos = simulate_with_qos()

    traffic_types = ["voice", "video", "data"]

    traffic_names = ["Voix", "Vidéo", "Data"]

    metrics = [
        ("latency", "Latence (ms)"),
        ("packet_loss", "Perte de paquets (%)")
    ]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    fig.suptitle(
        "Impact de la priorisation QoS",
        fontsize=16,
        fontweight="bold"
    )

    x = range(len(traffic_types))
    width = 0.35

    for ax, (metric, title) in zip(axes, metrics):

        values_without = [
            without_qos[traffic][metric]
            for traffic in traffic_types
        ]

        values_with = [
            with_qos[traffic][metric]
            for traffic in traffic_types
        ]

        bars1 = ax.bar(
            [i - width / 2 for i in x],
            values_without,
            width,
            label="Sans QoS"
        )

        bars2 = ax.bar(
            [i + width / 2 for i in x],
            values_with,
            width,
            label="Avec QoS"
        )

        ax.set_title(title)
        ax.set_xticks(list(x))
        ax.set_xticklabels(traffic_names)
        ax.legend()
        ax.grid(axis="y", linestyle="--", alpha=0.4)

        for bars in [bars1, bars2]:
            for bar in bars:

                height = bar.get_height()

                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    height,
                    f"{height:.2f}",
                    ha="center",
                    va="bottom",
                    fontsize=9
                )

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "qos_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# ==========================================
# EXECUTION
# ==========================================

if __name__ == "__main__":

    print("Génération des graphiques QoS...")

    plot_scenario_comparison()

    plot_qos_comparison()

    print("\nLes graphiques ont été enregistrés dans le dossier results.")