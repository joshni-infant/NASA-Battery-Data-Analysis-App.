import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def impedance_chart(df):
    df['Re'] = pd.to_numeric(df['Re'])
    df['Rct'] = pd.to_numeric(df['Rct'])
    fig, ax = plt.subplots(figsize=(10,6))
    plt.plot(df['test_id'],df['Re'], label='Re')
    plt.plot(df['test_id'],df['Rct'], label='Rct')
    plt.legend()
    plt.xlabel('Test ids')    
    plt.ylabel('Resistance (Ohm)')
    plt.yticks(rotation=45)
    plt.title('Impedance evolution')
    return fig 

def tamb_chart(df):  
    fig, ax = plt.subplots(figsize=(10,6))
    plt.plot(df['test_id'],df['ambient_temperature'], label='ambient_temperature')
    plt.xlabel('Test ids')    
    ax.set_ylabel('Temperature (°C)')
    ax.set_xlabel('Test ids')
    plt.yticks(rotation=45)
    plt.title('Ambient temperatures')
    return fig

def capacity_chart(df):
    df['Capacity'] = pd.to_numeric(df['Capacity'])
    fig, ax = plt.subplots(figsize=(10,6))
    plt.plot(df['test_id'],df['Capacity'], label='Capacity')
    plt.xlabel('Test ids')    
    ax.set_ylabel('Capacity (mAh)')
    ax.set_xlabel('Test ids')
    plt.yticks(rotation=45)
    plt.title('Capacity evolution')
    return fig

def voltage_chart(dfs):
    fig, ax = plt.subplots(figsize=(15,8))
    n = len(dfs)  # e.g. 71
    colors = plt.cm.tab20c(np.linspace(0, 1, n))  # pick n distinct colors from colormap
    for i,df in enumerate(dfs) :
        ax.plot(df['Time'],df['Voltage_measured'], label=f'Test {i}',color=colors[i])
        
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Voltage (V)')
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    ax.set_title('Voltage trends over cycles')
    plt.show()
    return fig 

def current_chart(dfs):
    fig, ax = plt.subplots(figsize=(15,8))
    n = len(dfs)  # e.g. 71
    colors = plt.cm.tab20c(np.linspace(0, 1, n))  # pick n distinct colors from colormap
    for i,df in enumerate(dfs) :
        ax.plot(df['Time'],df['Current_measured'], label=f'Test {i}',color=colors[i])
        
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Current (A)')
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    ax.set_title('Current trends over cycles')
    plt.show()
    return fig 

def tamb_charts(dfs):  
    fig, ax = plt.subplots(figsize=(15,8))
    n = len(dfs)  # e.g. 71
    colors = plt.cm.tab20c(np.linspace(0, 1, n))  # pick n distinct colors from colormap
    for i,df in enumerate(dfs) :
        ax.plot(df['Time'],df['Temperature_measured'], label=f'Test {i}',color=colors[i])
        
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    ax.set_title('Temperature trends over cycles')
    plt.show()
    return fig 

def capacity_comparision_charts(df):
    df['Precomputed Capacity'] = pd.to_numeric(df['Precomputed Capacity'])
    fig, ax = plt.subplots(figsize=(10,6))
    plt.plot(df['test_id'],df['Precomputed Capacity'], label='Precomputed Capacity')
    plt.plot(df['test_id'],df['Computed Capacity'], label='Computed Capacity')
    plt.xlabel('Test ids')    
    ax.set_ylabel('Capacity (mAh)')
    ax.set_xlabel('Test ids')
    ax.legend()
    plt.yticks(rotation=45)
    plt.title('Capacity Comparison')
    return fig