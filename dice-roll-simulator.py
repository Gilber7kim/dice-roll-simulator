#This makes the while loop that makes the program run forever.
while True:
    # it imports the module random.
    import random
    # These two commands print "Hi!! Welcome to Gilbert's ramdom dicedice simulator!" and "Press ctrl+c to quit"
    print("Hi!! Welcome to Gilbert's ramdom dicedice simulator!")
    print("Press ctrl+c to quit")
    # Command raw_input allows you to type something. In this case, it allows you to type enter or ctrl+C by pausing the while loop.
    raw_input("Enter to continue")
    # It makes the numbers between one to six to show up in the dice randomly.
    number = random.randint (1,6)
    # These are the possibilities of dice
    if number==1:
        print ("[----------------]")
        print ("[----------------]")
        print ("[-------()-------]")
        print ("[----------------]")
        print ("[----------------]")
    if number==2:
        print ("[----------------]")
        print ("[----------------]")
        print ("[--()--------()--]")
        print ("[----------------]")
        print ("[----------------]")
    if number==3:
        print ("[-()-------------]")
        print ("[----------------]")
        print ("[-------()-------]")
        print ("[----------------]")
        print ("[-------------()-]")
    if number==4:
        print ("[-()----------()-]")
        print ("[----------------]")
        print ("[----------------]")
        print ("[----------------]")
        print ("[-()----------()-]")
    if number==5:
        print ("[-()----------()-]")
        print ("[----------------]")
        print ("[-------()-------]")
        print ("[----------------]")
        print ("[-()----------()-]")
    if number == 6:
        print ("[-()----------()-]")
        print ("[----------------]")
        print ("[-()----------()-]")
        print ("[----------------]")
        print ("[-()----------()-]")
