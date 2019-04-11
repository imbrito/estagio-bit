#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import permutations

def combinatorial_analysis(value):
    '''
    Utilizando os métodos de programação funcional, complete o método combinatorial_analysis e caso de teste, de modo que o mesmo receba como 
    parâmetro um número inteiro positivo N (0 < N < 1000), e retorne uma lista com as combinações possíveis para os algarismos 
    que compõem N, observando ainda as seguintes restrições: 
        ( i ) não devem ser considerados no resultado números, iniciados por 0; 
        ( ii ) não devem ser geradas combinações repetidas;

        Exemplo: 120 -> [102, 120, 201, 210]

    Para gerar as combinações possíveis, utilize o método permutations do módulo itertools, visite o link:
    https://docs.python.org/3.7/library/itertools.html#itertools.permutations

    '''
    x = str(value)
    y = list(x)
    z = map(lambda x: ''.join(x), permutations(y, len(y)))
    w = list(set(z))
    
    # sort combinations
    k = list(filter(lambda x: not x.startswith('0'), w))
    result = list(map(int, k))
    # delete numbers starts with 0
    # while(combinations[0].startswith('0')): combinations.pop(0)
    
    result.sort()
    return result