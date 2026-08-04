# Problem 1
reports = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]

class Soldier:
    def __init__(self, name, rank, fitness, deployed):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def dispatch(self):
        self.deployed = True

    def __str__(self):
        return (
            f"{self.name} ({self.rank}, fitness: {self.fitness}, "
            f"deployed: {self.deployed})"
        )


def process_reports(reports):
    roster = {}
    ranks = set()

    for report in reports:
        fields = report.split("|")
        data = {}

        for field in fields:
            key, value = field.strip().split(":")
            data[key.strip().lower()] = value.strip()

        name = data["name"].title()
        rank = data["rank"].upper()
        fitness = int(data["fitness"])
        status = data["status"].lower()

        deployed = status in {"deployed", "true", "yes"}

        soldier = Soldier(name, rank, fitness, deployed)
        roster[name] = soldier
        ranks.add(rank)

    return roster, ranks