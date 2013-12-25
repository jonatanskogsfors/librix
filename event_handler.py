# -*- coding: utf-8 -*-

import urwid

class EventHandler(object):
    def key_pressed(self, key):
        if key == 'down':
            urwid.emit_signal(self, 'beep')
        elif key.lower() == 'q':
            raise urwid.ExitMainLoop()