# challenge_3.py
#
# Copyright (C) 2014-2016 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2
#
# A chapter of the story

from linux_story.StepTemplate import StepTemplate
from linux_story.story.terminals.terminal_cat import TerminalCat


class StepTemplateCat(StepTemplate):
    TerminalClass = TerminalCat


class Step1(StepTemplateCat):
    story = [
        ("Love it! Put it on quickly."),
        ("There's loads more interesting stuff in your room.\n"),
        ("Let's {{lb:look}} in your {{bb:shelves}} using {{yb:ls}}.\n")
    ]
    start_dir = "~/my-house/my-room"
    end_dir = "~/my-house/my-room"
    commands = ["ls shelves", "ls shelves/"]
    hints = [("{{rb:Type}} {{yb:ls shelves/}} {{rb:to look at your books.}}")]

    def __next__(self):
        return 3, 2


class Step2(StepTemplateCat):
    story = [
        ("Did you know you can use the {{ob:TAB}} key to speed up your typing?"),
        ("Try it by checking out that {{bb:comic book}}.\n"),
        ("{{lb:Examine}} it with {{yb:cat shelves/comic-book}}\n"),
        ("Press the {{ob:TAB}} key before you've finished typing!\n")
    ]
    start_dir = "~/my-house/my-room"
    end_dir = "~/my-house/my-room"
    commands = "cat shelves/comic-book"
    hints = [("{{rb:Type}} {{yb:cat shelves/comic-book}} {{rb:to read the comic.}}")]

    def __next__(self):
        return 3, 3


class Step3(StepTemplateCat):
    story = [
        ("Why is it covered in pawprints?"),
        ("Hang on, can you see that? There's a {{bb:note}} amongst your books.\n"),
        ("{{lb:Read}} the {{bb:note}} using {{yb:cat}}.\n")
    ]
    start_dir = "~/my-house/my-room"
    end_dir = "~/my-house/my-room"
    commands = "cat shelves/note"
    hints = [("{{rb:Type}} {{yb:cat shelves/note}} {{rb:to read the note.}}")]

    def __next__(self):
        return 4, 1
