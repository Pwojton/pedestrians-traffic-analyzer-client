import os
from database import fetch_data_from_db
from process_data import pre_process_data, going_up_going_down, going_up_end_direction, plot_direction_histogram, \
    going_up_start_destination, going_down_destination, going_down_start_direction


def main():
    data = fetch_data_from_db()
    processed_data = pre_process_data(data)
    going_up, going_down = going_up_going_down(processed_data)

    print(len(going_up))

    going_up_end_direction(going_up)
    # # plot_direction_histogram(going_up)
    going_up_start_destination(going_up)
    #
    going_down_destination(going_down)
    going_down_start_direction(going_down)


if __name__ == '__main__':
    main()
