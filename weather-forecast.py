#!/usr/bin/env python3
import python_weather

import argparse
import asyncio
import os

async def print_weather_forecast(city):
  async with python_weather.Client(unit=python_weather.METRIC) as client:

    # Fetch weather forecast
    weather = await client.get(city)

    print("Current Temperature in {}: {}°C".format(city, weather.temperature))
    
    # Get the weather forecast for three days
    for daily in weather:
      print("\n{}".format(daily.date))
      
      # Hourly forecasts (every 3 hours)
      for hourly in daily:
        print(f'- {hourly.time} - {hourly.temperature}°C and {hourly.description}')

def main():
    parser=argparse.ArgumentParser()

    parser.add_argument("--city", default="Kiel", help="Name of city for weather forecast")

    args=parser.parse_args()
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
    asyncio.run(print_weather_forecast(args.city))
  

if __name__ == '__main__':
    main()