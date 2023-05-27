import subprocess


def create_user(user_number):
    subprocess.call(f"pytest -s tests/test_register_new_user.py --user_number={user_number}", shell=True)