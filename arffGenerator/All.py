information = "@RELATION all\n\n"
for i in range(1, 24 + 81 + 1 + 1):
    information += "@ATTRIBUTE a" + str(i) + " REAL\n"
information += "@ATTRIBUTE class {1,2,3,4,5}\n\n"
information += "@DATA\n"

labels = open("/home/emre/Desktop/labels.txt", "r")
file = open("/home/emre/Desktop/Project/arff files/all.arff", "w+")
file.write(information)

hogName = "/home/emre/Desktop/Feature Vectors/HOG/SCUT-FBP-"
gaborName = "/home/emre/Desktop/Feature Vectors/GABOR/SCUT-FBP-"
fractalName = "/home/emre/Desktop/Feature Vectors/FRACTAL/SCUT-FBP-"

for i in range(1, 501):

    foo3 = open(fractalName + str(i) + ".txt", "r")
    token = foo3.readline()
    float_number = float(token)
    file.write(str(float_number) + ", ")
    foo3.close()

    foo = open(hogName + str(i) + ".txt", "r")
    for j in range(81):
        token = foo.readline()
        float_number = float(token)
        file.write(str(float_number) + ", ")
    foo.close()

    foo2 = open(gaborName + str(i) + ".txt", "r")
    for j in range(24):
        token = foo2.readline()
        float_number = float(token)
        file.write(str(float_number) + ", ")
    foo2.close()

    label = int(labels.readline())
    file.write(str(label) + "\n")

file.close()
labels.close()