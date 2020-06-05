# Implementación de patrones Abstract Factory y Builder
## Integrantes
- Brayan Alejandro Puentes Camargo - 20181020044
- Johnatan Guillermo Ruiz Bautista - 20181020034
- Juan Camilo Ramírez Rátiva - 20181020089

## Diagrama UML
![alt text](https://github.com/jgruizba/Mdlpygame/blob/master/personajeWW.jpg)

## Descripción del programa
<p align= "Justify">Este programa simula el movimiento de un objeto 2d que puede representar 3 clases diferentes, las cuales son: guerrero, mago, monstruo. Estos pueden interactuar con las funciones básicas de movimiento.</p>

## Requisitos
<p align= "Justify">Este programa fue diseñado en Python 3.7.3, para poder ejecutar correctamente el programa asegúrese de tener instalado el módulo pygame.</p>

## Principios de diseño

1. **Principio Liskov**
<p align= "Justify">En este software se puede observar analizar como este principio participa en la implementación de las herencias de la clase CharacterFactory, debido a que todas las clases derivadas también pueden ser tratadas como la propia clase base, Esto significa que los objetos deben poder ser reemplazados por instancias de sus subtipos sin alterar el correcto funcionamiento del sistema o lo que es lo mismo.</p>

2. **Principio Responsabilidad única**
<p align= "Justify">Este principio dice que una clase tiene una, y solo una, razón para cambiar. Cómo podemos observar el programa deja a sus clases una y solo un objetivo de ejecución o responsabilidad, logrando así tener un bajo acoplamiento entre dichas clases.</p>

3. **Principio Abierto-Cerrado**
<p align= "Justify">Como se puede observar este principio trata que las clases deben estar abiertos para las extensiones, pero cerrado para las modificaciones del código fuente. Este programa cumple el principio debido a que como podemos observar la clase "CharacterFactory" se instancia en la clase "Animación", pero esta no puede modificar el funcionamiento de "CharacterFactory”. Es decir, que el diseño del programa debe está abierto para poderse extender, pero cerrado para poder realizar modificaciones de su código fuente.</p>

## Patrones de diseño

1. **Abstract Factory**
<p align= "Justify">En el abstract factory podemos determinar en nuestro programa las clases abstractas ChracterFactory y CharacterBuilder perteneces a fabricas abstractas que nos permiten crear un conjunto de objetos que dependen mutuamente sin la necesidad de especificar un objeto en concreto.</p>

2. **Builder**
<p align= "Justify">Este patrón nos permite a través de la clase CharacterBuilder crear objetos complejos mediante el recurso de objetos más simples, y debido a esto, poder construir paso a paso con el fin de poderlo crear varias veces.</p>




