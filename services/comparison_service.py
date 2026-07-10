class ComparisonService:

    @staticmethod
    def compare(previous_report: dict, current_report: dict):

        previous_tests = {}

        current_tests = {}

        # -----------------------------
        # Convert list -> dictionary
        # -----------------------------

        for test in previous_report.get("tests", []):

            previous_tests[test["name"].lower()] = test

        for test in current_report.get("tests", []):

            current_tests[test["name"].lower()] = test

        comparison = []

        all_tests = sorted(
            set(previous_tests.keys()) |
            set(current_tests.keys())
        )

        # -----------------------------
        # Compare values
        # -----------------------------

        for name in all_tests:

            previous = previous_tests.get(name)

            current = current_tests.get(name)

            previous_value = (
                previous["value"]
                if previous
                else "N/A"
            )

            current_value = (
                current["value"]
                if current
                else "N/A"
            )

            direction = "→"

            difference = "N/A"

            try:

                p = float(previous_value)

                c = float(current_value)

                diff = round(c - p, 2)

                difference = diff

                if diff > 0:

                    direction = "▲"

                elif diff < 0:

                    direction = "▼"

            except:

                pass

            comparison.append({

                "test": name.title(),

                "previous": previous_value,

                "current": current_value,

                "difference": difference,

                "direction": direction

            })

        return comparison