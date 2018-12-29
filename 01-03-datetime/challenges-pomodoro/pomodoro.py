import time
from datetime import datetime, timedelta


POMODORO_DURATION_MIN = 50


def main():
    print(f'{POMODORO_DURATION_MIN} Minutes Pomodoro Started now!!!')
    print(f'Started at: {datetime.now()}')

    pomodoro_duration = POMODORO_DURATION_MIN / 60
    ended_time = datetime.now() + timedelta(hours=pomodoro_duration)

    ticking = True
    while ticking:
        current_time = datetime.now()
        seconds_left = (ended_time - current_time).seconds

        if seconds_left is 0:
            ticking = False

        time_left_minute = int(seconds_left / 60)
        time_left_second = seconds_left % 60

        if time_left_second is 0 and time_left_minute is not 0:
            tick_or_tock = 'Tick'

            if time_left_minute % 2 is 0:
                tick_or_tock = 'Tock'

            time_left = f'{time_left_minute}:{time_left_second}'
            print(f'{tick_or_tock}: {time_left} minutes left')

        time.sleep(1)

    print('Pomodoro Ended!!!')
    print(f'Ended at: {datetime.now()}')


main()
