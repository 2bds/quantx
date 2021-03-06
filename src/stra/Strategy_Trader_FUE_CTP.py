
# -*- coding: utf-8 -*-

# Copyright (c) 2018-2018 the QuantX authors
# All rights reserved.
#
# The project sponsor and lead author is Xu Rendong.
# E-mail: xrd@ustc.edu, QQ: 277195007, WeChat: ustc_xrd
# You can get more information at https://xurendong.github.io
# For names of other contributors see the contributors file.
#
# Commercial use of this code in source and binary forms is
# governed by a LGPL v3 license. You may get a copy from the
# root directory. Or else you should get a specific written 
# permission from the project author.
#
# Individual and educational use of this code in source and
# binary forms is governed by a 3-clause BSD license. You may
# get a copy from the root directory. Certainly welcome you
# to contribute code of all sorts.
#
# Be sure to retain the above copyright notice and conditions.

from math import ceil, floor

import strategy_base
import panel_trader_fue_ctp

class Strategy_Trader_FUE_CTP(strategy_base.StrategyBase):
    def __init__(self):
        strategy_base.StrategyBase.__init__(self, "Strategy_Trader_FUE_CTP", "Trader_FUE_CTP", "手动交易-期货-CTP")
        self.log_cate = "Strategy_Trader_FUE_CTP"
        self.panel = panel_trader_fue_ctp.Panel(strategy = self.strategy)

    def OnDoubleClick(self):
        self.panel.show()

    def OnWorking(self): # 供具体策略继承调用，在 运行 前执行一些操作
        self.panel.OnWorking()

    def OnSuspend(self): # 供具体策略继承调用，在 暂停 前执行一些操作
        pass

    def OnContinue(self): # 供具体策略继承调用，在 继续 前执行一些操作
        pass

    def OnTerminal(self): # 供具体策略继承调用，在 停止 前执行一些操作
        self.panel.OnTerminal()

    def OnTraderEvent(self, trader, ret_func, task_item): # 交易模块事件通知，供具体策略继承调用
        self.panel.OnTraderEvent(trader, ret_func, task_item)
