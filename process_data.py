def pre_process_data(data):
    processed_data = []
    aliased_pedestrians = []

    # for row in sorted(data, key=lambda x: sorting_order.index(x[2]) if x[2] in sorting_order else float('inf')):
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