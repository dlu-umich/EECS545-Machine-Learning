# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:16:41 2017

@author: Di LU
"""


class BRNode:
    def __init__(self, black, red, node_dict):
        self.black = black
        self.red = red
        self.node_dict = node_dict
        
    def expected_winnings(self):
        if self.red == 0 and self.black == 0:
            winnings_if_stop = 0
            winnings_if_go = 0
            
        if self.red == 0:
            winnings_if_stop = 0 - self.black
            winnings_if_go = self.node_dict.get_node(self.black-1,self.red)
            
        if self.black == 0:
            winnings_if_stop = self.red
            winnings_if_go = self.node_dict.get_node(self.black, self.red-1)
            
        else:
            winnings_if_stop = self.red - self.black
            prob_black = float(self.black)/(self.black+self.red)
            prob_red = float(self.red)/(self.black+self.red)
            winnings_if_go = float( prob_black * self.node_dict.get_node(self.black-1,self.red).expected_winnings()+\
            prob_red * self.node_dict.get_node(self.black,self.red-1).expected_winnings() )
        
        self.winnings = max(float(winnings_if_stop),float(winnings_if_go))
        
        return self.winnings
    
class NodeDict:
    def __init__(self):
        self.black_and_red_node_dict = {}
        
    def get_node(self, black, red):
        key = (black, red)
        if key not in self.black_and_red_node_dict:
            self.black_and_red_node_dict[key] = BRNode(black, red, self)
        
        return self.black_and_red_node_dict[key]
    