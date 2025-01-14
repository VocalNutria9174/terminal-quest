# challenge_28.py
#
# Copyright (C) 2014-2016 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A chapter of the story
from linux_story.story.challenges.CompanionMisc import StepTemplateNano
from linux_story.common import get_story_file
from linux_story.step_helper_functions import unblock_cd_commands


# ----------------------------------------------------------------------------------------


class Step1(StepTemplateNano):
    story = [
        ("You're back in town. {{bb:Eleanor}} looked relieved to be outside."),
        ("Where could the {{bb:librarian}} be hiding?\n"),
        ("{{lb:Look around}} to decide where to go next.")
    ]

    start_dir = "~/town/east"
    end_dir = "~/town/east"

    hints = [
        ("{{rb:Use}} {{yb:ls}} {{rb:to look around.}}")
    ]

    deleted_items = ["~/town/east/shed-shop/Eleanor"]
    file_list = [
        {
            "path": "~/town/east/Eleanor",
            "contents": get_story_file("Eleanor")
        }
    ]

    commands = [
        "ls",
        "ls -a"
    ]

    companion_speech = ("Eleanor: {{Bb:\"I'm hungry. Can you see anywhere we could eat?\"}}")

    def __next__(self):
        return 28, 2


class Step2(StepTemplateNano):
    story = [
        ("We haven't checked out the {{bb:restaurant}} yet.\n"),
        ("Let's {{lb:go}} into the {{bb:restaurant}}.")
    ]

    start_dir = "~/town/east"
    end_dir = "~/town/east/restaurant"

    hints = [
        ("{{rb:Use}} {{yb:cd restaurant}} {{rb:to go into the restaurant.}}")
    ]

    companion_speech = (("Eleanor: {{Bb:Ooh, do you think they'll have a sandwich anywhere?}}"))

    def block_command(self, line):
        return unblock_cd_commands(line)

    def __next__(self):
        return 28, 3


class Step3(StepTemplateNano):
    story = [
        ("You and {{bb:Eleanor}} walk into the {{bb:restaurant}}.\n"),
        ("Look around {{lb:closely}}.")
    ]

    start_dir = "~/town/east/restaurant"
    end_dir = "~/town/east/restaurant"

    hints = [
        ("Eleanor: {{Bb:Do you remember how you found me? You used}} {{yb:ls -a}} {{Bb:right?}}")
    ]

    commands = [
        "ls -a"
    ]

    deleted_items = ["~/town/east/Eleanor"]
    file_list = [
        {
            "path": "~/town/east/restaurant/Eleanor",
            "contents": get_story_file("Eleanor"),
            "type": "file"
        }
    ]

    companion_speech = ("Eleanor: {{Bb:It seems really empty here...}}")

    def __next__(self):
        return 28, 4


class Step4(StepTemplateNano):
    story = [
        ("Do you see the {{bb:.cellar}}?\n"),
        ("Let's {{lb:go}} into the {{bb:.cellar}}.")
    ]

    start_dir = "~/town/east/restaurant"
    end_dir = "~/town/east/restaurant/.cellar"

    hints = [
        ("{{rb:Go in the wine cellar using}} {{yb:cd .cellar}}{{rb:.}}")
    ]

    companion_speech = ("Eleanor: {{Bb:I'm scared...can you hold my hand?}}")

    def block_command(self, line):
        return unblock_cd_commands(line)

    def __next__(self):
        return 28, 5


class Step5(StepTemplateNano):
    story = [
        ("{{bb:Eleanor}} grabs your hand, and the two of you walk into the {{bb:cellar}}.\n"),
        ("{{lb:Look around.}}")
    ]

    start_dir = "~/town/east/restaurant/.cellar"
    end_dir = "~/town/east/restaurant/.cellar"

    hints = [
        ("{{rb:Look around with}} {{yb:ls}}{{rb:.}}")
    ]

    deleted_items = ["~/town/east/restaurant/Eleanor"]
    file_list = [
        {
            "path": "~/town/east/restaurant/.cellar/Eleanor",
            "contents": get_story_file("Eleanor"),
            "type": "file"
        }
    ]
    commands = [
        "ls",
        "ls -a"
    ]

    companion_speech = ("Eleanor: {{Bb:\"...is there someone there?\"}}")


    def __next__(self):
        return 28, 6


class Step6(StepTemplateNano):
    story = [
        ("You see a woman {{bb:Clara}} in the {{bb:cellar}}.\n"),
        ("{{lb:Listen}} to what she has to say.")
    ]

    start_dir = "~/town/east/restaurant/.cellar"
    end_dir = "~/town/east/restaurant/.cellar"

    hints = [
        ("{{rb:Use}} {{yb:cat}} {{rb:to listen what she has to say.}}"),
        ("{{rb:Use}} {{yb:cat Clara}} {{rb:to listen to Clara.}}")
    ]

    commands = [
        "cat Clara"
    ]
    companion_speech = ("Eleanor: {{Bb:\"...oh! I think I recognise that woman!\"}}")

    def __next__(self):
        return 29, 1
