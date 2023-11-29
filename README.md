# CS5252 Final Project

## Overview

## Context-Free Grammar Representation

All grammar should be stored in .gmma files (it would be confusing to use .cfg since .cfg usually means config file). In .gmma files, use %A, %B, etc., to represent variables. If necessary, %{A0}, %{A1}, etc., might be used to represent variables A0, A1. Anything not starting with symbol % is considered character by default. At the top of the file, User must specify their starting variable in a seperate line, where % should also be used. 

## Context-Free Grammar Example

```
%S
%S->0%S0|1%S1|0|1
```

## Push-Down Automata Representation

All automata should be stored in .pda files. In the file, just like what we used in context-free grammar files, symbol % need to be used for stack symbols, and brackets might be used, e.g., %A, %B, %{A0}. It's a general rule that a stack symbol should starts with a capitalized letter. Both symbols @ and δ are accepted as push-down automata, both symbols ~ and ε are accepted as epsilon. A transition can be written as follows:

```
δ(q0,a,ε)=δ(q0,%A)
```
