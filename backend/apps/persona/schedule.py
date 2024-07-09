import numpy as np
import pandas as pd
import random

# Define constraints
work_hours_per_week = 40
min_block_hours = 4
max_block_hours = 8

# Define time blocks
def create_time_blocks(activity, total_hours, min_block, max_block):
    """
    Generate a list of time blocks for a given activity based on the total number of hours needed.
    
    Parameters:
    activity (str): The name of the activity.
    total_hours (int): The total number of hours needed for the activity.
    min_block (int): The minimum number of hours for each block.
    max_block (int): The maximum number of hours for each block.
    
    Returns:
    list: A list of time blocks representing the distribution of hours.
    """
    blocks = []
    remaining_hours = total_hours
    while remaining_hours > 0:
        block_hours = min(random.randint(min_block, max_block), remaining_hours)
        blocks.append(block_hours)
        remaining_hours -= block_hours
    return blocks

# Assign blocks to the schedule
def assign_blocks_to_schedule(schedule, blocks, activity, possible_hours, days_of_week, daily=False):
    """
    Assigns blocks of time for a specific activity to a schedule DataFrame based on available hours.

    Parameters:
    schedule (pd.DataFrame): The DataFrame representing the schedule with a datetime index.
    blocks (list): A list of integers where each integer represents the duration of a block in hours.
    activity (str): The name of the activity to be scheduled.
    possible_hours (list): A list of integers representing possible start hours for the activity blocks.
    days_of_week (list): A list of days the activity can happen 0 - Mon, 1 - Tue etc.
    daily (bool, optional): If True, the activity is scheduled daily at the same time. Defaults to False.

    Returns:
    pd.DataFrame: The updated schedule DataFrame with the activity blocks assigned.
    """
    for block in blocks:
        attempts = 0
        max_attempts = 100  # Prevent infinite loop
        
        while attempts < max_attempts:
            if daily:
                start_hour = random.choice(possible_hours)
                for start_day in range(7):
                    start_time = schedule.index[(schedule.index.dayofweek == start_day) & (schedule.index.hour == start_hour)].min()
                    end_time = start_time + pd.Timedelta(hours=block)
                    if end_time.date() != start_time.date():  # Adjust to fit within the day
                        end_time = start_time + pd.Timedelta(hours=block)
                    if schedule.loc[start_time:end_time, 'Activity'].isnull().all():
                        schedule.loc[start_time:end_time - pd.Timedelta(minutes=15), 'Activity'] = activity
                        print(f"Assigned {activity} block from {start_time} to {end_time} every day")
                        break
            else:
                start_day = random.choice(days_of_week)
                start_hour = random.choice(possible_hours)
                potential_start_times = schedule.index[(schedule.index.dayofweek == start_day) & (schedule.index.hour == start_hour)]
                if not potential_start_times.empty:
                    start_time = potential_start_times.min()
                    end_time = start_time + pd.Timedelta(hours=block)
                    if end_time.date() != start_time.date():  # Adjust to fit within the day
                        end_time = pd.Timestamp(year=start_time.year, month=start_time.month, day=start_time.day, hour=23, minute=59)
                    if schedule.loc[start_time:end_time, 'Activity'].isnull().all():
                        schedule.loc[start_time:end_time - pd.Timedelta(minutes=15), 'Activity'] = activity
                        break
            attempts += 1
        if attempts == max_attempts:
            print(f"Could not place a {block}-hour block for {activity}.")
            break
    return schedule  # Return the modified DataFrame

