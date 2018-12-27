@echo off
cls

REM AMMM Lab Heuristics v1.2
REM Run the heuristic algorithm.
REM Store the output log in a file and view it on the terminal.
REM Copyright 2018 Luis Velasco.
REM 
REM This program is free software: you can redistribute it and/or modify
REM it under the terms of the GNU General Public License as published by
REM the Free Software Foundation, either version 3 of the License, or
REM (at your option) any later version.
REM 
REM This program is distributed in the hope that it will be useful,
REM but WITHOUT ANY WARRANTY; without even the implied warranty of
REM MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
REM GNU General Public License for more details.
REM 
REM You should have received a copy of the GNU General Public License
REM along with this program.  If not, see <http://www.gnu.org/licenses/>.

REM Python 2.7 is required.
REM This script assumes that Python is installed to C:\Python27

C:\Python27\python.exe Main.py config\bgreedy.dat > outputs\bgreedy.txt
C:\Python27\python.exe Main.py config\b1greedy.dat > outputs\b1greedy.txt
C:\Python27\python.exe Main.py config\hgreedy.dat > outputs\hgreedy.txt
C:\Python27\python.exe Main.py config\h1greedy.dat > outputs\h1greedy.txt
C:\Python27\python.exe Main.py config\h2greedy.dat > outputs\h2greedy.txt
C:\Python27\python.exe Main.py config\mgreedy.dat > outputs\mgreedy.txt
C:\Python27\python.exe Main.py config\m1greedy.dat > outputs\m1greedy.txt
C:\Python27\python.exe Main.py config\sgreedy.dat > outputs\sgreedy.txt
C:\Python27\python.exe Main.py config\s1greedy.dat > outputs\s1greedy.txt

C:\Python27\python.exe Main.py config\bgreedy_Local_N1_BI.dat > outputs\bgreedy_Local_N1_BI.txt
C:\Python27\python.exe Main.py config\b1greedy_Local_N1_BI.dat > outputs\b1greedy_Local_N1_BI.txt
C:\Python27\python.exe Main.py config\hgreedy_Local_N1_BI.dat > outputs\hgreedy_Local_N1_BI.txt
C:\Python27\python.exe Main.py config\h1greedy_Local_N1_BI.dat > outputs\h1greedy_Local_N1_BI.txt
C:\Python27\python.exe Main.py config\h2greedy_Local_N1_BI.dat > outputs\h2greedy_Local_N1_BI.txt
C:\Python27\python.exe Main.py config\mgreedy_Local_N1_BI.dat > outputs\mgreedy_Local_N1_BI.txt
C:\Python27\python.exe Main.py config\m1greedy_Local_N1_BI.dat > outputs\m1greedy_Local_N1_BI.txt
C:\Python27\python.exe Main.py config\sgreedy_Local_N1_BI.dat > outputs\sgreedy_Local_N1_BI.txt
C:\Python27\python.exe Main.py config\s1greedy_Local_N1_BI.dat > outputs\s1greedy_Local_N1_BI.txt

C:\Python27\python.exe Main.py config\bgreedy_Local_N1_FI.dat > outputs\bgreedy_Local_N1_FI.txt
C:\Python27\python.exe Main.py config\b1greedy_Local_N1_FI.dat > outputs\b1greedy_Local_N1_FI.txt
C:\Python27\python.exe Main.py config\hgreedy_Local_N1_FI.dat > outputs\hgreedy_Local_N1_FI.txt
C:\Python27\python.exe Main.py config\h1greedy_Local_N1_FI.dat > outputs\h1greedy_Local_N1_FI.txt
C:\Python27\python.exe Main.py config\h2greedy_Local_N1_FI.dat > outputs\h2greedy_Local_N1_FI.txt
C:\Python27\python.exe Main.py config\mgreedy_Local_N1_FI.dat > outputs\mgreedy_Local_N1_FI.txt
C:\Python27\python.exe Main.py config\m1greedy_Local_N1_FI.dat > outputs\m1greedy_Local_N1_FI.txt
C:\Python27\python.exe Main.py config\sgreedy_Local_N1_FI.dat > outputs\sgreedy_Local_N1_FI.txt
C:\Python27\python.exe Main.py config\s1greedy_Local_N1_FI.dat > outputs\s1greedy_Local_N1_FI.txt

C:\Python27\python.exe Main.py config\bgreedy_Local_N2_BI.dat > outputs\bgreedy_Local_N2_BI.txt
C:\Python27\python.exe Main.py config\b1greedy_Local_N2_BI.dat > outputs\b1greedy_Local_N2_BI.txt
C:\Python27\python.exe Main.py config\hgreedy_Local_N2_BI.dat > outputs\hgreedy_Local_N2_BI.txt
C:\Python27\python.exe Main.py config\h1greedy_Local_N2_BI.dat > outputs\h1greedy_Local_N2_BI.txt
C:\Python27\python.exe Main.py config\h2greedy_Local_N2_BI.dat > outputs\h2greedy_Local_N2_BI.txt
C:\Python27\python.exe Main.py config\mgreedy_Local_N2_BI.dat > outputs\mgreedy_Local_N2_BI.txt
C:\Python27\python.exe Main.py config\m1greedy_Local_N2_BI.dat > outputs\m1greedy_Local_N2_BI.txt
C:\Python27\python.exe Main.py config\sgreedy_Local_N2_BI.dat > outputs\sgreedy_Local_N2_BI.txt
C:\Python27\python.exe Main.py config\s1greedy_Local_N2_BI.dat > outputs\s1greedy_Local_N2_BI.txt

C:\Python27\python.exe Main.py config\bgreedy_Local_N2_FI.dat > outputs\bgreedy_Local_N2_FI.txt
C:\Python27\python.exe Main.py config\b1greedy_Local_N2_FI.dat > outputs\b1greedy_Local_N2_FI.txt
C:\Python27\python.exe Main.py config\hgreedy_Local_N2_FI.dat > outputs\hgreedy_Local_N2_FI.txt
C:\Python27\python.exe Main.py config\h1greedy_Local_N2_FI.dat > outputs\h1greedy_Local_N2_FI.txt
C:\Python27\python.exe Main.py config\h2greedy_Local_N2_FI.dat > outputs\h2greedy_Local_N2_FI.txt
C:\Python27\python.exe Main.py config\mgreedy_Local_N2_FI.dat > outputs\mgreedy_Local_N2_FI.txt
C:\Python27\python.exe Main.py config\m1greedy_Local_N2_FI.dat > outputs\m1greedy_Local_N2_FI.txt
C:\Python27\python.exe Main.py config\sgreedy_Local_N2_FI.dat > outputs\sgreedy_Local_N2_FI.txt
C:\Python27\python.exe Main.py config\s1greedy_Local_N2_FI.dat > outputs\s1greedy_Local_N2_FI.txt

pause
