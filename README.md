# Alarm-Clock-Python
An implementation of Alarm Clock in Terminal using Python.

This is a Python script that creates a simple alarm clock application using the Tkinter GUI library. 
Users can set a specific time for the alarm to go off, and when that time is reached, a message is displayed on the screen and a sound is played.

The script uses the datetime and time libraries to manage the time and the playsound library to play audio files. 
The GUI elements are created using Tkinter, and the alarm time is set by the user using Entry widgets. When the user clicks the "Set Alarm" button, the setalarm() function is called, which sets the alarm time and calls the alarmclock() function.

The alarmclock() function continuously checks the current time against the alarm time until the two are equal. 
When the times match, a message is displayed on the screen, and the audio file specified in the code is played. 
Finally, the function exits the while loop and the program ends
