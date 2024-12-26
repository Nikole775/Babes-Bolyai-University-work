
import random
def print_menu():
    print("menu----------------------------------")
    print("1-->generate a list of random numbers")
    print("2-->sort the list using bubble sort")
    print ("3-->sort the list using the heap sort")
    print("4-->exit the program")
    print("choose an option:")
    return input("-->")

def random_numbers(n):
    list = []
    for i in range (1,n+1):
        list.append(random.randint(0,100))
    return list

def bubble_sort(list,s):
    n=len(list)
    steps =0
    for i in range(n):
        arranged =False
        for j in range(0,n-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                steps=steps+1
                if steps==s:
                    print("step -->")
                    print(list)
                    steps=0
                arranged= True
        if arranged==False :
            break

def heapify(list2,size,root,s,steps):
    largest=root
    l=2*root+1
    r=2*root+2
    if l<size and list2[largest]<list2[l]:
        largest=l
    if r<size and list2[largest]<list2[r]:
        largest=r
    if largest !=root:
        list2[root],list2[largest]=list2[largest],list2[root]
        steps = steps + 1
        if steps == s:
            print("building heap -->")
            print(list2)
            steps = 0
        heapify(list2,size,largest,s,steps)
        return steps


def heapMain(list,s):
    list2=list.copy()
    size=len(list2)
    steps=0
    for root in range (size//2-1,-1,-1):
        heapify(list2,size,root,s,steps)

    for root in range (size-1,0,-1):
        list2[root],list2[0]=list2[0],list2[root]

        steps = steps + 1
        if steps==s:
            print("building heap -->")
            print(list2)
            steps = 0
        heapify(list2, root, 0,s,steps)
    print("the sorted list: ",list2)

def start():
    ok=0
    while True :
        try:
            option = int(print_menu())
        except:
            print("invalid option")
            pass
        if option==1:
            print("length of the list: ")
            n=int(input())
            arr = random_numbers(n)
            print(arr)
            ok=1
        elif option==2:
            if ok==1:
                print("step number: ")
                s=int(input())
                bubble_sort(arr,s)
            else :print("the list doesn't exist.Choose first option 1")
        elif option==3:
            if ok==1:
                print("step number: ")
                s = int(input())
                heapMain(arr,s)
                print("the sorted list: ",arr)
            else:print("the list doesn't exist.Choose first option 1")
        elif option==4:
            break
        else:
            print("bad command!")

start()


