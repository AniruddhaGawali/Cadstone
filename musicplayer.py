import os
import pygame
from tkinter import Tk, Button, Label, filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        self.label = Label(root, text="No file selected")
        self.label.pack(pady=10)

        self.select_button = Button(root, text="Select Music", command=self.select_music)
        self.select_button.pack(pady=5)

        self.play_button = Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=5)

        self.stop_button = Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=5)

        self.selected_music = ""
        self.playing = False

    def select_music(self):
        self.selected_music = filedialog.askopenfilename(filetypes=[("Music files", "*.mp3")])
        self.label.config(text="Selected: " + os.path.basename(self.selected_music))

    def play_music(self):
        if self.selected_music:
            if not self.playing:
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load(self.selected_music)
                pygame.mixer.music.play()
                self.playing = True
        else:
            self.label.config(text="No file selected")

    def stop_music(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False

if __name__ == "__main__":
    root = Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
