n = int(input())

registered = dict()
loginned = set()

while n > 0:
    n = n - 1

    input_args = input().split(' ')
    cmd = input_args[0]
    name = input_args[1]
    if len(input_args) > 2:
        pwd = input_args[2]

    if 'register' == cmd:
        if name in registered.keys():
            print('fail: user already exists')
        else:
            registered[name] = pwd
            print('success: new user added')

    elif 'login' == cmd:
        if name in registered.keys():
            if registered[name] != pwd:
                print('fail: incorrect password')
            elif name in loginned:
                print('fail: already logged in')
            else:
                loginned.add(name)
                print('success: user logged in')
        else:
            print('fail: no such user')

    elif 'logout' == cmd:
        if name in registered.keys():
            if name in loginned:
                loginned.remove(name)
                print('success: user logged out')
            else:
                print('fail: already logged out')
        else:
            print('fail: no such user')
