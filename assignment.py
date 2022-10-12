import os

ppid: int


def child() -> None:
    c_pid = os.getpid()
    if c_pid == ppid:
        print("This is not a child")
        return
    print("This is a child")
    status = int(input())
    os._exit(status)

    

def get_child_exit_status() -> int:
    cpid, status = os.wait()
    if os.WIFEXITED(status):
        return os.WEXITSTATUS(status)


def main() -> None:
    global ppid
    ppid = os.getpid()
    pid = os.fork()
    # Write the code here to create a child process.
    if pid == 0:
    # inside the child process
    # -----------------------------------------------------------
        child()
    # -----------------------------------------------------------
    else:
    # inside the parent process
    # -----------------------------------------------------------
        print("Child exited with status={}".format(get_child_exit_status()))
    # -----------------------------------------------------------

if __name__ == "__main__":
    main()
  
