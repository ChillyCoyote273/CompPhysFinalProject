# name: Alex Prichard
# date: 28 Nov 2022
# bugs: none

import numpy as np
import matplotlib.pyplot as plt


def get_temp(x, y):
	if np.hypot(x, y) < 0.1:
		return 100
	return 0


def main():
	num_points = 11
	x_axis = np.linspace(-1, 1, num_points)
	y_axis = np.linspace(-1, 1, num_points)
	heat_map = np.array([[get_temp(x_coord, y_coord) for x_coord in x_axis] for y_coord in y_axis])

	dt = 0.1
	dx = 2.0 / (num_points - 1)
	alpha = 1
	heat_flow_kernel_2d = np.array([
		[ 0, 1, 0 ],
		[ 1, -4, 1 ],
		[ 0, 1, 0 ]
	]) / dx**2
	print(heat_map)


if __name__ == "__main__":
	main()
