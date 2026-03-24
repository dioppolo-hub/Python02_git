class PlantError(Exception):
    def __init__(self, message="Plant error"):
        Exception.__init__(self, message)


def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants):
    try:
        print("Opening watering systems")
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print("Caught PlantError:", e)
        print("...ending tests and return to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Carrot", "Lettuce"])
    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "caRRoT", "LEttUcE"])
    print("\nCleanup always happens, even with errors!")
