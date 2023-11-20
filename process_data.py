import matplotlib.pyplot as plt


def pre_process_data(data):
    processed_data = []
    aliased_pedestrians = []

    for row in data:
        time, ped_id, spots, aliases = row[:5]

        if aliases[0] == 0:
            continue
        if spots[0] == 0 and len(spots):
            continue

        for alias in aliases:
            matching_pedestrian = next((p for p in data if p[1] == alias), None)
            aliased_pedestrians.append(matching_pedestrian[1])
            if matching_pedestrian:
                spots += [spot for spot in matching_pedestrian[2] if spot not in spots]

        if ped_id not in aliased_pedestrians:
            time = time.strftime("%H:%M")
            processed_data.append((time, ped_id, spots))

    return processed_data


def going_up_going_down(data):
    time_counts = {}
    up_counts = {}
    down_counts = {}
    going_up = []
    going_down = []

    for entry in data:
        time_str, ped_id, spots = entry
        time_obj = time_str
        direction = "up" if spots[-1] > 10 > spots[0] else "down" if spots[-1] < 10 < spots[0] else "none"

        time_counts[time_obj] = time_counts.get(time_obj, 0) + 1
        if direction == "up":
            up_counts[time_obj] = up_counts.get(time_obj, 0) + 1
            going_up.append(entry)
        elif direction == "down":
            down_counts[time_obj] = down_counts.get(time_obj, 0) + 1
            going_down.append(entry)

    # Convert the data for plotting
    times = list(time_counts.keys())
    # ped_counts = list(time_counts.values())
    up_ped_counts = [up_counts.get(time, 0) for time in times]
    down_ped_counts = [down_counts.get(time, 0) for time in times]

    fig, ax = plt.subplots(figsize=(16, 6))
    bar_width = 0.4

    indices = range(len(times))
    up_x = [x - bar_width / 2 for x in indices]
    down_x = [x + bar_width / 2 for x in indices]

    # ax.bar(indices, ped_counts, width=bar_width, label='Total Pedestrians', align='center')
    ax.bar(up_x, up_ped_counts, width=bar_width, label='Pedestrians Going Up', color='green', alpha=0.7)
    ax.bar(down_x, down_ped_counts, width=bar_width, label='Pedestrians Going Down', color='blue', alpha=0.7)

    plt.xlabel('Time')
    plt.ylabel('Number of Pedestrians')
    plt.title('Pedestrian Traffic 2023-11-20')
    plt.xticks(indices, times, rotation=45, ha='right')  # Use the original times as x-axis labels
    plt.legend()
    plt.show()

    return going_up, going_down


def going_up_end_direction(data):
    time_counts = {}
    left_counts = {}
    right_counts = {}

    for entry in data:
        time_str, ped_id, spots = entry
        time_obj = time_str
        direction = "right" if (spots[-1] > 11 and spots[-1] % 2 == 0) else "left" if (
                spots[-1] > 11 and spots[-1] % 2 != 0) else "none"

        time_counts[time_obj] = time_counts.get(time_obj, 0) + 1
        if direction == "left":
            left_counts[time_obj] = left_counts.get(time_obj, 0) + 1
        elif direction == "right":
            right_counts[time_obj] = right_counts.get(time_obj, 0) + 1

    times = list(time_counts.keys())
    left_ped_counts = [left_counts.get(time, 0) for time in times]
    right_ped_counts = [right_counts.get(time, 0) for time in times]

    fig, ax = plt.subplots(figsize=(16, 6))
    bar_width = 0.4

    indices = range(len(times))
    up_x = [x - bar_width / 2 for x in indices]
    down_x = [x + bar_width / 2 for x in indices]

    ax.bar(up_x, left_ped_counts, width=bar_width, label='Pedestrians Going left', color='green', alpha=0.7)
    ax.bar(down_x, right_ped_counts, width=bar_width, label='Pedestrians Going right', color='blue', alpha=0.7)

    # plt.subplots(figsize=(12, 6))
    plt.xlabel('Time')
    plt.ylabel('Number of Pedestrians')
    plt.title('Pedestrian going up end direction 2023-11-20')
    plt.xticks(indices, times, rotation=45, ha='right')
    plt.legend()
    plt.show()


def going_up_start_destination(data):
    time_counts = {}
    left_counts = {}
    right_counts = {}
    center_counts = {}

    for entry in data:
        time_str, ped_id, spots = entry
        time_obj = time_str
        direction = "right" if (spots[0] == 4 or spots[0] == 5 or spots[0] == 7) else "left" if (
                spots[0] == 1 or spots[0] == 2 or spots[0] == 3) else "center" if spots[0] == 6 else "none"

        time_counts[time_obj] = time_counts.get(time_obj, 0) + 1
        if direction == "left":
            left_counts[time_obj] = left_counts.get(time_obj, 0) + 1
        elif direction == "right":
            right_counts[time_obj] = right_counts.get(time_obj, 0) + 1
        elif direction == "center":
            center_counts[time_obj] = center_counts.get(time_obj, 0) + 1

    times = list(time_counts.keys())
    left_ped_counts = [left_counts.get(time, 0) for time in times]
    right_ped_counts = [right_counts.get(time, 0) for time in times]
    center_ped_counts = [center_counts.get(time, 0) for time in times]

    fig, ax = plt.subplots(figsize=(18, 6))
    bar_width = 0.4
    indices = range(len(times))
    up_x = [x - bar_width / 2 for x in indices]
    center_x = indices
    down_x = [x + bar_width / 2 for x in indices]

    ax.bar(up_x, left_ped_counts, width=bar_width, label='left', color='green', alpha=0.7)
    ax.bar(center_x, center_ped_counts, width=bar_width, label='center', color='red', alpha=0.7)
    ax.bar(down_x, right_ped_counts, width=bar_width, label='right', color='blue', alpha=0.7)

    # plt.subplots(figsize=(12, 6))
    plt.xlabel('Time')
    plt.ylabel('Number of Pedestrians')
    plt.title('Pedestrian going up start direction 2023-11-16')
    plt.xticks(indices, times, rotation=45, ha='right')
    plt.legend()
    plt.show()


