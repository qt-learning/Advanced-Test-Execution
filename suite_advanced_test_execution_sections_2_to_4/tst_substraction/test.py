# -*- coding: utf-8 -*-

import names


def main():
    startApplication("calqlatr")
    mouseClick(waitForObject(names.o3_Text))
    mouseClick(waitForObject(names.oMinus_Text))
    mouseClick(waitForObject(names.o4_Text))
    mouseClick(waitForObject(names.oEqual_Text))
    test.compare(str(waitForObjectExists({"container": names.listView_Item, "type": "Text", "text": -1}).text), "-1")