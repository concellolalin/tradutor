#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Traduce unha cadea invocando ao sistema o sistema de tradución
automática apertium

Asegurarse de ter instado apertium:
sudo apt-get install apertium apertium-en-es apertium-es-pt apertium-pt-gl apertium-es-gl

Invocar o script con
python tradutor.py /ruta/ficheiro.po
"""

import os
import polib
import argparse

def traducir(cadea):
    """ Traduce unha cadea do inglés ao galego, empregando apertium

    Parámetros:
    cadea -- Cadea a traducir
    """
    cadea = polib.escape(cadea.encode('utf-8'))
    cmd = 'echo -n "%s" | apertium en-es -u | apertium es-gl -u ' % cadea

    f = os.popen(cmd)  
    traducion = f.read()    
    traducion = polib.escape(unicode(traducion, "utf-8"))

    return traducion

# Parsear os argumentos do script
parser = argparse.ArgumentParser()
parser.add_argument("ficheiro", help="ficheiro .po a procesar", type=str)
args = parser.parse_args()

po = polib.pofile(args.ficheiro)
# Traducir as cadeas pendentes de tradución
for entry in po.untranslated_entries():
    print "\33[42mmsgid:\33[0m " + entry.msgid
    traducido = traducir(entry.msgid)
    entry.msgstr = traducido
    print "\33[43mmsgstr:\33[0m " + traducido + "\n"

# Gardar nun ficheiro co prefixo auto-nome.po
po.save(u'auto-' + args.ficheiro)    
