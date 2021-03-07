print "Arimengen script"

CorrectUsername = "a"
CorrectPassword = "a"

loop = 'true'
while (loop == 'true'):
    username = raw_input("username: ")
    if (username == CorrectUsername):
    	password = raw_input("password: ")
        if (password == CorrectPassword):
            print "Login Berhasil !!! " + username
            loop = 'false'
        else:
            print "Password Salah!"
    else:
        print "Username Salah!"