def input_temperature(temp_str):
    x = int(temp_str)
    return x


def test_temperature(temp_str):
    try:
        x = input_temperature(temp_str)
        if x < 0:
            raise Exception
        elif x > 40:
            raise Exception
        else:
            print(f"Temperature is now {x}°C")
    except ValueError:
        print(
            f"Caught input_temperature error: invalid literal"
            f"for int() with base 10: '{temp_str}'"
        )
        print("\nAll tested completed - program didn't crash!")
    except Exception:
        if x > 40:
            print(
                f"Caught input_temperature error: {temp_str}°C "
                f"is too hot for plants (max 40°C)"
            )
            print("\nAll tested completed - program didn't crash!")
        elif x < 0:
            print(
                f"Caught input_temperature error: {temp_str}°C "
                f"is too cold for plants (min 0°C)"
            )
            print("\nAll tested completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    temp_str = "40"
    print(f"Input data is '{temp_str}'")
    test_temperature(temp_str)
