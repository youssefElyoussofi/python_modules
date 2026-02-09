

def test():
    print("hello world")

# we are using this condition because if we include our lib somewhere else we don't want 
# print("i am running") and test() execute until we run it using lib.test()
# remove condition will let test() execute each time we import lib
if __name__=="__main__":
    test()