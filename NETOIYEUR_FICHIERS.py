import os
import tkinter as tk
from tkinter import filedialog, scrolledtext


class EmptyFileSweeper:
    def __init__(self, master):
        self.master = master
        master.title("Balayeur de Fichiers Vides")
        master.geometry("560x460")
        master.minsize(400, 320)
        master.configure(bg="#37474f")

        header = tk.Frame(master, bg="#37474f")
        header.pack(fill="x", padx=16, pady=(16, 6))

        title_lbl = tk.Label(
            header, text="Nettoyage de dossier",
            font=("Segoe UI", 13, "bold"),
            bg="#37474f", fg="#eceff1"
        )
        title_lbl.pack(side="left")

        pick_btn = tk.Button(
            header, text="Parcourir...",
            bg="#00897b", fg="white", relief="groove", bd=2,
            font=("Segoe UI", 10), padx=14, pady=4,
            command=self.select_and_sweep
        )
        pick_btn.pack(side="right")

        self.status_lbl = tk.Label(
            master, text="Aucun dossier analysé pour le moment.",
            font=("Segoe UI", 9, "italic"),
            bg="#37474f", fg="#b0bec5", anchor="w"
        )
        self.status_lbl.pack(fill="x", padx=18, pady=(0, 10))

        log_frame = tk.Frame(master, bg="#263238", bd=2, relief="ridge")
        log_frame.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        self.log = scrolledtext.ScrolledText(
            log_frame, wrap=tk.WORD, bd=0, font=("Consolas", 10),
            bg="#263238", fg="#c8e6c9", insertbackground="white"
        )
        self.log.pack(fill="both", expand=True, padx=4, pady=4)

        self.deleted_count = 0

    def select_and_sweep(self):
        target = filedialog.askdirectory()
        if target:
            self.status_lbl.config(text=f"Dossier sélectionné : {target}")
            self.sweep_directory(target)

    def sweep_directory(self, target):
        self.log.delete("1.0", tk.END)
        self._log_line(f"Analyse en cours: {target}\n")
        self.master.update()

        self.deleted_count = 0

        self._remove_empty_files(target)
        self._remove_empty_folders(target)

        self._log_line(f"\nOpération terminée. {self.deleted_count} élément(s) supprimé(s).\n")
        self.status_lbl.config(text=f"Terminé — {self.deleted_count} élément(s) supprimé(s).")

    def _remove_empty_files(self, target):
        for current_dir, _subdirs, files in os.walk(target):
            for name in files:
                full_path = os.path.join(current_dir, name)
                self._try_delete_file(full_path)

    def _try_delete_file(self, full_path):
        try:
            if os.path.getsize(full_path) == 0:
                os.remove(full_path)
                self._log_line(f"Fichier vide supprimé: {full_path}\n")
                self.deleted_count += 1
        except OSError as err:
            self._log_line(f"Échec: {full_path} ({err})\n")

    def _remove_empty_folders(self, target):
        for current_dir, _subdirs, _files in os.walk(target, topdown=False):
            if current_dir == target:
                continue
            self._try_delete_folder(current_dir)

    def _try_delete_folder(self, folder_path):
        try:
            if not os.listdir(folder_path):
                os.rmdir(folder_path)
                self._log_line(f"Dossier vide supprimé: {folder_path}\n")
                self.deleted_count += 1
        except OSError as err:
            self._log_line(f"Échec: {folder_path} ({err})\n")

    def _log_line(self, text):
        self.log.insert(tk.END, text)


def main():
    root = tk.Tk()
    EmptyFileSweeper(root)
    root.mainloop()


if __name__ == "__main__":
    main()