# Assign sleep blocks specifically to handle spanning days
# We do this first and fill in the other activities around it
def assign_sleep_blocks(schedule: pd.DataFrame, min_block: int, max_block: int):
    """
    Assigns sleep blocks to the schedule DataFrame for each day of the week.

    Parameters:
    schedule (pd.DataFrame): The schedule DataFrame where sleep blocks will be assigned.
    min_block (int): The minimum number of hours for a sleep block.
    max_block (int): The maximum number of hours for a sleep block.

    Returns:
    pd.DataFrame: The updated schedule DataFrame with sleep blocks assigned.
    """
    # NB / Issue: There is an assumption this is for 7 days
    for day in range(7):
        if day == 0:
            # For the first day, calculate sleep from 00:00 to the morning
            block_hours = random.randint(min_block, max_block)
            start_time = schedule.index[0]
            end_time = start_time + pd.Timedelta(hours=block_hours)
            schedule.loc[start_time:end_time - pd.Timedelta(minutes=15), 'Activity'] = 'Sleep'
            # print(schedule.loc[start_time:end_time - pd.Timedelta(minutes=15)])  # Debug statement to verify assignment
        else:
            start_hour = random.choice(list(range(22, 24)))  # Start sleep between 10 PM and midnight
            start_time = schedule.index[(schedule.index.dayofweek == day) & (schedule.index.hour == start_hour)].min()
            block_hours = random.randint(min_block, max_block)
            end_time = start_time + pd.Timedelta(hours=block_hours)
            
            if end_time.date() != start_time.date():  # If the sleep block spans into the next day
                span_end_time = pd.Timestamp(end_time.date())  # Midnight of the next day
                schedule.loc[start_time:span_end_time - pd.Timedelta(minutes=15), 'Activity'] = 'Sleep'
                next_day_start_time = span_end_time
                next_day_end_time = end_time
                schedule.loc[next_day_start_time:next_day_end_time - pd.Timedelta(minutes=15), 'Activity'] = 'Sleep'
                # print(f"Assigned Sleep block from {start_time} to {span_end_time - pd.Timedelta(minutes=15)} and from {next_day_start_time} to {next_day_end_time - pd.Timedelta(minutes=15)}")
            else:
                schedule.loc[start_time:end_time - pd.Timedelta(minutes=15), 'Activity'] = 'Sleep'
                # print(f"Assigned Sleep block from {start_time} to {end_time - pd.Timedelta(minutes=15)}")
            # print(schedule.loc[start_time:end_time - pd.Timedelta(minutes=15)]) 
    
    return schedule # Debug statement to verify assignment

def fill_remaining_slots(schedule: pd.DataFrame, activity: str) -> pd.DataFrame:
    """
    Fills all remaining unassigned slots in the schedule with the specified activity.

    Parameters:
    schedule (pd.DataFrame): The schedule DataFrame.
    activity (str): The name of the activity to fill in the remaining slots.

    Returns:
    pd.DataFrame: The updated schedule DataFrame with the remaining slots filled.
    """
    schedule.fillna({'Activity': activity }, inplace=True)
    return schedule

def define_activities(work_hours_per_week, min_block_hours, max_block_hours):
    """
    Defines activities and their constraints.

    Parameters:
    work_hours_per_week (int): Total hours dedicated to work per week.
    min_block_hours (int): Minimum block hours for activities.
    max_block_hours (int): Maximum block hours for activities.

    Returns:
    dict: A dictionary of activities with their respective constraints.
    """
    activities = {
        'Sleep': {'total_hours': 56, 'min_block': 7, 'max_block': 10, 'possible_hours': list(range(22, 24)) + list(range(0, 8)), 'daily': True, 'priority': 1, 'days_of_week': list(range(7))},
        'Work': {'total_hours': work_hours_per_week, 'min_block': min_block_hours, 'max_block': max_block_hours, 'possible_hours': list(range(9, 17)), 'daily': False, 'priority': 2, 'days_of_week': [0, 1, 2, 3, 4]},  # Monday to Friday
        'School': {'total_hours': 20, 'min_block': min_block_hours, 'max_block': max_block_hours, 'possible_hours': list(range(8, 16)), 'daily': False, 'priority': 3, 'days_of_week': [0, 1, 2, 3, 4]},  # Monday to Friday
        'Activities': {'total_hours': 30, 'min_block': 1, 'max_block': 3, 'possible_hours': list(range(6, 22)), 'daily': False, 'priority': 4, 'days_of_week': list(range(7))},  # Every day
        'Leisure': {'total_hours': 0, 'min_block': 0, 'max_block': 0, 'possible_hours': list(range(0, 24)), 'daily': False, 'priority': 5, 'days_of_week': list(range(7))}  # Every day
    }

    return activities


