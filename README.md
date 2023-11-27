# CS5252 Final Project

## Overview

## Context-Free Grammar Representation

All grammar should be stored in .gmma files. In .gmma files, use %A, %B, etc., to represent variables. If necessary, %{A0}, %{A1}, etc., might be used to represent variables A0, A1. Anything not starting with symbol % is considered character by default. At the top of the file, User must specify their starting variable in a seperate line, where % should also be used. 

## Context-Free Grammar Example

'''

%S

%S->0%S0|1%S1|0|1

'''

## Push-Down Automata Representation
