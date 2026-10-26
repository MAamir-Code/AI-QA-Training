"""Python basics for QA: variables, conditions, loops, functions, and a first check."""

LARGE_TEAM_SIZE = 5


def calculate_total_pay(base_salary, bonus=0):
    """Return the total pay for one employee."""
    return base_salary + bonus


def main():
    # Variables and arithmetic
    employee_count = 10
    base_salary = 100
    bonus = 20

    total_pay = calculate_total_pay(base_salary, bonus)
    print(f"Total pay per employee: {total_pay}")
    print(f"Total payroll: {employee_count * total_pay}")

    # Conditions
    if employee_count > LARGE_TEAM_SIZE:
        print("Large team")
    else:
        print("Small team")

    # Lists and loops
    salaries = [100, 150, 200]
    for salary in salaries:
        print(f"Salary {salary} + bonus = {calculate_total_pay(salary, bonus)}")

    # A first check - the seed of every test
    expected = 120
    actual = calculate_total_pay(base_salary, bonus)
    assert actual == expected, f"Expected {expected}, got {actual}"
    print("PASS: total pay is correct")

    # Data-driven checks: the same check, many inputs
    cases = [(100, 20, 120), (150, 0, 150), (200, 50, 250)]
    for base, extra, expected_pay in cases:
        assert calculate_total_pay(base, extra) == expected_pay
        print(f"PASS: {base} + {extra} = {expected_pay}")


if __name__ == "__main__":
    main()
