def draw(stick, cx):
    """Function to draw of the board."""
    if stick == 11:
        print("#######################\n | | | | | | | | | | | \n#######################")

    if stick == 10:
        print("#######################\n | | | | | | | | | |", cx, " \n#######################")

    if stick == 9:
        print("#######################\n | | | | | | | | |", cx, " \n#######################")

    if stick == 8:
        print("#######################\n | | | | | | | |", cx, " \n#######################")

    if stick == 7:
        print("######################\n | | | | | | |", cx, " \n#######################")

    if stick == 6:
        print("#######################\n | | | | | |", cx, " \n#######################")

    if stick == 5:
        print("########################\n | | | | |", cx, " \n#######################")

    if stick == 4:
        print("#######################\n | | | |", cx, " \n#######################")

    if stick == 3:
        print("#######################\n | | |", cx, " \n#######################")

    if stick == 2:
        print("#######################\n | |", cx, " \n#######################")

    if stick == 1:
        print("#######################\n |", cx, " \n#######################")

