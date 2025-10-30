#!/usr/bin/env python3
"""
Script pour créer un GIF animé à partir des captures d'écran conda
"""
from PIL import Image
import sys

def create_conda_gif(image_paths, output_path, durations):
    """
    Crée un GIF animé à partir d'une liste d'images.

    Args:
        image_paths: Liste des chemins vers les images
        output_path: Chemin de sortie pour le GIF
        durations: Liste des durées en ms pour chaque frame (ou durée unique)
    """
    try:
        # Charger toutes les images
        images = []
        for img_path in image_paths:
            img = Image.open(img_path)
            images.append(img)
            print(f"[OK] Charge: {img_path} ({img.size[0]}x{img.size[1]})")

        # Créer le GIF
        images[0].save(
            output_path,
            save_all=True,
            append_images=images[1:],
            duration=durations,  # millisecondes par frame
            loop=0,  # boucle infinie
            optimize=False  # garde la qualité maximale
        )

        print(f"\n[OK] GIF cree avec succes: {output_path}")
        print(f"  Nombre de frames: {len(images)}")
        print(f"  Dimensions: {images[0].size[0]}x{images[0].size[1]}")

        # Afficher la taille du fichier
        import os
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"  Taille: {size_mb:.2f} MB")

    except Exception as e:
        print(f"[ERREUR] {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Chemins des images (dans l'ordre fourni par l'utilisateur)
    image_files = [
        "docs/images/GIF/Frame 1.png",  # PowerShell prompt de base
        "docs/images/GIF/Frame 2.png",  # mamba install seaborn
        "docs/images/GIF/Frame 3.png",  # conda list (longue liste)
        "docs/images/GIF/Frame 4.png",  # conda env list + activate
        "docs/images/GIF/Frame 5.png"   # conda env list
    ]

    # Durées en millisecondes pour chaque frame
    frame_durations = [
        800,   # Frame 1: prompt de base (0.8s)
        1200,  # Frame 2: mamba install (1.2s)
        1200,  # Frame 3: conda list (1.2s)
        1200,  # Frame 4: activation (1.2s)
        800    # Frame 5: env list final (0.8s)
    ]

    output_file = "docs/images/conda-commands.gif"

    print("Creation du GIF anime conda...")
    print("=" * 60)
    create_conda_gif(image_files, output_file, frame_durations)
    print("=" * 60)
