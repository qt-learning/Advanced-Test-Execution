# -*- coding: utf-8 -*-

import names


def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o5_Text))
    mouseClick(waitForObject(names.oPlus_Text))
    mouseClick(waitForObject(names.o6_Text))
    mouseClick(waitForObject(names.oEqual_Text))
    test.compare(str(waitForObjectExists({"container": names.listView_Item, "type": "Text", "text": 11}).text), "11")