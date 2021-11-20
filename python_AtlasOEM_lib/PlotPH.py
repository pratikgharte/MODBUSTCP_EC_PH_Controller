import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Read_PH_OEM
# Create figure for plotting
PHTrend = plt.figure()
ax = PHTrend.add_subplot(1, 1, 1)
xs = []
ys = []
# Initialize communication with TMP102

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    PH = round(Read_PH_OEM.main(), 2)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(PH)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    plt.ylim(0,14)
    plt.plot(xs, ys, marker='o', linestyle='--', color='g')
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('PH over Time')
    plt.ylabel('PH')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(PHTrend, animate, fargs=(xs, ys), interval=1000)
plt
plt.show()