def assign_state_probs(schedule, activities):

    # Sort activities by priority
    sorted_activities = sorted(activities.items(), key=lambda x: x[1]['priority'])

    # Assign sleep blocks first to ensure daily sleep
    schedule = assign_sleep_blocks(schedule, activities['Sleep']['min_block'], activities['Sleep']['max_block'])

    # Assign blocks for each activity based on priority, skipping sleep as it is already assigned
    for activity, constraints in sorted_activities:
        if activity == 'Sleep':
            continue

        blocks = create_time_blocks(activity, constraints['total_hours'], constraints['min_block'], constraints['max_block'])
        schedule = assign_blocks_to_schedule(schedule, blocks, activity, constraints['possible_hours'], constraints['days_of_week'], constraints['daily'])

    # Fill the rest of the schedule with the 'Leisure' activity
    schedule = fill_remaining_slots(schedule, 'Leisure')

    state_probs = {
        'Work': {'Online': 0.1, 'Offline': 0.1, 'Busy': 0.7, 'Away': 0.1},
        'School': {'Online': 0.2, 'Offline': 0.1, 'Busy': 0.5, 'Away': 0.2},
        'Sleep': {'Online': 0.05, 'Offline': 0.9, 'Busy': 0.05, 'Away': 0.0},
        'Activities': {'Online': 0.3, 'Offline': 0.1, 'Busy': 0.2, 'Away': 0.4},
        'Leisure': {'Online': 0.3, 'Offline': 0.3, 'Busy': 0.2, 'Away': 0.2},  # Add state probabilities for 'Leisure'
        None: {'Online': 0.4, 'Offline': 0.2, 'Busy': 0.2, 'Away': 0.2}
    }


    schedule = assign_states_to_schedule(schedule, state_probs)
    return schedule


def assign_states_to_schedule(schedule, state_probs):
    for idx, row in schedule.iterrows():
        activity = row['Activity']
        if pd.isna(activity):  # Only assign states if the activity is NaN
            activity = None
            state = np.random.choice(list(state_probs[activity].keys()), p=list(state_probs[activity].values()))
            schedule.at[idx, 'State'] = state
        else:
            # Preserve the current activity's state assignment
            state = np.random.choice(list(state_probs[row['Activity']].keys()), p=list(state_probs[row['Activity']].values()))
            schedule.at[idx, 'State'] = state
    return schedule


def get_next_state(schedule: pd.DataFrame, reference_date_time: pd.Timestamp, state: str) -> pd.Series:
    """
    Queries the schedule DataFrame and returns the next state of a given type after the reference date and time.

    Parameters:
    schedule (pd.DataFrame): The schedule DataFrame.
    reference_date_time (pd.Timestamp): The reference date and time to start the search.
    state (str): The state to search for.

    Returns:
    pd.Series: The next state found after the reference date and time.
    """
    # Filter the schedule for rows after the reference date and time
    future_schedule = schedule[schedule.index > reference_date_time]
    
    # Filter for the specified state
    next_state = future_schedule[future_schedule['State'] == state]
    
    # Return the first occurrence of the state
    if not next_state.empty:
        return next_state.iloc[0]
    else:
        return None

if __name__ == '__main__':

    work_hours_per_week = 20
    min_block_hours = 4
    max_block_hours = 8

    # Define time slots for a week in 15-minute intervals
    time_slots = pd.date_range(start='2024-06-01', periods=24*7*4, freq='15min')

    # Initialize DataFrame to hold the schedule
    schedule = pd.DataFrame(index=time_slots, columns=['Activity', 'State'])
    
    activities = define_activities(work_hours_per_week, min_block_hours, max_block_hours)
    
    schedule = assign_state_probs(schedule, activities)

    # Resample the DataFrame to 15-minute intervals
    schedule = schedule.resample('1h').asfreq()

    # Display the schedule
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        schedule_display = schedule.copy()
        print(schedule_display)

    # Reference date and time
    reference_date_time = pd.Timestamp('2024-06-03 08:00')

    # Get the next state
    next_state = get_next_state(schedule, reference_date_time, 'Online')
    print(next_state)