def div_number(a,b):
    try:
        print(a/b)
    #except:
        #print("unable to divide by zero")
    except ZeroDivisionError:
        print("adsadsasd")
    finally:
        print("all good")
div_number(8,2)
div_number(9,0)