def going_down_destination(data):
    time_counts = {}
    left_counts = {}
    right_counts = {}
    center_counts = {}

    for entry in data:
        time_str, ped_id, spots = entry
        time_obj = time_str
        direction = "right" if (spots[-1] == 4 or spots[-1] == 5 or spots[-1] == 7) else "left" if (
                spots[-1] == 1 or spots[-1] == 2 or spots[-1] == 3) else "center" if spots[-1] == 6 else "none"

        time_counts[time_obj] = time_counts.get(time_obj, 0) + 1
        if direction == "left":
            left_counts[time_obj] = left_counts.get(time_obj, 0) + 1
        elif direction == "right":
            right_counts[time_obj] = right_counts.get(time_obj, 0) + 1
        elif direction == "center":
            center_counts[time_obj] = center_counts.get(time_obj, 0) + 1

    times = list(time_counts.keys())
    left_ped_counts = [left_counts.get(time, 0) for time in times]
    right_ped_counts = [right_counts.get(time, 0) for time in times]
    center_ped_counts = [center_counts.get(time, 0) for time in times]

    fig, ax = plt.subplots(figsize=(18, 6))
    bar_width = 0.4

    indices = range(len(times))
    up_x = [x - bar_width / 2 for x in indices]
    center_x = indices
    down_x = [x + bar_width / 2 for x in indices]

    ax.bar(up_x, left_ped_counts, width=bar_width, label='left', color='green', alpha=0.7)
    ax.bar(center_x, center_ped_counts, width=bar_width, label='center', color='red', alpha=0.7)
    ax.bar(down_x, right_ped_counts, width=bar_width, label='right', color='blue', alpha=0.7)

    # plt.subplots(figsize=(12, 6))
    plt.xlabel('Time')
    plt.ylabel('Number of Pedestrians')
    plt.title('Pedestrian going down destination 2023-11-16')
    plt.xticks(indices, times, rotation=45, ha='right')
    plt.legend()
    plt.show()


def going_down_start_direction(data):
    time_counts = {}
    left_counts = {}
    right_counts = {}
    # none_counts = {}

    for entry in data:
        time_str, ped_id, spots = entry
        time_obj = time_str
        direction = "right" if (spots[0] > 11 and spots[0] % 2 == 0) else "left" if (
                spots[0] > 11 and spots[0] % 2 != 0) else "none"

        time_counts[time_obj] = time_counts.get(time_obj, 0) + 1
        if direction == "left":
            left_counts[time_obj] = left_counts.get(time_obj, 0) + 1
        elif direction == "right":
            right_counts[time_obj] = right_counts.get(time_obj, 0) + 1
        # elif direction == "none":
            # none_counts[time_obj] = none_counts.get(time_obj, 0) + 1

    times = list(time_counts.keys())

    fig, ax = plt.subplots(figsize=(16, 6))
    bar_width = 0.4

    indices = range(len(times))
    up_x = [x - bar_width / 2 for x in indices]
    # none_x = indices
    down_x = [x + bar_width / 2 for x in indices]

    # Use the same set of times for getting counts
    left_ped_counts = [left_counts.get(time, 0) for time in times]
    # none_ped_counts = [none_counts.get(time, 0) for time in times]
    right_ped_counts = [right_counts.get(time, 0) for time in times]

    ax.bar(up_x, left_ped_counts, width=bar_width, label='left', color='green', alpha=0.7)
    # ax.bar(none_x, none_ped_counts, width=bar_width, label='not specified', color='red', alpha=0.7)
    ax.bar(down_x, right_ped_counts, width=bar_width, label='right', color='blue', alpha=0.7)

    # plt.subplots(figsize=(12, 6))
    plt.xlabel('Time')
    plt.ylabel('Number of Pedestrians')
    plt.title('Pedestrian going down start direction 2023-11-16')
    plt.xticks(indices, times, rotation=45, ha='right')
    plt.legend()
    plt.show()


# TEST
def plot_direction_histogram(data):
    left_counts = 0
    right_counts = 0

    for entry in data:
        time_str, ped_id, spots = entry

        # Check if the condition for going right is met
        if spots[-1] > 11 and spots[-1] % 2 == 0:
            right_counts += 1

        # Check if the condition for going left is met
        elif spots[-1] > 11 and spots[-1] % 2 != 0:
            left_counts += 1

    # Plot the histogram
    fig, ax = plt.subplots()
    categories = ['Going Left', 'Going Right']
    counts = [left_counts, right_counts]
    colors = ['blue', 'green']

    ax.bar(categories, counts, color=colors)
    plt.xlabel('Direction')
    plt.ylabel('Number of Pedestrians')
    plt.title('Pedestrian Direction Histogram')

    # Display the plot
    plt.show()
