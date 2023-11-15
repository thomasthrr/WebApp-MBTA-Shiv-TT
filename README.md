# WebApp-MBTA
 This is the base repository for Web App Developement project. Please read [instructions](instructions.md). 

# Key Learnings and Takeaways - Shivant Malkani, Thomas Thiry

### Project Overview

In this Project we learned how to utilize MapBox API, MBTA API, and OPEN WEATHER API to pull information from these sources and output the closest bus stop, longitude, latitude, nearest station, wheelchair accessibility and weather temperature give user input of a location in massachussets. Using Flask, we created a webpage that allows the user to interact buttons to submit their location and see the output with different color schemes.

### Reflection

The entire process involved developing Python scripts utilizing APIs for location-based services and weather data. The team effectively established a solid project scope, focusing on integrating various APIs and handling data retrieval. However, there were challenges, such as insufficient error handling and limited testing. A more robust testing strategy would include error notifications to the user when the API could not pull the nearest bus stop, or if the API did not have sufficient data on wheelchair accessibility. 

Shivant was trying to debugg the backend for a long period of team when he realized that his error was actually in the config file, where he was missing one number (2) at the end of the Open Weather API key. 
Thomas initially struggled with the frontend and wheelchair accessibility, and making the connection with the backend before piecing it all together. Thomas had fun playing with colors, padding, borders and sizes to personalize the frontend while maintaining its simplcitity 

ChatGPT definetely helped to debug and resolve some of these issues that we experienced. Overall, while the team successfully scoped and implemented the functionality, incorporating more rigorous testing protocols would improve the project's success;
We were ensure as to how to run our program perfectly connecting both the backend and the frontend as we experienced numerous errors downloading Flask and making it work on VS code. And ChatGPT was a very helpful tool for us to understand why it was not working and what appropriate steps to take.
