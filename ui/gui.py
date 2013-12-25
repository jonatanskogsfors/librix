# -*- coding: utf-8 -*-

import urwid
from datetime import datetime

class Palettes(object):
    GREEN = [
        ('body', 'dark green', 'black'),
        ('bold', 'dark green, bold', 'black'),
        ('inverted', 'black', 'dark green'),
        ('inverted-bold', 'black, bold', 'dark green'),
        ]

    BROWN = [
        ('body', 'brown', 'black'),
        ('bold', 'brown, bold', 'black'),
        ('inverted', 'black', 'brown'),
        ('inverted-bold', 'black, bold', 'brown'),
        ]

    CYAN = [
        ('body', 'dark cyan', 'black'),
        ('bold', 'dark cyan, bold', 'black'),
        ('inverted', 'black', 'dark cyan'),
        ('inverted-bold', 'black, bold', 'dark cyan'),
        ]


class UI(object):
    def __init__(self, system="-", version="-", library=None, locale=None):
        self.system = system
        self.version = version
        self.library = library
        self.locale = locale
        
    
    def start_screen(self):
        footer = Footer([("inverted-bold", "{} {}".format(self.system, self.version)), " - (C) Jonatan Lindström 2013"])
        body = Body([self.locale.MAIN_WELCOME, self.locale.MAIN_CHOOSE])
        main_screen = Screen(name=self.library.name, body=body, footer=footer)
        return main_screen


class Header(urwid.AttrMap):
    def __init__(self, text, *args, **kwargs):
        now = datetime.now()
        date_text = urwid.Text("{d.day} {d:%b} {d.year}".format(d=now).upper(), align="left")
        header_text = urwid.Text(text.upper(), align="center")
        time_text = urwid.Text("{d.hour:02}:{d.minute:02}".format(d=now), align="right")
        header_columns = urwid.Columns([date_text, header_text, time_text])
        super(Header, self).__init__(header_columns, "inverted-bold", *args, **kwargs)


class Footer(urwid.AttrMap):
    def __init__(self, text, *args, **kwargs):
        footer_text = urwid.Text(text, align="center")
        super(Footer, self).__init__(footer_text, "body", *args, **kwargs)


class Body(urwid.AttrMap):
    def __init__(self, text, *args, **kwargs):
        menu = NumberMenu(["test", "att", "göra", "meny"])
        content = urwid.Text(text, align="center")
        #colored_content = urwid.AttrMap(content, "body")
        content_filler = urwid.Filler(content, valign="top", top=1, bottom=1)
        v_padding = urwid.Padding(content_filler, left=1, right=1)
        line_box = urwid.ListBox(urwid.SimpleListWalker([content, menu]))
        super(Body, self).__init__(line_box, "body", *args, **kwargs)


class Screen(urwid.Frame):
    def __init__(self, *args, name="Sceen", body=None, footer=None, **kwargs):
        header = Header(name)
        super(Screen, self).__init__(*args, header=header, body=body, footer=footer, **kwargs)


class NumberMenu(urwid.GridFlow):
    def __init__(self, items, *args, **kwargs):
        super(NumberMenu, self).__init__([urwid.Text(txt) for txt in items], 5, 2, 2, 'left', *args, **kwargs)
           