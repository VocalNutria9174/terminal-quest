# commands_real.py
#
# Copyright (C) 2014-2016 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# Terminal commands which end up running in the terminal.


import os
import subprocess
import shutil

from .helper_functions import colour_file_dir, debugger
from linux_story.common import tq_file_system, fake_home_dir



def ls(real_loc, line, has_access=True):
    '''
    Prints out the coloured output of the ls command.

    Args:
        real_loc (str): the filepath of the current location of the user.
        line (str): line that the user entered in the terminal
            excluding ls.

    Returns:
        str of the output printed to the terminal.
    '''

    if not has_access:
        print(("ls: cannot open directory {}: Permission denied".format(line)))
        return

    new_loc = real_loc
    get_all_info = False
    new_lines = False
    args = ["ls"]
    line = line.replace('~', fake_home_dir)

    if line:
        args = line.split(" ")

        for a in args:
            # flags
            if a.startswith('-'):
                # break back up into new lines
                # long format
                if a.find("l") != -1:
                    get_all_info = True
                    pass
                if a.find("1") != -1:
                    new_lines = True
                    pass
            # directory
            else:
                new_loc = os.path.join(new_loc, a)

        args = ["ls"] + args

    debugger("args = {}".format(args))
    p = subprocess.Popen(args, cwd=real_loc,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    orig_output, err = p.communicate()
    if type(orig_output) != str:
        orig_output = orig_output.decode()
    if type(err) != str:
        err = err.decode()
    # The error will need to be edited if it contains info about the edited
    # filename
    if err:
        err = err.replace(tq_file_system, '~')
        print(err)
        return err

    # Need to filter output
    if type(orig_output) != str:
        files = (orig_output).decode().split('\n')
    else:
        files = (orig_output).split('\n')
    coloured_files = []
    output = " ".join(files)

    if get_all_info:
        for f in files:
            info = f.split(" ")
            i = info[-1]
            info.pop()
            path = os.path.join(new_loc, i)
            info.append(colour_file_dir(path, i))
            f = " ".join(info)
            coloured_files.append(f)
        coloured_output = "\n".join(coloured_files)

    else:
        for f in files:
            path = os.path.join(new_loc, f)
            coloured_files.append(colour_file_dir(path, f))

        if new_lines:
            coloured_output = "\n".join(coloured_files)
        else:
            coloured_output = " ".join(coloured_files)

    print(coloured_output)
    return output


def shell_command(real_loc, line, command_word=""):
    """
    Suitable for launching commands which don't involve curses.

    Args:
        real_loc (str): the current location of the user.
        line (str): line user typed not including the command word.
        command_word (str): command you want to run (e.g. ls).

    Returns:
        bool: False if error, True otherwise.
    """

    if command_word:
        line = command_word + " " + line

    line = line.replace('~', fake_home_dir)
    args = line.split(" ")

    # run the command
    p = subprocess.Popen(args, cwd=real_loc,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()

    if stderr:
        if type(stderr) != str:
            stderr = stderr.decode()
        print((stderr.strip().replace(fake_home_dir, '~')))
        return False

    if stdout:
        if type(stdout) != str:
            stdout = stdout.decode()
        if command_word == "cat":
            print(stdout)

        else:
            print((stdout.strip()))

    # should this return stdout?
    return True


def launch_application(real_path, line, command_word=""):
    '''
    This is appropriate for commands which use curses (e.g. less).

    Args:
        real_path (str): the current location of the user.
        line (str): the line (not including the command word) the user entered.
        command_word (str): the command that we want to launch.

    Returns:
        None.
    '''

    line = line.replace('~', fake_home_dir)
    line = " ".join([command_word] + line.split(" "))

    p = subprocess.Popen(line, cwd=real_path, shell=True)
    stdout, stderr = p.communicate()
    if stdout:
        if type(stdout) != str:
            stdout = stdout.decode()
        print((stdout.strip()))

    if stderr:
        if type(stderr) != str:
            stderr = stderr.decode()
        print((stderr.strip()))


def turn_abs_path_to_real_loc(path):
    return path.replace('~', tq_file_system)


def nano(real_path, line):
    '''
    Runs the linux-story version of nano as a separate process,
    and prints out any resulting errors.

    Args:
        real_path (str): the current location of the user.
        line (str): the command entered by the user.

    Returns:
        None
    '''

    # File path of the local nano
    nano_filepath = shutil.which("nano")

    if not os.path.exists(nano_filepath):
        # File path of installed nano
        nano_filepath = shutil.which("pico")

    if not os.path.exists(nano_filepath):
        raise Exception("Cannot find nano or pico")


    # Unsetting the LINES and COLUMNS variables because the
    # hack in TerminalUi.py which sets the size to 1000x1000 is disturbing nano
    # (https://github.com/KanoComputing/terminal-quest/commit/dd45b447363e3fdcebf80000dbbfd920b96637db)
    cmd = 'LINES= COLUMNS= ' + nano_filepath + " " + line
    p = subprocess.Popen(cmd, cwd=real_path, shell=True)
    stdout, stderr = p.communicate()

    if stdout:
        if type(stdout) != str:
            stdout = stdout.decode()
        print((stdout.strip()))

    if stderr:
        if type(stderr) != str:
            stderr = stderr.decode()
        print((stderr.strip()))


def run_executable(real_path, line):
    '''
    Runs the executable.

    Args:
        real_path (str): the current location of the user
        in the pseudo-terminal.
        line (str): the line the user entered.
    '''

    line = line.strip()

    if line.startswith("./"):
        line = line[2:]

    p = subprocess.Popen(["sh", line], cwd=real_path)
    stdout, stderr = p.communicate()


    if stdout:
            if type(stdout) != str:
                stdout = stdout.decode()
            print((stdout.strip()))

    if stderr:
        if type(stderr) != str:
            stderr = stderr.decode()
        print((stderr.strip()))
