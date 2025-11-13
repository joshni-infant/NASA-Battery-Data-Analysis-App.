def capacity(df):
    df['Capacity_computed'] = df['Voltage_measured'] * df['Time'] 
    capacity_value = df['Capacity_computed'].sum() / 3600 / 1000
    return capacity_value
