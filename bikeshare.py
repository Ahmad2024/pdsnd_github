import time
import datetime
import pandas as pd
import numpy as np
import statistics as st

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello user! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
    #lower is used to get input in any format

    while(True):
        if(city == 'chicago' or city == 'new york' or city == 'washington' or city == 'all'):
            break
        else:
            city = input('Enter Correct city: ').lower()
            
    # get user input for month (all, january, february, ... , june)
    month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()

    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Enter valid month\n').lower()
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day =  input('Which day ? monday, tuesday, wednesday, thursday, friday, saturday , sunday or all to display data of all days?\n').lower()

    while(True):
        
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Enter Correct day: ').lower()

    #return day

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
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

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)


    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    df = df.drop(['month', 'day_of_week'], axis = 1)
    row_index = 0

    see_data = input("\nYou like to see rows of the data used to compute the stats? Kindly write 'yes' or 'no' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see five more rows of the data used to compute the stats? Kindly write 'yes' or 'no' \n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
