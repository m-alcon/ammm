#!/bin/bash

#AMMM Lab Heuristics v1.2
#Run the heuristic algorithm.
#Store the output log in a file and view it on the terminal.
#Copyright 2018 Luis Velasco.
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

file="chungus_1"

#echo "GREEDY"
#python3 Main.py config/greedy_X.dat > logs/${file}_greedy_X.txt
#echo "GREEDY FI"
#python3 Main.py config/greedy_FI.dat > logs/${file}_greedy_FI.txt
#echo "GREEDY BI"
#python3 Main.py config/greedy_BI.dat > logs/${file}_greedy_BI.txt
echo "GRASP"
python3 Main.py config/grasp_BI.dat > logs/${file}_grasp_BI.txt