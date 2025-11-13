import streamlit as st
import pandas as pd
import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import charts_creation as chart
from src import tabs_content as t
from src import kpi_calculations as kpi

def tab1_render():
    battery_ids = []
    nb_charge_tests = []
    nb_discharge_tests = []
    nb_impedance_tests = []
    
    df = pd.read_csv("C:/Users/joshn/code/NASA_BatteryDataAnalysisApp/data/metadata.csv")
    df_copy = df.copy()
    unique_battery_ids = df['battery_id'].unique()
    for battery in unique_battery_ids :
        battery_ids.append(battery)
        df = df_copy[(df_copy['battery_id'] == battery) & (df_copy['type'] == 'charge')]
        nb_charge_tests.append(len(df))
        df = df_copy[(df_copy['battery_id'] == battery) & (df_copy['type'] == 'discharge')]
        nb_discharge_tests.append(len(df))
        df = df_copy[(df_copy['battery_id'] == battery) & (df_copy['type'] == 'impedance')]
        nb_impedance_tests.append(len(df))
        summary_df = pd.DataFrame({
            'Battery IDs': battery_ids,
            'Number of Charge Tests': nb_charge_tests,
            'Number of Discharge Tests': nb_discharge_tests,
            'Number of Impedance Tests': nb_impedance_tests
        })
    st.dataframe(summary_df)    


def tab2_render():
    df = pd.read_csv("C:/Users/joshn/code/NASA_BatteryDataAnalysisApp/data/metadata.csv")
    df_copy = df.copy()
    total_batteries_tested = len(df['battery_id'].unique())
    st.write(f"A total of {total_batteries_tested} batteries have been tested.")

    selected_battery_id = st.selectbox("Select a Battery ID to visualize data", options=df['battery_id'].unique().tolist())

    st.subheader(f'Resistance Evolution of {selected_battery_id}')
    df = df_copy[(df_copy['battery_id'] == selected_battery_id) & (df_copy['type'] == 'impedance')]
    st.write(f"{len(df)} impedance tests has been performed")
    impedance_evolution_fig = chart.impedance_chart(df)
    st.write(impedance_evolution_fig)
    impedance_tamb_fig = chart.tamb_chart(df)
    st.write(impedance_tamb_fig)

    st.subheader(f'Capacity Evolution of {selected_battery_id}')
    df = df_copy[(df_copy['battery_id'] == selected_battery_id) & (df_copy['type'] == 'discharge')]
    st.write(f"{len(df)} discharge tests has been performed")
    capacity_evolution_fig = chart.capacity_chart(df)
    st.write(capacity_evolution_fig)
    capacity_tamb_fig = chart.tamb_chart(df)
    st.write(capacity_tamb_fig)

    # Cycle tests data analysis
    st.subheader(f'Discharge cycles analysis of {selected_battery_id}')
    df = df_copy[(df_copy['battery_id'] == selected_battery_id) & (df_copy['type'] == 'discharge')]
    dfs = []
    for file in df['filename']:
        df = pd.read_csv(f'C:/Users/joshn/code/NASA_BatteryDataAnalysisApp/data/files/{file}')
        dfs.append(df)
    st.write(f"{len(dfs)} discharge cycles has been performed")
    voltage_fig = chart.voltage_chart(dfs)
    st.write(voltage_fig)
    current_fig = chart.current_chart(dfs)
    st.write(current_fig)
    temperature_fig = chart.tamb_charts(dfs)
    st.write(temperature_fig)

    st.subheader(f'Charge cycles analysis of {selected_battery_id}')
    df = df_copy[(df_copy['battery_id'] == selected_battery_id) & (df_copy['type'] == 'charge')]
    dfs = []
    for file in df['filename']:
        df = pd.read_csv(f'C:/Users/joshn/code/NASA_BatteryDataAnalysisApp/data/files/{file}')
        dfs.append(df)
    st.write(f"{len(dfs)} charge cycles has been performed")
    voltage_fig = chart.voltage_chart(dfs)
    st.write(voltage_fig)
    current_fig = chart.current_chart(dfs)
    st.write(current_fig)
    temperature_fig = chart.tamb_charts(dfs)
    st.write(temperature_fig)

def tab3_render():
    df = pd.read_csv("C:/Users/joshn/code/NASA_BatteryDataAnalysisApp/data/metadata.csv")
    df_copy = df.copy()
    total_batteries_tested = len(df['battery_id'].unique())
    st.write(f"A total of {total_batteries_tested} batteries have been tested.")

    selected_battery_id = st.selectbox("Select a Battery ID to compute capacity", options=df['battery_id'].unique().tolist())
    st.subheader(f'Capacity Evolution of {selected_battery_id}')
    df = df_copy[(df_copy['battery_id'] == selected_battery_id) & (df_copy['type'] == 'discharge')]
    st.write(f"{len(df)} discharge tests has been performed")

    test_ids = df['test_id'].tolist()
    capacities_precomputed = df['Capacity'].tolist()
    capacities_computed = []
    for file in df['filename']:
        df = pd.read_csv(f'C:/Users/joshn/code/NASA_BatteryDataAnalysisApp/data/files/{file}')
        capacity = kpi.capacity(df)
        capacities_computed.append(capacity)

    df_capacity = pd.DataFrame({
        'Precomputed Capacity': capacities_precomputed,
        'Computed Capacity': capacities_computed,
        'test_id' : test_ids
    })
    
    st.write(chart.capacity_comparision_charts(df_capacity))

