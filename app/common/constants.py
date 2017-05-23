import os

# Instance folder path, make it independent.
INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

# User role
ADMIN = 0
STAFF = 1
USER = 2
TESTER = 3
USER_ROLE = {
    ADMIN: 'admin',
    STAFF: 'staff',
    USER: 'user',
    TESTER: 'test'
}

# User model
PW_STRING_LEN = 80
MIN_USERNAME_LEN = 4
MAX_USERNAME_LEN = 30
MIN_PASSWORD_LEN = 6
MAX_PASSWORD_LEN = 30

# Standard stuff
STRING_LEN = 64
MAX_DESCRIPTION_LEN = 56000

