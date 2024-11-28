import pandas as pd
import matplotlib.pyplot as plt

# Function to load and process the data from the CSV file
def load_and_process_data(csv_file):
    # Load the CSV data into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Filter for rows where the 'type' corresponds to step count data
    df = df[df['type'] == 'HKQuantityTypeIdentifierStepCount']

    # Convert the 'startDate' column to datetime
    df['startDate'] = pd.to_datetime(df['startDate'])

    # Exclude data before 2023
    df = df[df['startDate'].dt.year >= 2023]

    # Extract the date (without time) from the 'startDate'
    df['date'] = df['startDate'].dt.date

    # Convert the 'value' column to numeric (step count)
    df['value'] = pd.to_numeric(df['value'], errors='coerce')

    # Group by date and sum the step counts for each day
    daily_steps = df.groupby('date')['value'].sum().reset_index()

    return df, daily_steps

# Function to calculate monthly average steps
def calculate_monthly_average(df):
    # Extract year and month from the 'startDate' for monthly grouping
    df['year_month'] = df['startDate'].dt.to_period('M')

    # Group by year-month and calculate the average steps for each month
    monthly_average_steps = df.groupby('year_month')['value'].mean().reset_index()

    return monthly_average_steps

# Function to plot the daily step count
def plot_daily_steps(daily_steps):
    plt.figure(figsize=(10, 6))
    plt.plot(daily_steps['date'], daily_steps['value'], marker='o', linestyle='-', color='b')
    plt.title('Daily Step Count (2023 and Later)', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Steps', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Function to plot the monthly average step count
def plot_monthly_average_steps(monthly_average_steps):
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_average_steps['year_month'].astype(str), monthly_average_steps['value'], marker='o', linestyle='-', color='g')
    plt.title('Monthly Average Step Count (2023 and Later)', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Average Steps', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main function to load, process, and plot the data
def main(csv_file):
    # Load and process the data
    df, daily_steps = load_and_process_data(csv_file)

    # Plot daily steps
    plot_daily_steps(daily_steps)

    # Calculate and plot monthly averages
    monthly_average_steps = calculate_monthly_average(df)
    plot_monthly_average_steps(monthly_average_steps)

# Example usage
csv_file = 'apple_health_data.csv'  # Path to your converted CSV file

# Run the main function
main(csv_file)
