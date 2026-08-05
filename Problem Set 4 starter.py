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
    def __init__(self, name: str, rank: str, fitness: int, deployed: bool):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def dispath(self):
        self.deployed = True

    def _str_(self):
        return f"{self.name} ({self.rank}, fitness: {self.fitness}, deployed: {self.deployed})"

    def process_reports(report_list: list[str]) -> tuple[dict[str, Soldier], set[str]]:
        roster = {}
        ranks = set()

        for report in report_list:
            parts = []
            for part in report.split("|"):
                parts.append(part.strip())

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
                
    available_soldiers = []
            
    for name, soldier in roster.items():
        if not soldier.deployed:
            available_soldiers.append(name)
            
    available_soldiers.sort()
    print(f"Available soldiers: {available_soldiers}\n")
            
            
def dispatch(roster: dict[str, Soldier], name: str) -> None:
                
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
    pass
# Problem 2
recipe_data = {
    "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese":  ["bread", "cheese", "butter"],
}

pantry_items = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]

class Recipe:
    

    def __init__(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, pantry_set: set[str]) -> bool:
       
        for ingredient in self.ingredients:
            if ingredient not in pantry_set:
                return False
        return True

    def missing_ingredients(self, pantry_set: set[str]) -> list[str]:
        
        missing = []
        for ingredient in self.ingredients:
            if ingredient not in pantry_set:
                missing.append(ingredient)
        missing.sort()
        return missing


class Pantry:
    

    def __init__(self, items: list[str]):
        self.items = set(items)

    def add_ingredients(self, extra_ingredients: list[str]) -> None:
        """Add new ingredients to the pantry."""
        for ingredient in extra_ingredients:
            self.items.add(ingredient)

    def has(self, ingredient: str) -> bool:
        """Check if the pantry contains an ingredient."""
        return ingredient in self.items

    def get_items(self) -> set[str]:
        """Return the set of all items in the pantry."""
        return self.items


def create_recipes(recipe_data: dict[str, list[str]]) -> list[Recipe]:
    """Convert recipe dictionary to list of Recipe objects."""
    recipes = []
    for name, ingredients in recipe_data.items():
        recipes.append(Recipe(name, ingredients))
    return recipes


def check_recipes(recipes: list[Recipe], pantry: Pantry) -> None:
    """Check which recipes can be made and print results."""
    print("=== RECIPE CHECKER ===")

    all_ingredients = set()
    pantry_set = pantry.get_items()

    for recipe in recipes:
        for ingredient in recipe.ingredients:
            all_ingredients.add(ingredient)

        if recipe.can_make(pantry_set):
            print(f"{recipe.name:<14}: CAN MAKE ✓")
        else:
            missing = recipe.missing_ingredients(pantry_set)
            print(f"{recipe.name:<14}: MISSING — {missing}")

    unique = list(all_ingredients)
    unique.sort()
    print(f"\nAll unique ingredients ({len(unique)}): {unique}")

