#Exercise2
f = open("txt_test", "r")
print(f.read())
f.close()

#Exercise3
x = open("txt_test", "a")
x.write("This line was appended")
x.close()

#Exercise4
y = open("txt_test", "r")
print(y.read())
y.close()

#Exercise5
copy = open("txt_test_copy", "w")
z = open("txt_test", "r")
for i in z:
    copy.write(str(i))
z.close()


