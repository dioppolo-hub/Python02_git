class GardenError(Exception):
    def __init__(self, message="Generic garden error"):
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message="Plant error"):
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message="Water error"):
        GardenError.__init__(self, message)


def plant_seed(seed_type):
    if seed_type not in ["Tulip", "Rose", "Sunflower"]:
        raise PlantError("Seed not supported")
    print("Seed planted")


def water_plant(amount):
    if amount < 0:
        raise WaterError("Insert only positive numbers")
    print(f"Water amount: {amount}l")


if __name__ == "__main__":
    print("=== Custom Garden Errors DEmp ===")
    try:
        print("\nTesting PlantError...")
        plant_seed("Rose")
        plant_seed("Tree")
    except PlantError as e:
        print("Plant Error:", e)
    try:
        print("\nTesting WaterError...")
        water_plant(8)
        water_plant(-8)
    except WaterError as e:
        print("Water Error:", e)
    try:
        print("\nTesting GardenError...")
        plant_seed("Tree")
        water_plant(-9)
    except GardenError as e:
        print("Garden Error:", e)
    try:
        water_plant(-9)
    except GardenError as e:
        print("Garden Error:", e)
    print("\nAll custom error types work correctly!")
