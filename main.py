from database import fetch_data_from_db
from process_data import pre_process_data, going_up_going_down


def main():
    data = fetch_data_from_db()
    processed_data = pre_process_data(data)
    going_up, going_down = going_up_going_down(processed_data)


if __name__ == '__main__':
    main()
