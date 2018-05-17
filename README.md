# Tradutor

Script para traducir automaticamente un ficheiro de gettext empregando o sistema de tradución automatica Apertium.
Traduce do Inglés ao Galego, outras linguaxes requiren editar o script (ningunha complexidade).

## Instalación

O script emprega a libraría de Python __polib__ e fai chamadas ao sistema invocando o comando de apertium.

```bash
sudo apt-get install apertium apertium-en-es apertium-es-pt apertium-pt-gl apertium-es-gl
sudo pip install polib
```

## Uso

```bash
python tradutor.po /ruta/ficheiro.po
```

## Referencias

* [Apertium](https://www.apertium.org)
* [polib](https://pypi.org/project/polib/)