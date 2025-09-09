from openal import oalOpen, Listener, oalQuit
import threading

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

    # ---------- Reproduction ----------
    def play_background(self, filename, loop=True, gain=None):
        def _bg():
            try:
                if self.background:
                    self.background.stop()
                    self.background = None

                snd = oalOpen(f"sounds/{filename}")
                if loop:
                    snd.set_looping(True)

                if gain is not None:
                    self.bg_gain = max(0.0, min(1.0, gain))

                snd.play()
                snd.set_gain(self.bg_gain * self.master_gain)
                self.background = snd
            except Exception as e:
                print(f"[Error en música de fondo {filename}] {e}")

        threading.Thread(target=_bg, daemon=True).start()

    def stop_background(self):
        if self.background:
            self.background.stop()
            self.background = None

    def play(self, filename, position="center", gain=None, exclusive=True):
        def _play():
            try:
                if exclusive and self.current_sfx:
                    self.current_sfx.stop()

                snd = oalOpen(f"sounds/{filename}")

                # General Positions in 3D..
                if position == "left":
                    snd.set_position((-10, 0, 0))
                elif position == "right":
                    snd.set_position((10, 0, 0))
                elif position == "back":
                    snd.set_position((0, 0, -10))
                elif position == "front":
                    snd.set_position((0, 0, 10))
                else:
                    snd.set_position((0, 0, 0))  

                eff_gain = self.sfx_gain if gain is None else max(0.0, min(1.0, gain))
                snd.play()
                snd.set_gain(eff_gain * self.master_gain)

                self.current_sfx = snd
            except Exception as e:
                print(f"[Error reproduciendo {filename}] {e}")

        threading.Thread(target=_play, daemon=True).start()
