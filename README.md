# Fruit Fly Optimization Algorithm (FOA) & Robot Kinematics Application :robot:

This repository contains Python implementations of the Fruit Fly Optimization Algorithm (FOA) for solving the inverse kinematics of a robot. Additionally, it includes a GUI application for forward and inverse kinematics calculations for various robot models.

## Table of Contents
- [FOA for Inverse Kinematics](#foa-for-inverse-kinematics)
- [Robot Kinematics Application](#robot-kinematics-application)
- [Usage](#usage)
- [Author](#author)
- [References](#references)

## FOA for Inverse Kinematics :apple:

The FOA is a nature-inspired optimization algorithm that emulates the foraging behavior of fruit flies. The algorithm is applied to find the best joint angles that will position the robot's end-effector closest to a desired position.

The basic structure of a fruit fly is defined in the `FruitFly` class. Each fruit fly has a position (joint angles) and a smell (distance from the desired position). The optimization process guides the fruit flies towards the best solution.

The main steps are:
1. Initialize a population of fruit flies.
2. Evaluate their smells based on their positions.
3. Guide them towards the best position found so far.
4. Repeat for a set number of iterations.

## Robot Kinematics Application :gear:

A GUI-based application is provided that helps in calculating the forward and inverse kinematics of various robot models. The application allows users to:
- Select the robot model.
- Input the number of links and joints.
- Provide dimensions and types for each link and joint.
- Compute the Degrees of Freedom (DOF) based on the provided parameters.
- Calculate forward and inverse kinematics.

The application is built using the `Tkinter` library.
![image](https://github.com/SAIPRONE/kinematics/assets/95390348/e258a172-231c-42db-9761-fdcf20f18e25)

## Usage :computer:

1. To run the FOA for inverse kinematics, execute the script containing the FOA implementation.
2. To run the Robot Kinematics Application, execute the script with the `Tkinter` GUI application.

 'python foa_script.py'
 'python robot_kinematics_app.py'

## Author :pencil:

**Fadi Helal**

## License :balance_scale:

This project is licensed under the BSD3 License.

## References :books:

- For a deeper understanding of the Fruit Fly Optimization Algorithm:
  - [Nature-Inspired Optimization Algorithms](#) (relevant book on the topic)

- `Tkinter` library for GUI:
  - [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

