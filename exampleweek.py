# wellness week example analysis

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

week_days = np.array([1, 2, 3, 4, 5, 6, 7])  


# water consumption

water1 = np.array([34, 51, 42, 68, 34, 51, 17])
water2 = np.array([17, 34, 68, 51, 34, 34, 51])
water3 = np.array([68, 17, 51, 17, 34, 17, 34])
watergoal = np.array([68, 68, 68, 68, 68, 68, 68])

plt.plot(week_days, water1)
plt.plot(week_days, water2)
plt.plot(week_days, water3)
plt.plot(week_days, watergoal)

plt.xlabel("Week Days")
plt.ylabel("Water Fluid oz")
plt.title('Water Consumption')

plt.legend(["Week 01", "Week 02", "Week 03", "Water Goal"], loc ="upper right")
plt.show()


# sleep received

sleep1 = np.array([8, 6, 7, 7, 6, 6, 8])
sleep2 = np.array([7, 6, 5, 7, 6, 7, 8])
sleep3 = np.array([8, 5, 7, 6, 7, 6, 7])
sleepgoal = np.array([8, 8, 8, 8, 8, 8, 8])
  
plt.plot(week_days, sleep1)
plt.plot(week_days, sleep2)
plt.plot(week_days, sleep3)
plt.plot(week_days, sleepgoal)

  
plt.xlabel("Week Days")
plt.ylabel("Sleep Hours")
plt.title('Sleep Received')

plt.legend(["Week 01", "Week 02", "Week 03", "Sleep Goal"], loc ="upper right")
plt.show()

# exercise done

exercise1 = np.array([65, 70, 60, 70, 75, 60, 65])
exercise2 = np.array([85, 55, 70, 60, 80, 50, 60])
exercise3 = np.array([70, 80, 65, 55, 70, 65, 70])
exercisegoal = np.array([60, 60, 60, 60, 60, 60, 60])
  
plt.plot(week_days, exercise1)
plt.plot(week_days, exercise2)
plt.plot(week_days, exercise3)
plt.plot(week_days, exercisegoal)
  
plt.xlabel("Week Days")
plt.ylabel("Exercise Minutes")
plt.title('Exercise Done')

plt.legend(["Week 01", "Week 02", "Week 03", "Exercise Goal"], loc ="upper right")
plt.show()

# active mind time

activemind1 = np.array([2, 4, 5, 4, 5, 5, 3])
activemind2 = np.array([3, 5, 4, 6, 2, 3, 2])
activemind3 = np.array([4, 3, 6, 5, 3, 4, 3])
activemindgoal = np.array([4, 4, 4, 4, 4, 4, 4])
  
plt.plot(week_days, activemind1)
plt.plot(week_days, activemind2)
plt.plot(week_days, activemind3)
plt.plot(week_days, activemindgoal)

plt.xlabel("Week Days")
plt.ylabel("Active Mind Hours")
plt.title('Active Mind Time')

plt.legend(["Week 01", "Week 02", "Week 03", "Active Mind Goal"], loc ="upper right")
plt.show()

