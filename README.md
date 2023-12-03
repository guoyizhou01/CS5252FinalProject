# CS5252 Final Project

## Overview

The final project is to prove the equivlance of Context-Free Grammars and Push-Down Automata. The program included in the project is a parser that converts any Context-Free Grammar to Push-Down Automata. 

## Context-Free Grammar Representation

All grammar should be stored in .gmma files (it would be confusing to use .cfg since .cfg usually means config file). In .gmma files, use %A, %B, etc., to represent variables. If necessary, %{A0}, %{A1}, etc., might be used to represent variables A0, A1. Anything not starting with symbol % is considered character by default. At the top of the file, User must specify their starting variable in a seperate line, where % should also be used. 

## Context-Free Grammar Example

```
%S
%S->0%S0|1%S1|0|1
```
## Push-Down Automata Example

```
Start state: q_START
δ(q_START,ε,ε)=δ(q_%S_0,{ACCEPT})
δ(q_%S_0,ε,ε)=δ(q_%S_0,%S_1)
δ(q_%S_0,ε,ε)=δ(q_%S_2,ε)
δ(q_%S_1,1,%S_1)=δ(q_%S_1,ε)
δ(q_%S_1,1,{ACCEPT})=δ(q_END,ε)
δ(q_%S_2,ε,%S_1)=δ(q_%S_1,ε)
δ(q_%S_2,ε,{ACCEPT})=δ(q_END,ε)
Accept by empty stack only
```
