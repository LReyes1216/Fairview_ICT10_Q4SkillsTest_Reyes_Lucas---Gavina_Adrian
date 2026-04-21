from pyscript import display, document
import numpy as np
# as np was used to easily use numpy
import matplotlib.pyplot as plt
# as plt was used for the same reason
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

plt.figure()
plt.plot([0,1], [0,1])
plt.close()
     
days = [] # these are the days of the week, which will be used as the x-axis labels for the plot
absences = [] # I used 0 for all days since there were no absences, but you can change the values to reflect the actual absences for each day.

def calculate_absences(e):
    document.getElementById('output').innerHTML = ""
    absence = document.getElementById('absences').value
    day = document.getElementById('Days').value
    if day == "" or absence == "":
        display("ERROR! Please check all input fields!", target="output", append=False)
        return
    
    days.append(day)
    absences.append(absence)
    
    converted_absences = sorted(np.array(absences))
   
    plt.clf() # This clears the previous plot so that the new plot can be displayed without overlap
    plt.grid() # This adds a grid to the plot for better visibility
    plt.plot(days, converted_absences, marker='o')
    plt.title("Weekly Attendance (Absences)")  
    
    plt.xlabel("Days of the Week")
    plt.ylabel("Number of Absences")
    plt.show()