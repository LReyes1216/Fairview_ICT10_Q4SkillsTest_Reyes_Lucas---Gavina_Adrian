from operator import index

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
     
days = np.array(["Mon", "Tues", "Wed", "Thurs", "Fri"]) # these are the days of the week, which will be used as the x-axis labels for the plot
ogabsences = np.zeros(5) # I used 0 for all days since we are assuming the default value to be 0, but you can change the values to reflect the actual absences for each day.

def calculate_absences(e):
    #To clear output field
    document.getElementById('output').innerHTML = ""
    absence_user = document.getElementById('absences').value
    day = document.getElementById('Days').value
    
    if day == "" or absence_user == "":
        display("ERROR! Please check all input fields!", target="output", append=False)
        return
    absence = int(absence_user)
    index = np.where(days == day)[0][0] # This finds the index of the selected day in the 'days' array
    ogabsences[index] = absence # This updates the 'ogabsences' array at the corresponding index with the input for absences. This ensures the graph can go up or down.
    
    
    plt.clf() # This clears the previous plot so that the new plot can be displayed without overlap
    plt.grid() # This adds a grid to the plot for better visibility
    plt.plot(days, ogabsences, marker='o')
    plt.title("Weekly Attendance (Absences)")  
    
    plt.xlabel("Days of the Week")
    plt.ylabel("Number of Absences")
    display(plt, target="graph-area", append=False)