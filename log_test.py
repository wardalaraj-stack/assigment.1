import csv

LEDGER_FILE = "test-ledger.csv"

COLUMNS = ["area", "test_case", "input_summary", "expected_result",
           "actual_result", "owner", "status", "date"]

PROMPTS = ["Area", "Test case", "Input summary", "Expected result",
           "Actual result", "Owner", "Status", "Date (YYYY-MM-DD)"]


def ask_for_row(prompts):
    """Ask one question per column and return the answers as a list."""
    row = []
    for prompt in prompts:
        answer = input(prompt + ": ").strip()
        row.append(answer)
    return row


def append_row(filename, row):
    """Add one row to the end of the CSV file."""
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)


def main():
    row = ask_for_row(PROMPTS)
    append_row(LEDGER_FILE, row)
    print("Test logged.")


if __name__ == "__main__":
    main()