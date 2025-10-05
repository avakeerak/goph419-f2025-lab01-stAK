from python_package.functions import (sqrt, arcsin, launch_angle_range)
import numpy as np
import matplotlib.pyplot as plt

def main():

    ve_v0 = 2
    tol_alpha = 0.04

    a_values = np.linspace(0.01, 0.99, 100)

    min_angle = []
    max_angle = []
    failed_a = []

    for a in a_values:
            try:
                angles = launch_angle_range(ve_v0, a, tol_alpha)
                min_rads = (angles[1])
                max_rads = (angles[0])
            
            except ValueError:
                 failed_a.append(a)
                 min_angle.append(np.nan)
                 max_angle.append(np.nan)
                 continue
            
            min_deg = min_rads * (180 / 3.14159265359)
            max_deg = max_rads * (180 / 3.14159265359)

            min_angle.append(min_deg)
            max_angle.append(max_deg)     

    save_path = 'C:/Users/avake/GOPH419/goph419-f2025-lab01-stAK/figures/constant_ve_v0.png'

    plt.figure(figsize=(6.5, 4.5))
    plt.plot(a_values, min_angle, label='Minimum Launch Angle')
    plt.plot(a_values, max_angle, label='Maximum Launch Angle')
    plt.xlabel('alpha')
    plt.ylabel('Launch Angle (degrees)')
    plt.title('Launch Angle Range at Ve/V0 = 2')
    plt.legend(loc='best')

    plt.savefig(save_path)
    plt.close()

    if failed_a:
        print(f"Values of alpha that caused a negative radicand in equation 17: {failed_a}")

main()