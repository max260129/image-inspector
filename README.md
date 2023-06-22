# Image Inspector

## Description
Image Inspector est un projet codé en Python qui vous permet d'inspecter les images pour obtenir des informations sur leur contenu. Le projet est divisé en deux parties :

1. **Extraction de métadonnées** : Cette partie du projet utilise la bibliothèque `exiftool` pour extraire les métadonnées d'une image. Ces métadonnées peuvent inclure des informations comme la date de création de l'image, l'appareil utilisé pour la prendre, et dans certains cas, l'emplacement géographique où l'image a été prise.

2. **Stéganographie** : Cette partie du projet utilise la bibliothèque `steghide` pour cacher des données secrètes dans une image. Les données sont cachées de manière à ce qu'elles ne soient pas perceptibles à l'œil nu.

## Installation
Pour installer les outils, exécutez les commandes suivantes dans le terminal :
```
sudo apt install exiftool
sudo apt install strings
```

## Utillisation
```
pythyon3 main.py <flag> <image>

ex: python3 main.py -map image.jpeg
ex: python3 main.py -steg image.jpeg
```

## Licence

Lemsle Maxence
