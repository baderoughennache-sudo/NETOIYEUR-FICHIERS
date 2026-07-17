# Balayeur de Fichiers Vides

Une application de bureau simple, développée avec Tkinter, qui analyse un dossier et supprime automatiquement les fichiers vides ainsi que les sous-dossiers devenus vides.

## Aperçu

L'utilisateur sélectionne un dossier via une boîte de dialogue. L'application parcourt ensuite récursivement l'arborescence, supprime tout fichier de taille nulle, puis supprime les dossiers qui ne contiennent plus aucun élément. Un journal des opérations s'affiche en temps réel dans la fenêtre.

## Prérequis

- Python 3.7 ou version supérieure
- Tkinter (généralement inclus avec l'installation standard de Python)

## Installation

Aucune installation supplémentaire n'est nécessaire si Tkinter est déjà présent. Sur certaines distributions Linux, il peut être nécessaire de l'installer séparément :

```bash
sudo apt-get install python3-tk
```

## Utilisation

Exécuter le script suivant :

```bash
python nettoyeur_fichiers_vides.py
```

Cliquer sur **Parcourir...**, puis choisir le dossier à nettoyer. Le journal des suppressions et un résumé s'affichent automatiquement.

## Fonctionnalités

- Suppression récursive des fichiers de taille 0 octet
- Suppression des dossiers vides après le nettoyage des fichiers
- Journal détaillé de chaque suppression et des erreurs rencontrées
- Résumé du nombre total d'éléments supprimés

## Structure du code

Le projet est organisé autour d'une classe unique, `EmptyFileSweeper` :

- `select_and_sweep` : ouvre la boîte de dialogue et lance l'analyse
- `sweep_directory` : orchestre le nettoyage complet d'un dossier
- `_remove_empty_files` / `_try_delete_file` : suppression des fichiers vides
- `_remove_empty_folders` / `_try_delete_folder` : suppression des dossiers vides
- `_log_line` : affichage d'une ligne dans le journal

## Avertissement

Les suppressions effectuées par cette application sont définitives (aucune corbeille n'est utilisée). Il est recommandé de faire un essai sur un dossier de test avant une utilisation sur des données importantes.

## Licence

Projet libre d'utilisation à des fins d'apprentissage.
