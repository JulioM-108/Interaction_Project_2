from openal import oalOpen, Listener
import threading
from pathlib import Path
from typing import Tuple, Dict

Position = Tuple[float, float, float]

POSITION_MAP: Dict[str, Position] = {
    "left":  (-10, 0, 0),
    "right": ( 10, 0, 0),
    "back":  ( 0, 0, -10),
    "front": ( 0, 0, 10),
    "center":( 0, 0, 0),
}

class SoundManager:
    def __init__(self):
        self.listener = Listener()
        self.listener.set_position((0, 0, 0))             
        self.listener.set_orientation((0, 0, 1, 0, 1, 0)) 
        self.master_gain = 1.0
        self.bg_gain = 0.2     
        self.sfx_gain = 0.8     

        self.background = None
        self.current_sfx = None

    def master_volume(self, gain: float):
        self.master_gain = max(0.0, min(1.0, gain))
        if self.background:
            self.background.set_gain(self.bg_gain * self.master_gain)
        if self.current_sfx:
            self.current_sfx.set_gain(self.sfx_gain * self.master_gain)

    def background_volume(self, gain: float):
        self.bg_gain = max(0.0, min(1.0, gain))
        if self.background:
            self.background.set_gain(self.bg_gain * self.master_gain)

    def set_sfx_volume(self, gain: float):
        self.sfx_gain = max(0.0, min(1.0, gain))
        if self.current_sfx:
            self.current_sfx.set_gain(self.sfx_gain * self.master_gain)

    def play_background(self, path: Path, loop=True, gain=None):
        def _bg():
            try:
                if self.background:
                    self.background.stop()
                    self.background = None

                snd = oalOpen(str(path))
                snd.set_looping(loop)

                if gain is not None:
                    self.bg_gain = max(0.0, min(1.0, gain))

                snd.play()
                snd.set_gain(self.bg_gain * self.master_gain)
                self.background = snd
            except Exception as e:
                print(f"[Error en música de fondo {path}] {e}")

        threading.Thread(target=_bg, daemon=True).start()

    def stop_background(self):
        if self.background:
            self.background.stop()
            self.background = None

    def play(self, path: Path, position="center", gain=None, exclusive=True):
        def _play():
            try:
                if exclusive and self.current_sfx:
                    self.current_sfx.stop()
                snd = oalOpen(str(path))  
                coords = POSITION_MAP.get(position, POSITION_MAP["center"])
                snd.set_position(coords)

                eff_gain = self.sfx_gain if gain is None else max(0.0, min(1.0, gain))
                snd.play()
                snd.set_gain(eff_gain * self.master_gain)

                self.current_sfx = snd
            except Exception as e:
                print(f"[Error reproduciendo {path}] {e}")

        threading.Thread(target=_play, daemon=True).start()
