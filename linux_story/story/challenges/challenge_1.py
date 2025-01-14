# challenge_1.py
#
# Copyright (C) 2014-2017 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A chapter of the story

from linux_story.StepTemplate import StepTemplate
from linux_story.story.terminals.terminal_ls import TerminalLs
from linux_story.helper_functions import wrap_in_box


class StepLs(StepTemplate):
    TerminalClass = TerminalLs


# ----------------------------------------------------------------------------------------


class Step1(StepLs):
    story = [
        ("{{wb:Alarm}}: {{Bb:\"Beep beep beep! Beep beep beep!\"}}"),
        ("{{wb:Radio}}: {{Bb:\"Good Morning, this is the 9am news.\"\n"),
        ("\"The town of Folderton has awoken to strange news. There have been reports of missing people and "
            "damaged buildings across the town, with more stories coming in as we speak.\""),
        ("\n\"Mayor Hubert has called an emergency town meeting and we'll keep you posted as it "
            "happens...\"}}\n"),
        ("It's time to get up sleepy head!\n "),
    ]  # TODO: " \ is a hack in this array to stop word wrap code screwing up and adding new lines in where it shouldn't

    story += wrap_in_box([
        ("{{gb:New Power:}} Type {{yb:ls}} and press"),
        ("{{ob:Enter}} to {{lb:look around}}."),
        "If you ever want to exit, type {{yb:exit}} and press {{ob:Enter}}."
    ])

    start_dir = "~/my-house/my-room"
    end_dir = "~/my-house/my-room"
    commands = "ls"
    highlighted_commands = ["ls"]
    hints = [
        ("{{rb:Type}} {{yb:ls}} {{rb:and press}} {{ob:Enter}} {{rb:to take a look around your bedroom.}}")
    ]


    def __next__(self):
        return 2, 1
