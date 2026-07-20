def combine_trucks(t,t1,t2):
    return t[t1]+t[t2]
def main():
    t=[0,4,7,2,6,9]
    print(combine_trucks(t,2,4))  # Expected: 13
    print(combine_trucks(t,1,3))  # Expected: 6
main()