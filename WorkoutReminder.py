
from tkinter import *
import time
import random


window = Tk()

class Workout:

	def __init__(self,master):
		self.frame = Frame(master)
		self.core_workout = ['Sit-ups','Butterflies','Bicycle','5-Inches']
		self.muscular_workout_equipment = ['Bench','Bicep Curl','Lawnmower','Butterfly-Sides']
		self.muscular_workout = ['Push-ups', 'Crunch']
		self.cardio_workout = ['Running in place','Jumping Up and Down']
		self.rep_workouts = [self.core_workout[0],self.muscular_workout_equipment[0 and 1 and 2],self.muscular_workout[0]]
		self.cardio_workouts = [self.core_workout[1 and 2 and 3],self.muscular_workout_equipment[3],self.muscular_workout[1],self.cardio_workout[0 and 1]]

	#	hell_workout = ['Push-ups, Sit-ups, Bicep Curl, Running in place']

		self.all_workouts = [self.core_workout[random.randint(0,3)],self.muscular_workout_equipment[random.randint(0,3)],self.muscular_workout[random.randint(0,1)],self.cardio_workout[random.randint(0,1)]]
		self.final_workouts = random.sample(self.all_workouts,2)
		self.final_workouts_1 = self.final_workouts[0]
		self.final_workouts_2 = self.final_workouts[1]

		self.reps_or_time()
		self.frame.pack()

	def reps_or_time(self):
		self.random_reps = random.randint(15,40)

		for workout in self.rep_workouts:
			if workout == self.final_workouts_1 or self.final_workouts_2:
				self.workout_label_1 = Label(self.frame,text=self.final_workouts_1 + ': ' + str(self.random_reps),anchor=N,font=('arial',20))
				self.workout_label_1.grid(row=0,column=0)

		for workout in self.cardio_workouts:
			if workout == self.final_workouts_1 or self.final_workouts_2:
				self.workout_label_2 = Label(self.frame,text=self.final_workouts_2 + ': ' + '2:00',anchor=N,font=('arial',20))
				self.workout_label_2.grid(row=1,column=0)

class Recursion(Workout):
	pass


c = Workout(window)

window.mainloop()



