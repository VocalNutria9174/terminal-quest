# challenge_18.py
#
# Copyright (C) 2014-2016 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A chapter of the story
from linux_story.StepTemplate import StepTemplate
from linux_story.step_helper_functions import unblock_cd_commands
from linux_story.story.terminals.terminal_echo import TerminalEcho


class StepTemplateEcho(StepTemplate):
    TerminalClass = TerminalEcho


# ----------------------------------------------------------------------------------------

class Step1(StepTemplateEcho):
    story = [
        ("Woah! You spoke aloud into the empty room!\n"),
        ("{{gb:You learnt the new power}} {{lb:echo}}{{gb:!}}\n"),
        ("This command can probably be used to talk to people."),

        ("\nNow let's head to {{bb:~}} to find that farm!"),
        ("Type {{yb:cd}} by itself to go to the Windy Road {{bb:~}}")
    ]

    hints = [
        ("{{rb:Use}} {{yb:cd}} {{rb:by itself to go to}} {{bb:~}}")
    ]

    start_dir = "~/my-house/parents-room"
    end_dir = "~"

    def block_command(self, line):
        return unblock_cd_commands(line)

    def __next__(self):
        return 18, 2


class Step2(StepTemplateEcho):
    story = [
        ("You are back on the windy road, which stretches endlessly in both directions. \n{{lb:Look around.}}")
    ]
    hints = [
        ("{{rb:Look around with}} {{yb:ls}}{{rb:.}}")
    ]

    commands = [
        "ls",
        "ls -a"
    ]
    start_dir = '~'
    end_dir = '~'

    def __next__(self):
        return 18, 3


class Step3(StepTemplateEcho):
    story = [
        ("You notice a small remote farm in the distance.\n"),
        ("{{lb:Let's go}} to the {{bb:farm}}.")
    ]

    start_dir = "~"
    end_dir = "~/farm"
    hints = [
        ("{{rb:Use}} {{yb:cd farm}} {{rb:to head to the farm.}}")
    ]

    def block_command(self, line):
        return unblock_cd_commands(line)

    def __next__(self):
        return 18, 4


class Step4(StepTemplateEcho):
    story = [
        ("You walk up the path to the farm"),
        ("{{lb:Look around.}}")
    ]

    commands = "ls"
    start_dir = "~/farm"
    end_dir = "~/farm"
    hints = [("{{rb:Use}} {{yb:ls}} {{rb:to look around.}}")]

    def __next__(self):
        return 18, 5


class Step5(StepTemplateEcho):
    story = [
        ("You are in a farm, with a {{bb:barn}}, a {{bb:farmhouse}} and a large {{bb:toolshed}} in sight."),
        ("The land is well tended and weed free, so there must be people about here.\n"),
        ("{{lb:Look around}} and see if you can find someone to talk to.")
    ]
    start_dir = "~/farm"
    end_dir = "~/farm"
    counter = 0

    def finished_challenge(self, line):
        output = self.check_output(line)
        if not output:
            # If Ruth not in output, check if command is ls
            self.check_command()

        return output

    def output_condition(self, output):
        if 'Ruth' in output:
            return True

        return False

    def check_command(self, line):
        if line == 'ls' or 'ls ' in line:
            self.counter += 1

            if self.counter >= 3:
                self.send_hint(("\n{{rb:Use}} {{yb:ls barn}} {{rb:to look in the barn.}}"))
            if self.counter == 2:
                self.send_hint(("\n{{rb:Have you looked in the}} {{bb:barn}} {{rb:yet?}}"))
            elif self.counter == 1:
                self.send_hint(("\n{{rb:There is no one here. You should look somewhere else.}}"))

        else:
            self.send_hint("\n{{rb:Use}} {{yb:ls}} {{rb:to look around.}}")

    def block_command(self, line):
        if "mv" in line:
            return True

    def __next__(self):
        return 18, 6


class Step6(StepTemplateEcho):

    story = [
        ("In the {{bb:barn}}, you see a woman tending some animals."),
        ("{{lb:Walk}} into the {{bb:barn}} so you can have a closer look.")
    ]

    start_dir = "~/farm"
    end_dir = "~/farm/barn"
    hints = [
        ("{{rb:Use}} {{yb:cd barn}} {{rb:to walk into the barn.}}")
    ]

    def block_command(self, line):
        return unblock_cd_commands(line)

    def __next__(self):
        return 18, 7


class Step7(StepTemplateEcho):

    story = [
        ("{{lb:Examine}} everyone in the {{bb:barn}} using the {{yb:cat}} command.")
    ]

    all_commands = {
        "cat Ruth": ("Ruth: {{Bb:\"Ah! Who are you?!\"}}"),
        "cat Cobweb": ("Cobweb: {{Bb:\"Neiiigh.\"}}"),
        "cat Trotter": ("Trotter: {{Bb:\"Oink Oink.\"}}"),
        "cat Daisy": ("Daisy: {{Bb:\"Mooooooooo.\"}}")
    }

    start_dir = "~/farm/barn"
    end_dir = "~/farm/barn"

    hints = [
        ("{{rb:If you've forgotten who's in the barn, use}} {{yb:ls}} {{rb:to remind yourself.}}")
    ]

    # TODO: move this into step_helper_functions, used a few too many times outside.
    def check_command(self, line):

        # If we've emptied the list of available commands, then pass the level
        if not self.all_commands:
            return True

        # If they enter ls, say Well Done
        if line == 'ls':
            hint = ("\n{{gb:You look around.}}")
            self.send_hint(hint)
            return False

        # check through list of commands
        end_dir_validated = self.get_fake_path() == self.end_dir

        # if the validation is included
        if self._last_user_input in list(self.all_commands.keys()) and \
                end_dir_validated:

            # Print hint from person
            hint = "\n" + self.all_commands[self._last_user_input]

            self.all_commands.pop(self._last_user_input, None)

            if len(self.all_commands) == 1:
                hint += ("\n{{gb:Well done! Have a look at one more.}}")
            elif len(self.all_commands) > 0:
                hint += ("\n{{gb:Well done! Look at %d more.}}") % len(self.all_commands)
            else:
                hint += ("\n{{gb:Press}} {{ob:Enter}} {{gb:to continue.}}")

            self.send_hint(hint)

        else:
            if not self.hints:
                self.hints = [
                    ("{{rb:Use}} {{yb:%s}} {{rb:to progress.}}") % list(self.all_commands.keys())[0]
                ]
            self.send_stored_hint()
            self.hints.pop()
        return False

    def __next__(self):
        return 19, 1
