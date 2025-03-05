# Strava HR Aggregator
The Strava HR Aggregator tabulates time spent at heart rate across multiple activities. It was developed to simplify the process of tracking time spent at heart rate for those of us that train off a heart rate monitor

Because of strava call limits, I'm only using this to append the last 1-2 weeks of training to a separate log at this time

## Setup
When setting up the repo change the name of 'example_cofig.txt' to '.env', and populate the client id and client secret from Strava 

## Usage
You can [Get Started with the Strava API here](https://developers.strava.com/docs/getting-started/)  
This is built with [Strava Lib which can be found here](https://stravalib.readthedocs.io/en/v2.1/index.html)

## Roadmap
Future versions may  
-improve token generation process  
-include graphing/plotting of trends  
-contain an integrated "database" to connect directly to a larger global workout log

## License
[MIT](https://choosealicense.com/licenses/mit/)