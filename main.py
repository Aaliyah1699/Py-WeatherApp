from weather_api import get_weather, get_weather_details
from model import Weather


def main():
    while True:
        # Ask the user for their city
        user_city: str = input('Enter a city: ')

        # Get the current weather details
        current_weather: dict = get_weather(user_city, mock=False)
        if current_weather:
            try:
                weather_details: list[Weather] = get_weather_details(current_weather)
            except Exception as e:
                print("Error:", e)
                print("Please try another city.")
                continue

            # Get the current days
            dfmt: str = '%m/%d/%y'
            days: list[str] = sorted({f'{date.date:{dfmt}}' for date in weather_details})

            for day in days:
                print(day)
                print('----')

                # Group the weather data by date
                grouped: list[Weather] = [current for current in weather_details if f'{current.date:{dfmt}}' == day]
                for element in grouped:
                    print(element)

                print()  # Space
            break
        else:
            choice = input("Do you want to try another city? (yes/no): ")
            if choice.lower() != 'yes':
                break


if __name__ == '__main__':
    main()
