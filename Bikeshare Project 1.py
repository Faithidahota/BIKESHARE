#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',200)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" 
     """
    
    print('Hello! let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    available_cities = ['chicago', 'washington', 'new york city']
    while True:
        city = input("which city would you like to analyse? please enter chicago, washington or new york city\n").lower()
        if city in available_cities:
            break
        else:
            print("You entered an invalid city")
    
    
    # TO DO: get user input for month (all, january, february, 'march', 'april', 'may', 'june')
    months_avaliable = ['january', 'febuary', 'march', 'april', 'may', 'june']
    month_choice = input("would you like to analyse all months? if all, please enter yes and enter any other thing for specfic month\n").lower()
    if month_choice == 'yes':
          month = 'all'
    else:
        while True:
            month = input("which month do you want to analyse from january, febuary, 'march', 'april', 'may', 'june'\n").lower
            if month in months_available:
                break
            else:
                print("you entered an invalid month")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_choice = input("do you want to anlyse all days of the week or a specific day? if all, please enter yes and enter anything for specific month\n").lower()
    if day_choice == 'yes':
        day = 'all'
    else:
        while True:
            try:
                day = int( input('which day would you like to analyse? please enter 1 for sunday, 2 for monday, 3 for tuesday, 4 for wednesday, 5 for thursday, 6 for friday, 7 for saturday\n'))
                if 1 < day < 7:
                    break
                else:
                    print('out of range')
            except:
                print('You entered an invalid month')
            


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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Week Day'] = df['Start Time'].dt.day
    df['Hour'] = df['Start Time'].dt.hour
    month_index = {'january':1, 'febuary':2, 'march':3, 'april':4, 'may':5, 'june':6}
    if month != 'all':
        df = df.loc[df['month'] == mon_index[month]]
    if day != 'all':
        day -= 1
        df = df.loc[df['Week Day'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()
    print(most_month)


    # TO DO: display the most common day of week
    most_weekday = df['Week Day'].mode()
    print(most_weekday)


    # TO DO: display the most common start hour
    most_hour = df['Hour'].mode()
    print(most_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()
    print(most_start_station)
    


    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode
    print(most_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station'] + "_" + df['End Station']
    most_start_station = df


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum()
    print(total_tt)


    # TO DO: display mean travel time
    average_tt = df['Trip Duration'].mean() 
    print(average_tt)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print(user_count)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print("Gender data not available")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yob = df['Birth Year'].min()
        print(earliest_yob)
        most_recent_yob = df['Birth Year'].max()
        print(most_recent_yob)
        most_common_yob = df['Birth Year'].mode()
        print(most_common_yob) 
    else:
        print('No data available for birth year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
              

def see_data(df):
    view_data = input("Do you want to view the first five lines or raw data? enter yes or no\n").lower() 
    if view_data == 'yes':
        i = 0
        while 0 < 1:
            print(df.loc[i:i + 5])
            i+=5
            see_more = input("Do you want to view the next 5 lines?\n").lower()
            if see_more != 'yes':
                break
        
               

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()import time
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',200)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" 
     """
    
    print('Hello! let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    available_cities = ['chicago', 'washington', 'new york city']
    while True:
        city = input("which city would you like to analyse? please enter chicago, washington or new york city\n").lower()
        if city in available_cities:
            break
        else:
            print("You entered an invalid city")
    
    
    # TO DO: get user input for month (all, january, february, 'march', 'april', 'may', 'june')
    months_avaliable = ['january', 'febuary', 'march', 'april', 'may', 'june']
    month_choice = input("would you like to analyse all months? if all, please enter yes and enter any other thing for specfic month\n").lower()
    if month_choice == 'yes':
          month = 'all'
    else:
        while True:
            month = input("which month do you want to analyse from january, febuary, 'march', 'april', 'may', 'june'\n").lower
            if month in months_available:
                break
            else:
                print("you entered an invalid month")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_choice = input("do you want to anlyse all days of the week or a specific day? if all, please enter yes and enter anything for specific month\n").lower()
    if day_choice == 'yes':
        day = 'all'
    else:
        while True:
            try:
                day = int( input('which day would you like to analyse? please enter 1 for sunday, 2 for monday, 3 for tuesday, 4 for wednesday, 5 for thursday, 6 for friday, 7 for saturday\n'))
                if 1 < day < 7:
                    break
                else:
                    print('out of range')
            except:
                print(' You entered an invalid month')
            


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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Week Day'] = df['Start Time'].dt.day
    df['Hour'] = df['Start Time'].dt.hour
    month_index = {'january':1, 'febuary':2, 'march':3, 'april':4, 'may':5, 'june':6}
    if month != 'all':
        df = df.loc[df['month'] == mon_index[month]]
    if day != 'all':
        day -= 1
        df = df.loc[df['Week Day'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()
    print(most_month)


    # TO DO: display the most common day of week
    most_weekday = df['Week Day'].mode()
    print(most_weekday)


    # TO DO: display the most common start hour
    most_hour = df['Hour'].mode()
    print(most_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()
    print(most_start_station)
    


    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode
    print(most_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station'] + "_" + df['End Station']
    most_start_station = df


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = df['Trip Duration'].sum()
    print(total_tt)


    # TO DO: display mean travel time
    average_tt = df['Trip Duration'].mean() 
    print(average_tt)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print(user_count)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print("Gender data not available")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_yob = df['Birth Year'].min()
        print(earliest_yob)
        most_recent_yob = df['Birth Year'].max()
        print(most_recent_yob)
        most_common_yob = df['Birth Year'].mode()
        print(most_common_yob) 
    else:
        print('No data available for birth year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
              

def see_data(df):
    view_data = input("Do you want to view the first five lines or raw data? enter yes or no\n").lower() 
    if view_data == 'yes':
        i = 0
        while 0 < 1:
            print(df.loc[i:i + 5])
            i+=5
            see_more = input("Do you want to view the next 5 lines?\n").lower()
            if see_more != 'yes':
                break
        
               

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

