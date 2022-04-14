def PrintNames():
    try:
        my_file = open("namjes.txt")
        for name in my_file.readlines():
            print(name, end="")
            my_file.close()
    except:  # FileNotFoundError as e:
        print(f"unable to find the file: {str(e.args)}")
    finally:
        print("OK")


def InsertUser(user):
    my_file = open("names.txt", 'a')
    my_file.write(f"{user} \n")
    my_file.close()


InsertUser("haim")
InsertUser("baruch")
InsertUser("david")
my_file = open("namjes.txt")

PrintNames()
