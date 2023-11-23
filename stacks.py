#Stacks
#think of pancakes
#stacks are data structures where you can only ADD or REMOVE an element from the top of the structure
#last in first out

#Queue!
#people lining up in a queue
#first in first out
#two pointers: front of the queue and the space AFTER the last person at the queue
#if both pointers are pointing at same location: queue is empty
#circular array, when any of the two pointers reaches the end of the queue, it should go at the beginning
#dequeue is removing, enqueue is adding(an element)

#Deque => double-ended queue(you can remove/add from both sides)

#Simplify Path Interview Question
# e.g  /home/                /home
#      /../                  /
#      /home//1337/./        /home/1337
#      /home/../../tmp//./   /tmp


#      /home/../../tmp//./   /tmp

#      start    root(/)                 1
#      home  => /home(root to home)     2
#       <= ..   /                       3
#       <= ..   /                       4
#      tmp   => /tmp                    5
#       .       /tmp                    6
#      remove trailing slash(/)         7

#to remove an element without using pop(as the 
#requirements of my assignment dictate), I used 
#del, remove(), we could also use clear(), 
#   stack = []          #1
#   stack = ["home"]    #2
#   del stack[0]        #3-4 
#   print(stack)

#using logic we figure out the conditions where change is necessary
#1  start at home(stack=[])
#2  .. means back(remove element)
#3   . means here(pass)
#4   adding directory name means going there(stack.append(name))
 
def simplifyPath(path):
    stack = []

    for directory in path.split("/"):
        if directory == "":
            pass
        elif(directory == "."):
            pass
        elif(directory == ".."):
            if stack:
                del stack[-1]
            else:
                pass
        else:
            #add an empty variable at the end of the array
            stack = stack + ["0"]
            stack[-1] = directory
    return "/" + "/".join(stack)

result = simplifyPath("/home/../../tmp//./")
print(result)
