# -*- coding: utf-8 -*-
"""
@author: saibrone
"""
from tkinter import *
from tkinter.ttk import Combobox

class Application(Frame):
    def create_widgets(self):
        Label(self, text="Robot Model").grid(row=0)
        self.robot_model = Combobox(self, values=["Articulated", "Cartesian", "Scara", "Delta"])
        self.robot_model.grid(row=0, column=1)

        Label(self, text="Number of Links").grid(row=1)
        self.num_links = Entry(self)
        self.num_links.grid(row=1, column=1)

        Label(self, text="Number of Joints").grid(row=2)
        self.num_joints = Entry(self)
        self.num_joints.grid(row=2, column=1)

        Label(self, text="World Dimension").grid(row=3)
        self.dimension = Combobox(self, values=["2D", "3D"])
        self.dimension.grid(row=3, column=1)

        Button(self, text="Generate Link and Joint Inputs", command=self.generate_inputs).grid(row=4)
        Button(self, text="Calculate Forward Kinematics", command=self.calculate_forward_kinematics).grid(row=5)
        Button(self, text="Calculate Inverse Kinematics", command=self.calculate_inverse_kinematics).grid(row=6)

        self.link_entries = []
        self.joint_comboboxes = []

    def generate_inputs(self):
        links = int(self.num_links.get())
        joints = int(self.num_joints.get())
        dimension = self.dimension.get()

        # Clear previous link entries and joint comboboxes if any
        for entry in self.link_entries:
            entry.destroy()
        for combobox in self.joint_comboboxes:
            combobox.destroy()
        self.link_entries.clear()
        self.joint_comboboxes.clear()

        # Calculate DOF using Grubler's formula
        # For simplicity, assuming all joints are full joints (one degree of freedom)
        P = joints
        H = 0
        if dimension == "2D":
            DOF = 3 * (links - 1) - 2 * P + H
        else: # 3D
            DOF = 6 * (links - 1) - 2 * P + H

        Label(self, text=f"Degrees of Freedom: {DOF}").grid(row=7)

        for i in range(links):
            Label(self, text=f"Length of Link {i+1}").grid(row=i+8)
            entry = Entry(self)
            entry.grid(row=i+8, column=1)
            self.link_entries.append(entry)

        for j in range(joints):
            Label(self, text=f"Type of Joint {j+1}").grid(row=j+links+8)
            combobox = Combobox(self, values=["Revolute", "Prismatic", "Helical"])
            combobox.grid(row=j+links+8, column=1)
            self.joint_comboboxes.append(combobox)

    def calculate_forward_kinematics(self):
        # Implement Forward Kinematics Calculation
        robot_model = self.robot_model.get()
        link_lengths = [entry.get() for entry in self.link_entries]
        print(f"Calculating Forward Kinematics for {robot_model} with link lengths {link_lengths}")

    def calculate_inverse_kinematics(self):
        # Implement Inverse Kinematics Calculation
        robot_model = self.robot_model.get()
        link_lengths = [entry.get() for entry in self.link_entries]
        print(f"Calculating Inverse Kinematics for {robot_model} with link lengths {link_lengths}")

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

root = Tk()
app = Application(master=root)
app.mainloop()
