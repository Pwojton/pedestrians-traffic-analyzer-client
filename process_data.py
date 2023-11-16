def process_data(data):
    processed_data = []
    aliased_pedestrians = []

    # for row in sorted(data, key=lambda x: sorting_order.index(x[2]) if x[2] in sorting_order else float('inf')):
    for row in data:
        start_time, stop_time, ped_id, spots, aliases = row[:5]

        if aliases[0] == 0:
            continue
        if spots[0] == 0 and len(spots):
            continue

        for alias in aliases:
            matching_pedestrian = next((p for p in data if p[2] == alias), None)
            aliased_pedestrians.append(matching_pedestrian[2])
            if matching_pedestrian:
                spots += [spot for spot in matching_pedestrian[3] if spot not in spots]

        # print(ped_id, sorted(spots, key=lambda x: sorting_order.index(x) if x in sorting_order else float('inf')))
        if ped_id not in aliased_pedestrians:
            processed_data.append(row)
            print(start_time, stop_time, ped_id, spots)
    return processed_data