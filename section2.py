import pandas as pd
import numpy as np
1. def calculate_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
    if 'latitude' not in df.columns or 'longitude' not in df.columns:
        raise ValueError("DataFrame must contain 'latitude' and 'longitude' columns.")
    latitudes = df['latitude'].values
    longitudes = df['longitude'].values
    distance_matrix = np.zeros((len(df), len(df)))
    for i in range(len(df)):
        for j in range(len(df)):
            distance_matrix[i, j] = haversine(latitudes[i], longitudes[i], latitudes[j], longitudes[j])
    distance_df = pd.DataFrame(distance_matrix, index=df.index, columns=df.index)
    
    return distance_df
df = pd.DataFrame(data)
distance_matrix = calculate_distance_matrix(df)
print(distance_matrix)

2. def unroll_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
    unrolled_data = []
    indices = df.index
    for i in range(len(df)):
        for j in range(i + 1, len(df)):
            distance = df.iloc[i, j]
            unrolled_data.append({
                'id_start': indices[i],
                'id_end': indices[j],
                'distance': distance
            })
    unrolled_df = pd.DataFrame(unrolled_data)
    
    return unrolled_df
distance_matrix = pd.DataFrame(distance_data)
distance_matrix.index = ['A', 'B', 'C']
unrolled_df = unroll_distance_matrix(distance_matrix)
print(unrolled_df)

3. def find_ids_within_ten_percentage_threshold(df: pd.DataFrame, reference_id: int) -> pd.DataFrame:
    reference_distances = df[(df['id_start'] == reference_id) | (df['id_end'] == reference_id)]
    if reference_distances.empty:
        return pd.DataFrame(columns=['id', 'average_distance'])
    average_reference_distance = reference_distances['distance'].mean()
    lower_threshold = average_reference_distance * 0.9
    upper_threshold = average_reference_distance * 1.1
    grouped = df.groupby('id_start')['distance'].mean().reset_index()
    grouped = grouped.rename(columns={'id_start': 'id', 'distance': 'average_distance'})
    grouped_end = df.groupby('id_end')['distance'].mean().reset_index()
    grouped_end = grouped_end.rename(columns={'id_end': 'id', 'distance': 'average_distance'})
    combined = pd.concat([grouped, grouped_end]).groupby('id')['average_distance'].mean().reset_index()
    result = combined[(combined['average_distance'] >= lower_threshold) & (combined['average_distance'] <= upper_threshold)]
    return result
df = pd.DataFrame(data)
reference_id = 1
result_df = find_ids_within_ten_percentage_threshold(df, reference_id)
print(result_df)

4. def calculate_toll_rate(df: pd.DataFrame) -> pd.DataFrame:
     if 'vehicle_type' not in df.columns or 'distance' not in df.columns:
        raise ValueError("DataFrame must contain 'vehicle_type' and 'distance' columns.")
    df['toll'] = df.apply(lambda row: row['distance'] * toll_rates.get(row['vehicle_type'], 0), axis=1)
    return df
df = pd.DataFrame(data)
result_df = calculate_toll_rate(df)
print(result_df)

5. def calculate_time_based_toll_rates(df: pd.DataFrame) -> pd.DataFrame:
     if 'timestamp' not in df.columns or 'distance' not in df.columns:
        raise ValueError("DataFrame must contain 'timestamp' and 'distance' columns.")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    def get_toll_rate(row):
        time = row['timestamp'].time()  # Get the time part
        distance = row['distance']
        if time >= pd.to_datetime('06:00:00').time() and time < pd.to_datetime('10:00:00').time():
            return distance * toll_rates['morning_rush']
        elif time >= pd.to_datetime('10:00:00').time() and time < pd.to_datetime('16:00:00').time():
            return distance * toll_rates['midday']
        elif time >= pd.to_datetime('16:00:00').time() and time < pd.to_datetime('20:00:00').time():
            return distance * toll_rates['evening_rush']
        else:  # Late night
            return distance * toll_rates['late_night']
    df['toll'] = df.apply(get_toll_rate, axis=1)
    return df
df = pd.DataFrame(data)
result_df = calculate_time_based_toll_rates(df)
print(result_df)
