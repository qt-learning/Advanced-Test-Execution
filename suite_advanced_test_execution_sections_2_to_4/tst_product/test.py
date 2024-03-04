# -*- coding: utf-8 -*-

import names


def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o1_Text))
    mouseClick(waitForObject(names.oMultiply_Text))
    mouseClick(waitForObject(names.o2_Text))
    mouseClick(waitForObject(names.oEqual_Text))
    test.compare(str(waitForObjectExists({"container": names.listView_Item, "type": "Text", "text": 2}).text), "2")
