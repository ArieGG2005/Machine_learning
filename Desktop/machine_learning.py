from sklearn import tree
import sys
print("-------------------------\n")
print("APPLE OR ORANGE PREDICTOR!!!\n")
print("---------------------------\n")


features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
weight = input("Enter the weight: ")
texture = input("Enter texture: ")

if texture == "Smooth" or texture == "smooth":
	texture = 1
elif texture == "Bumpy" or texture == "bumpy":
	texture = 0
else:
	print("Invalid. Pls Try Again!")
	sys.exit()

featureArray = [weight, texture]

predict = clf.predict([featureArray])
print("\n")

if predict == 0:
	print("APPLE!!!!!!!!")
elif predict == 1: 
	print("ORANGE!!!!!!!!!")
