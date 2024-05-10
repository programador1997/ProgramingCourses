def main():
    m = int(input("m:"))
    print("E: ", emc2(m))

def emc2(m):
    c = (pow(300000000, 2))
    e = (m*c)
    return e 

main()