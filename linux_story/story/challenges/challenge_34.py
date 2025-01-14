#!/usr/bin/env python
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A chapter of the story
from linux_story.StepTemplate import StepTemplate
from linux_story.helper_functions import wrap_in_box
from linux_story.step_helper_functions import unblock_commands
from linux_story.story.terminals.terminal_chmod import TerminalChmod
from linux_story.story.terminals.terminal_nano import TerminalNano


class StepTemplateNano(StepTemplate):
    TerminalClass = TerminalNano


class StepTemplateChmod(StepTemplate):
    TerminalClass = TerminalChmod


class Step1(StepTemplateNano):
    story = [
        ("There are three doors, leading to two rooms and a cage."),
        ("First, {{lb:look inside the dark-room}}.")
    ]
    start_dir = "~/woods/cave"
    end_dir = "~/woods/cave"
    commands = [
        "ls dark-room",
        "ls dark-room/"
    ]
    hints = [
        ("{{rb:Use}} {{yb:ls dark-room/}} {{rb:to look inside the dark-room.}}")
    ]

    def __next__(self):
        return 34, 2


class Step2(StepTemplateNano):
    story = [
        ("The room is pitch black, and it is impossible to see anything inside."),
        ("Next, {{lb:look inside}} the {{bb:locked-room}}")
    ]
    start_dir = "~/woods/cave"
    end_dir = "~/woods/cave"
    commands = [
        "ls locked-room",
        "ls locked-room/"
    ]
    hints = [
        ("{{rb:Use}} {{yb:ls locked-room/}} {{rb:to look inside the locked-room.}}")
    ]

    def __next__(self):
        return 34, 3


class Step3(StepTemplateNano):
    story = [
        ("Peering through a grimy window, you can just make out the items inside."),
        ("{{lb:Examine the items inside}}.")
    ]
    start_dir = "~/woods/cave"
    end_dir = "~/woods/cave"
    commands = [
        "cat locked-room/sign",
        "cat locked-room/firework"
    ]
    hints = [
        ("{{rb:Examine the sign with}} {{yb:cat locked-room/sign}}")
    ]

    def __next__(self):
        return 34, 4


class Step4(StepTemplateNano):
    story = [
        ("You are unable to make out the items in the room."),
        ("Maybe it would help if you went inside?"),
        ("Try and {{lb:go inside}} the {{bb:locked-room}}.")
    ]
    start_dir = "~/woods/cave"
    end_dir = "~/woods/cave"
    dirs_to_attempt = "~/woods/cave/locked-room"
    hints = [
        ("{{rb:Go inside the locked-room with}} {{yb:cd locked-room}}")
    ]
    commands = [
        "cd locked-room",
        "cd locked-room/"
    ]

    def block_command(self, last_user_input):
        return unblock_commands(last_user_input, self.commands)

    def __next__(self):
        return 34, 5


class Step5(StepTemplateNano):
    story = [
        ("The door is locked, so you can't go in."),
        ("Finally, {{lb:look inside}} the {{bb:cage}}.")
    ]
    start_dir = "~/woods/cave"
    end_dir = "~/woods/cave"
    commands = [
        "ls cage",
        "ls cage/"
    ]
    hints = [
        ("{{rb:Look inside the cage with}} {{yb:ls cage}}")
    ]

    def __next__(self):
        return 34, 6


class Step6(StepTemplateNano):
    story = [
        ("There is a bird in the cage. {{lb:Examine}} the bird."),
    ]
    start_dir = "~/woods/cave"
    end_dir = "~/woods/cave"
    commands = [
        "cat cage/bird"
    ]
    hints = [
        ("{{rb:Examine the bird with}} {{yb:cat cage/bird}}")
    ]

    def __next__(self):
        return 34, 7


class Step7(StepTemplateNano):
    story = [
        ("Bird: {{Bb:\"...Me...trapped..\"}}"),
        ("{{Bb:\"Please help....get me out.\"}}"),
        "",
        ("Help the bird by {{lb:moving}} the {{lb:bird}} outside the {{lb:cage}}.")
    ]
    start_dir = "~/woods/cave"
    end_dir = "~/woods/cave"
    commands = [
        "mv cage/bird .",
        "mv cage/bird ./"
    ]
    hints = [
        ("{{rb:Move the bird outside the cage with}} {{yb:mv cage/bird ./}}")
    ]

    def block_command(self, line):
        return unblock_commands(line, self.commands)

    def __next__(self):
        return 34, 8



class Step8(StepTemplateChmod):
    story = [
        "You are unable to move the bird outside the cage.",
        "Bird: {{Bb:\"...didn't work....\"}}",
        "{{Bb:\"...look in}} {{lb:dark-room}} {{Bb:to find help..\"}}",
        "{{Bb:\"..use}} {{yb:chmod +r dark-room}} {{Bb:to switch lights on.\"}}",
        "{{Bb:\"...get me out...and I'll help you.\"}}",
        ""
    ]
    story += wrap_in_box([
        ("{{gb:New Power:}} Use "),
        ("{{yb:chmod +r dark-room}} "),
        ("to allow yourself to {{lb:read}} "),
        ("the contents of dark-room.")
    ])

    start_dir = "~/woods/cave"
    end_dir = "~/woods/cave"
    commands = [
        "chmod +r dark-room",
        "chmod +r dark-room/"
    ]
    highlighted_commands = "chmod"
    hints = [
        "{{rb:Follow the bird's instructions and use}} {{yb:chmod +r dark-room}} {{rb:to turn the lights on in the}} "
        "{{bb:dark-room.}}"
    ]

    def __next__(self):
        return 35, 1
