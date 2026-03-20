def garden_operations(operation_number):
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("esempio.txt", "r")
    elif operation_number == 3:
        temp_str2 = "abc"
        a = 5
        temp_str2 + a
    elif operation_number > 3:
        print(f"Testing operation {operation_number}...")
        print("Operation completed successfully")


def test_error_types(operation_number):
    try:
        garden_operations(operation_number)
    except ValueError:
        print(f"Testing operation {operation_number}...")
        print(
            "Caught ValueError: invalid "
            "literal for int() with base 10: 'abc'"
        )
    except ZeroDivisionError:
        print(f"Testing operation {operation_number}...")
        print("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        print(f"Testing operation {operation_number}...")
        print(
            "Caught FileNotFoundError: [Errno 2] "
            "No such file or directory: '/non/existent/file'"
        )
    except TypeError:
        print(f"Testing operation {operation_number}...")
        print("Caught TypeError: can only concatenate str (not 'int') to str")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    operation_number = 0
    while operation_number <= 4:
        test_error_types(operation_number)
        operation_number += 1
    print("\nAll error types tested successfully")
