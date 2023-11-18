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

    fig, ax = plt.subplots()
    bar_width = 0.3

    indices = range(len(times))
    up_x = [x - bar_width / 2 for x in indices]
    down_x = [x + bar_width / 2 for x in indices]

    # ax.bar(indices, ped_counts, width=bar_width, label='Total Pedestrians', align='center')
    ax.bar(up_x, up_ped_counts, width=bar_width, label='Pedestrians Going Up', color='green', alpha=0.7)
    ax.bar(down_x, down_ped_counts, width=bar_width, label='Pedestrians Going Down', color='blue', alpha=0.7)

    plt.xlabel('Time')
    plt.ylabel('Number of Pedestrians')
    plt.title('Pedestrian Traffic 2023-11-16')
    plt.xticks(indices, times, rotation=45, ha='right')  # Use the original times as x-axis labels
    plt.legend()
    plt.show()

    return going_up, going_down