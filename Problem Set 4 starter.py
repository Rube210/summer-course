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
    """Represents a soldier with rank, fitness, and deployment status."""

    def __init__(self, name: str, rank: str, fitness: int, deployed: bool):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def dispatch(self) -> None:
        """Mark this soldier as deployed."""
        self.deployed = True

    def __str__(self) -> str:
        return f"{self.name} ({self.rank}, fitness: {self.fitness}, deployed: {self.deployed})"


def process_reports(report_list: list[str]) -> tuple[dict[str, Soldier], set[str]]:
    """Parse report strings and return (roster_dict, ranks_set)."""
    roster = {}
    ranks = set()

    for report in report_list:
        parts = []
        for part in report.split("|"):
            parts.append(part.strip())

        # Expecting format: NAME | Rank | Fitness:NN | Status:state
        name = parts[0].title()
        rank = parts[1].upper()
        fitness_field = int(parts[2].split(":", 1)[1].strip())
        status_field = parts[3].split(":", 1)[1].strip().lower()

        soldier = Soldier(
            name=name,
            rank=rank,
            fitness=fitness_field,
            deployed=(status_field == "deployed"),
        )

        roster[name] = soldier
        ranks.add(rank)

    return roster, ranks


def show_available(roster: dict[str, Soldier]) -> None:
    """Display all available soldiers, sorted alphabetically."""
    available_soldiers = []

    for name, soldier in roster.items():
        if not soldier.deployed:
            available_soldiers.append(name)

    available_soldiers.sort()
    print(f"Available soldiers: {available_soldiers}\n")


def dispatch(roster: dict[str, Soldier], name: str) -> None:
    """Dispatch a soldier by name, or print an error if not available."""
    display_name = name.title()
    print(f"Dispatching {display_name}...", end=" ")

    soldier = roster.get(display_name)
    if soldier is None:
        print(f"{display_name} not found in roster.")
        return

    if not soldier.deployed:
        soldier.dispatch()
        print("Done. Status set to deployed.")
    else:
        print(f"{display_name} is already deployed.")


def fitness_report(roster: dict[str, Soldier]) -> dict[str, list[str]]:
    """Return a dict with 'high', 'medium', 'low' fitness bands."""
    bands = {"high": [], "medium": [], "low": []}

    for name, soldier in roster.items():
        if soldier.fitness >= 80:
            bands["high"].append(name)
        elif 60 <= soldier.fitness <= 79:
            bands["medium"].append(name)
        else:
            bands["low"].append(name)

    for level in bands.values():
        level.sort()

    return bands