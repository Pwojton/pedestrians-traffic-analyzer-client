from database import fetch_data_from_db
from process_data import process_data


def main():
    going_up = []
    going_down = []

    data = fetch_data_from_db()
    processed_data = process_data(data)
    # sorting_order = [6, 14, 13, 1, 2, 3, 10, 8]


if __name__ == '__main__':
    main()
