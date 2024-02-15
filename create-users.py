#!/usr/bin/env python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        # checking for lines that start with '#' and making sure to skip them
        match = re.match('^#', line)
        if match or len(fields := line.strip().split(':')) != 5:
            continue  # often anything that starts with '#' denotes a comment and anything with less than 5 fields is not valid

        username = fields[0]
        password = fields[1]

        gecos = "%s %s,,," % (fields[3], fields[2])  # combines fields 3 and 2 since the gecos string typically contains the full name and other information

        groups = fields[4].split(',')  # splits the fifth field by a comma and assigns the outcome to 'groups' because groups are comma-separated

        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)  # this line is to create a user account with the given options

        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)  # setting password for the newly created user account

        # this for loop is responsible for assigning the user to groups using the adduser command
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()


