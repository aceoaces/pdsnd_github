import time
import pandas as pd


CITY_DATA = {'chicago': "chicago.csv",
             'new york city': "new_york_city.csv",
             'washington': "washington.csv"}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
        or "none" to apply no month filter
        (str) day - name of the day of week to filter by,
         or "None" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington).
    city = get_city()

    month = get_month()

    day = get_day()

    print('-'*40)
    return city, month, day


def get_city():
    city = input('Which city you would like to explore, Chicago, Washington '
                 'or New York City\n').lower()

    if city not in CITY_DATA.keys():
        print("Sorry I am not sure which city you are reffering to\n"
              "Let\'s try again")
        return get_city()
    else:
        return city


def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        (str) String representation of month, e.g. for January it returns 'jan'
    '''
    month = input('\nWould you like to filter the data by month.\n'

                  'If yes then type the month name as Jan, Feb, Mar, Apr, May,'
                  'Jun. Type None for no filter\n'
                  'Data available from January to June only\n').lower()

    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'none']

    if month not in months:
        print('\nHumm.....sorry, I don\'t get by which month you want data to '
              'If yes then type the month,\n'
              'for e.g, jan as january. Type none for no filter.\n'
              'Data available from January to June only\n').title()
    else:
        return month


def get_day():
    '''
        Ask the user for day of the week and return specified day
    Args:
        none
    Returns:
        (Str)String representation of day like sun for Sunday
    '''
    day_of_week = input('\nWould you like to filter the data by month.\n'
                        'If yes then type the day names as Sunday, Monday,\n'
                        'Tuesday, Wednesday, Thursday, Friday, Saturday\n'
                        'Type None for no filter\n').title()

    weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
             'Friday', 'Saturday', 'Sunday', 'None']

    if day_of_week not in weeks:
        print('\nI\'m sorry, I\'m not sure which day of the week\n'
              'you\'re trying to filter by. Let\'s try again.')
        return get_day()
    else:
        return day_of_week


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if
    applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no
                      month filter
        (str) day - name of the day of week to filter by, or "none" to apply
                    no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'none':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'None':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # display the most common month
        print('Most common month of trevelling, month in  int')
        common_month = df['month'].mode()[0]
        print(common_month)
        print('-' * 40)
        print(" " * 40)

        # display the most common day of week
        print('Most common day of the week of travelling')
        day_of_week = df['day_of_week'].mode()[0]
        print(day_of_week)
        print('-' * 40)
        print(' ' * 40)

        # display the most common start hour
        print('Most common start hour')
        df['hour'] = df['Start Time'].dt.hour
        common_hour = df['hour'].mode()[0]
        print(common_hour)
        print('-' * 40)
        print(' ' * 40)

    except Exception as e:
        print('Sorry we could not calculate'
              'this stat because of {}'.format(e))
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('*'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    try:
        # display most commonly used start station
        print('Most commonly used start station')
        start_station = df['Start Station'].mode()[0]
        print(start_station)
        print('-' * 40)
        print(' ' * 40)

        # display most commonly used end station
        print('Most commonly used end station')
        end_station = df['End Station'].mode()[0]
        print(end_station)
        print('-' * 40)
        print(' ' * 40)

        # display most commonly used end station
        print('Most commonly used end station')
        end_station = df['End Station'].mode()[0]
        print(end_station)
        print('-' * 40)
        print(' ' * 40)

        # display most frequent combination of start station and end station
        # trip
        print('Most frequent combination of start station'
              'and end station trip')
        x = df.groupby(['Start Station'])["End Station"].unique().mode()[0]
        print(x)
        print('-' * 40)
        print(' ' * 40)
    except Exception as e:
        print('Sorry we could not calculate'
              'this stat because of {}'.format(e))
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('*'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    try:
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()
        print('-' * 40)
        print(' ' * 40)

        # display total travel time
        print("Total time travel")
        total_travel = int(df['Trip Duration'].sum())
        print(total_travel)
        print('-' * 40)
        print(' ' * 40)

        # display mean travel time
        print('Mean travel time')
        mean_travel = int(df['Trip Duration'].mean())
        print(mean_travel)
        print('-' * 40)
        print(' ' * 40)

    except Exception as e:
        print('Sorry we could not calculate'
              'this stat because of {}'.format(e))
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('*'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # Display counts of user types
        print('Count of user types')
        user_type = df['User Type'].value_counts()
        print(user_type)
        print('-' * 40)
        print(' ' * 40)

        # Display counts of gender
        print('Count of gender')
        gender_count = df['Gender'].value_counts()
        print(gender_count)
        print('-' * 40)
        print(' ' * 40)

        # Display earliest, most recent, and most common year of birth
        # Earliest Birth Year
        print('Earliest Birth Year')
        earliest_birth = int(df['Birth Year'].min())
        print(earliest_birth)
        print('-' * 40)
        print(' ' * 40)

        # Most recent Birth year
        print('Most recent Birth Year')
        most_recent = int(df['Birth Year'].max())
        print(most_recent)
        print('-' * 40)
        print(' ' * 40)

        # Most Common Birth Year
        print('Most Common Birth Year')
        most_common = int(df['Birth Year'].mode())
        print(most_common)
        print('-' * 40)
        print(' ' * 40)
    except KeyError:
        print("There is no Birth Year and Gender Data")
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('*'*40)


def display_data(df, current_line):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five
    more.
    Continues asking until they say stop.
    Args:
        df: dataframe of bikeshare data
    Returns:
        If the user says yes then this function returns the next five lines
            of the dataframe and then asks the question again by calling this
            function again (recursive)
        If the user says no then this function returns, but without any value
    '''
    display = input('\nWould you like to view individual trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    display = display.lower()
    if display == 'yes':
        print(df.iloc[current_line: current_line + 5])
        current_line += 5
        return display_data(df, current_line)
    if display == 'no':
        return
    else:
        print('\nI\'m sorry, I\'m not sure if you wanted'
              ' to see more data or not.\n'
              'Let\'s try again.')
        return display_data(df, current_line)


def main():
    try:
        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_data(df, 0)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                print("Exiting")
                break

    except KeyboardInterrupt:
        print("Exiting")


if __name__ == "__main__":
    main()
