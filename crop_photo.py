#!/usr/bin/env python3
"""
Recadre la photo de signature : réduit l'espace vide en haut et sur les côtés
pour que le visage soit plus centré et prominent.
"""
from PIL import Image

path = "David Chiche.png"
img = Image.open(path)
w, h = img.size

# Retirer ~12% en haut, ~8% à gauche/droite, ~5% en bas (visage plus centré)
left = int(w * 0.08)
top = int(h * 0.12)
right = int(w * 0.92)
bottom = int(h * 0.95)

cropped = img.crop((left, top, right, bottom))
cropped.save(path, "PNG", optimize=True)
print("Photo recadrée et enregistrée.")
