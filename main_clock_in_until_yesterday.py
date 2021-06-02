from factorial.exceptions import AuthenticationTokenNotFound, ApiError, UserNotLoggedIn
from factorial.factorialclient import FactorialClient
from factorial.loader import JsonCredentials, JsonWork
from datetime import date, timedelta, datetime
import random

settings_file = 'factorial_settings.json'

if __name__ == '__main__':
    try:
        # Get last month and year
        now = datetime.now()
        month = now.month - 1 if now.month > 1 else 12
        year = now.year if month < 12 else now.year -1
        
        # Set the factorial client
        client = FactorialClient.load_from_settings(JsonCredentials(settings_file))
                
        # my personal period id
        period_id = client.get_period_id(year, month)
        
        # gets my current shifts for a particular month and year
        my_shift = client.get_shift(year, month)

        # get the working days til yesterday
        working_days_until_yesterday = client.get_calendar_until_yesterday(year, month, is_leave=False, is_laborable=True)
        
        #clock in all the missing days til yesterday
        client.clock_in_until_yesterday(JsonWork(settings_file), period_id, my_shift, working_days_until_yesterday)  
        
    except AuthenticationTokenNotFound as err:
        print(f"Can't retrieve the login token: {err}")
    except UserNotLoggedIn as err:
        print(f'User not logged in: {err}')
    except ApiError as err:
        print(f"Api error: {err}")
