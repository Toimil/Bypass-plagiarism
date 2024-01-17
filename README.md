# Bypass Plagiarism Programs

Este script permite eludir la mayoría de los controles de plagio, que se utilizan a menudo en la educación, sin que notifiquen plagio aún teniendo el mismo texto que otra persona.

## ¿Cómo funciona?

Los programas de plagio normalmente comparan textos para buscar coincidencias entre ellos, mediante este programa dispondremos de dos útiles funciones para eludirlos:
* **Homóglifos**: se emplea esta palabra para referirse a caracteres que visualmente aparentan ser idénticos pero que en realidad son diferentes. Mediante ellos, conseguimos cambiar los caracteres de todo el texto por otros que parecen los mismos pero que difieren del texto original.
* **Patrón Braille en blanco**: este caracter casi invisible se utiliza en el lenguaje braille y a simple vista no se consigue distinguir. Gracias a él, meteremos estos *espacios invisibles* entre las letras del texto que queramos plagiar pero visualmente lo veremos igual que el original.

Debido a lo descrito anteriormente, conseguiremos textos igual que los originales visualmente pero que difieren en el contenido aunque uno no se puede dar cuenta de ello y que, al ser distintos, pasaran sin ningún problema los programas de plagio.

## Compilación y ejecución

### Prerrequisitos

Necesitarás disponer de:

* Un espacio de trabajo con **Python3**.


### Ejecución del script

1. Clona este repositorio en tu sistema mediante ```git clone https://github.com/Toimil/Bypass-plagiarism``` o descárgalo colocando todos los archivos en el mismo directorio.

2. Ejecuta el script mediante el comando **```python3 bypass_plagiarism.py```**, el cual te preguntará las funcionalidades que deseas utilizar así como si el texto a cambiar se encuentra en un fichero o lo vas a introducir manualmente.


## Hecho con

* [Python 3](https://www.python.org/)

## Autor

* **Óscar Toimil** - [Toimil](https://github.com/Toimil)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
