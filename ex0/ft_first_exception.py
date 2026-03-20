def input_temperature(temp_str):
    x = int(temp_str)
    print(f"Temperature is now {x}°C")
    return x


def test_temperature(temp_str):
    try:
        input_temperature(temp_str)
    except ValueError:
        print(
            f"Caught input_temperature error: invalid literal"
            f"for int() with base 10: '{temp_str}'"
        )
        print("\nAll tested completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    temp_str = "34"
    print(f"Input data is '{temp_str}'")
    x = test_temperature(temp_str)
