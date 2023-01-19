# The following are websites I used for bike share.

# https://pandas.pydata.org/pandas-docs/version/0.17.0/

# https://www.w3schools.com/python/default.asp

# https://docs.python.org/3/library/index.html

import time
import pandas as pd
import numpy as np

# import files

CITY_DATA =  {'chicago': '/users/scros/PycharmProjects/pythonProject/Udacitybikeshare/chicago.csv',
             'new york city': '/users/scros/PycharmProjects/pythonProject/Udacitybikeshare/new_york_city.csv',
             'washington': '/users/scros/PycharmProjects/pythonProject/Udacitybikeshare/washington.csv'}

# Create lists for user input

#MONTH_DATA =['january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'all']

#DAY_DATA =['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, and washington). HINT: Use a while loop to handle invalid inputs

    cities = ['chicago', 'new york city', 'washington']

    while True:
        city = input('Please enter city: chicago, new york city, or washington. \n').lower()
        if city not in cities:
            print('\nInvalid input. Please try again\n')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    while True:
        month = input('Please enter month: january, february, march, april, may, june, all. \n').lower()
        if month not in months:
            print('\nInvalid input. Please try again\n')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    while True:
        day = input('Please enter day: sunday, monday, tuesday, wednesday, thursday, friday, saturday, all \n').lower()
        if day not in days:
            print('\nInvalid input. Please try again\n')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        MONTHS = ("january", "february", "march", "april", "may", "june")
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].mode()[0]
    print('Most Common Month is: ', most_common_month)

    # display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week is: ', most_common_day)

    # display the most common start hour

    most_common_hour = df['hour'].mode()[0]
    print('Most common Start Hour of Day is: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most common used start station

    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station is: ', most_common_start_station)

    # display most common used end station

    most_common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station is: ', most_common_end_station)

    # display most frequent combination of start station and end station trip

    combination_group = df.groupby(['Start Station', 'End Station'])
    most_frequent_combination_station = combination_group.size().sort_values(ascending=False).head(1)
    print('Most frequestn combination of Start Station and End Station trip is: ', most_frequent_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is: ', total_travel_time)

    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
# Washington is missing gender and birth year used try and except to correct
    try:
        # Display counts of user types
        user_type = df['User Type'].value_counts()
        print('Count of users by type:{} \n', user_type)

        # Display counts of gender
        gender = df['Gender'].value_counts()
        print('Gender count: ', gender)

        # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('Earliest Year is: ', earliest_year)

        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year is ', most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year is: ', most_common_year)

    except KeyError:
        print('No data available for the selected city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#view raw data to user
def show_raw_data(df):
    row=0
    while True:
        show_raw_data = input("\nIf your would like to view the raw data please enter 'y' for yes, 'n' for no.\n").lower()
        if show_raw_data == 'y':
            print(df.iloc[row : row + 5])
            row += 5
        elif show_raw_data == 'n':
            break
        else:
            print('\nInvalid input. Please try again\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
