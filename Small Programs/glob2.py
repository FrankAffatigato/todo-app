import glob

iterate = glob.glob("Testing\*.txt")
print('hi')
print(iterate)

for i in iterate:
    with open(i, 'r') as text_file:
        print(text_file.read())

