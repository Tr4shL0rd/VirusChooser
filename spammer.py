print("spammer1 started!")
while True:
	with open("spam.txt", "a") as the_file:
    		the_file.write("Spam\n")