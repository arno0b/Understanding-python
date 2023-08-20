def is_strict_superset(A, rest):
    super = True
    for i in rest:
        if not set(A).issuperset(i):
            super = False
        else:
            super = True
    return super

def main():
    A = input().split()
    set_no = int(input())
    rest = []
    for _ in range(set_no):
        rest.append(input().split()) 
           
    if is_strict_superset(A, rest):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()