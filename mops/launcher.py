"""
Copyright (C) 2015, MuChu Hsu
Contributed by Muchu Hsu (muchu1983@gmail.com)
This file is part of BSD license

<https://opensource.org/licenses/BSD-3-Clause>
"""
"""
程式進入點 (main)
"""
from mops.ui.dashboard import Dashboard

def entry_point():
    Dashboard().showup()


if __name__ == '__main__':
    entry_point()