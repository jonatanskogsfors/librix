#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Usage: librix.py [options]

Options:
-c <clr> --color=<clr>     Choose color [default: green].
-l <loc> --locale=<loc>  Choose locale [default: sv_SE]
"""

import urwid
from docopt import docopt
from ui import gui
from event_handler import EventHandler
from models.library import Library
from ui.locales.sv_SE import *
from ui.locales.en_GB import *

def main():
    arguments = docopt(__doc__)

    if arguments["--color"].lower() == "cyan":
        palette = gui.Palettes.CYAN
    elif arguments["--color"].lower() == "brown":
        palette = gui.Palettes.BROWN
    elif arguments["--color"].lower() == "green":
        palette = gui.Palettes.GREEN
    else:
        raise ValueError("Unknown color scheme.")
    
    if arguments["--locale"] == "sv_SE":
        locale = sv_SE
    elif arguments["--locale"] == "en_GB":
        locale = en_GB
    else:
        raise ValueError("Unknown locale.")
    
    main_library = Library(name="Onkel Adams bibliotek")
    
    system = "Librix"
    version = "0.1a"
    my_ui = gui.UI(system=system, version=version, library=main_library, locale=locale)
    start_screen = my_ui.start_screen()
    events = EventHandler()
    loop = urwid.MainLoop(start_screen, palette,
                          unhandled_input=events.key_pressed)
    loop.run()


if __name__ == "__main__":
    main()