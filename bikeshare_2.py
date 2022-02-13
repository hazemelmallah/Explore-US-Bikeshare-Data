import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please enter the name of the city as (chicago, new york city, washington): ").lower()
    cities = ['new york city', 'washington', 'chicago']

    while city not in cities:
        city = input("please enter again a name of a city of chicago or new york city or washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june) 
    month = input("please enter the month from january to june (eg.june) or all: ").lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    while month not in months:
        month = input("please enter again a month from january to june (eg.may) or all: ").lower()

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please enter day of a week (eg.monday) or all: ").lower()
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    while day not in days:
        day = input("please enter again a day of week (eg.monday)or all: ").lower()

    print('-' * 40)
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if month != 'all':
        df = df[df['day'] == day.title()]

    return df


def display_data(df):
    k = 0
    ans = input("Would you like to view 5 rows of individual trip data? Enter yes or no: ").lower()

    while True:
        if ans == 'yes':
            print(df.iloc[k:k + 5])
            k += 5
            ans = input("Do you wish to continue?: ").lower()
        else:
            break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common month: ', most_common_month)
    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('most common day: ', most_common_day)
    # TO DO: display the most common start hour
    most_common_start_hour = df['Start Time'].mode()[0]
    print('most common start hour: ', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('most common start station: ', most_common_start_station)
    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('most common end station: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_of_start_and_end_stations = (df['Start Station'] + ' & ' + df['End Station']).mode()[0]
    print('combination of start and end stations: ', combination_of_start_and_end_stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('total trip duration: ', total_trip_duration)
    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('average trip duration: ', average_trip_duration)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('counts of user types: ', user_type)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Gender: ', gender)
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        print('most common year of birth: ', most_common_year_of_birth)
        most_recent = df['Birth Year'].max()
        print('most recent birth year: ', most_recent)
        earliest = df['Birth Year'].min()
        print('earliest birth year: ', earliest)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

