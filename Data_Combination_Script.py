import os
import pandas as pd

base_dir = 'Activity_Data'
activities = ['Jumping', 'Standing', 'Still', 'Walking']


for activity in activities:
    activity_dir = os.path.join(base_dir, activity)
    acc_files = []
    gyro_files = []
    for root, dirs, files in os.walk(activity_dir):
        for file in files:
            if file == 'Accelerometer.csv':
                acc_files.append(os.path.join(root, file))
            elif file == 'Gyroscope.csv':
                gyro_files.append(os.path.join(root, file))

    # Combine Accelerometer files
    acc_dfs = [pd.read_csv(f) for f in acc_files]
    if acc_dfs:
        acc_combined = pd.concat(acc_dfs, ignore_index=True)
        # Sort by time column
        if 'time' in acc_combined.columns:
            acc_combined = acc_combined.sort_values('time')
        acc_combined.to_csv(os.path.join(activity_dir, f'{activity}_Accelerometer_combined.csv'), index=False)

    # Combine Gyroscope files
    gyro_dfs = [pd.read_csv(f) for f in gyro_files]
    if gyro_dfs:
        gyro_combined = pd.concat(gyro_dfs, ignore_index=True)
        # Sort by time column
        if 'time' in gyro_combined.columns:
            gyro_combined = gyro_combined.sort_values('time')
        gyro_combined.to_csv(os.path.join(activity_dir, f'{activity}_Gyroscope_combined.csv'), index=False)