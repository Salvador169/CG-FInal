# LAB 7

1. É um programa que renderiza 4 objetos através do mesh criado para cada objeto com as respetivas texturas [lab7.py](lab7.py)

## Requerimentos

```
Python==3.10.2
numpy==1.22.2
pycodestyle==2.8.0
pygame==2.1.2
PyOpenGL==3.1.6
PyOpenGL-accelerate==3.1.6
```

## Como executar

```
cd src10
py lab7.py
```

## Controlos

### Movimentação da Câmara
WASD - Para mover a câmara pelas respetivas posições através do eixo x e z

QE - Para rodar a câmara para a esquerda e direita no eixo y

FR - Para mover a câmara para cima e para baixo no eixo y

TG - Para rodar a câmara para a esquerda e direita no eixo x

### Movimentação do arco
Numpad 8,4,6,2 - Para mover a câmara pelas respetivas posições através do eixo x e z

Numpad 7,9 - Para rodar a câmara para a esquerda e direita no eixo y

Numpad +,- - Para mover a câmara para cima e para baixo no eixo y

Numpad 1,0 - Para rodar a câmara para a esquerda e direita no eixo x

## Ferramentas utilizadas

Para a criação da geometria do objeto foi utlizado o código disponibilizado em aula [geometry](geometry)

Para a textura da madeira foi utilizada a [imagem](https://images.pexels.com/photos/129733/pexels-photo-129733.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500)

Para a textura da corda foi utilizada a [imagem](https://cdn.wallpaperdirect.com/asset/img/product/153039/tiled/albany-ombre-string-texture-grey-gold-wallpaper-tiled-153039.jpg)

## Referências
1. Madeira, M. (2022).. Acedido a 4 de Abril  2022, em:
https://tutoria.ualg.pt/2021/mod/resource/view.php?id=121444
2. (2022) Wood, em Pexels. Acedido a 7 de Abril de 2022, em:
https://images.pexels.com/photos/129733/pexels-photo-129733.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500
3. (2022) albany-ombre-string-texture-grey-gold-wallpaper-tiled, em Wallpaperdirect. Acedido a 12 de Abril de 2022, em:
https://cdn.wallpaperdirect.com/asset/img/product/153039/tiled/albany-ombre-string-texture-grey-gold-wallpaper-tiled-153039.jpg
4. (2022) Carlos Carvalho, [Alvo](geometry/target.py)
5. (2022) David Pereira, [Tripe](geometry/tripe.py)
6. (2022) Diogo Batista, [Flecha](geometry/arrow.py)
