from src.Story import Story
from src.sound import SoundManager
from src.Resources import get_audio


class Game:
    def __init__(self):
        self.story = Story()
        self.sound_manager = SoundManager()
        self.running = True

    def start(self):
        bg = get_audio("BACKGROUND_MUSIC")
        if bg:
            self.sound_manager.play_background(
                str(bg["path"]),
                loop=bg.get("loop", True),
                gain=bg.get("gain", 0.2)
            )

        while self.running:
            node = self.story.get_current()
           
            print("\n" + "-" * 50)
            print(node.text)
          
            if node.sound:
                meta = get_audio(node.sound)
                if meta:
                    self.sound_manager.play(str(meta["path"]), node.position)
                else:
                    self.sound_manager.play(node.sound, node.position)
        
            if node.choices:
                print("\nOpciones:")
                for i, option in enumerate(node.choices.keys(), start=1):
                    print(f"{i}. {option}")

                choice = input("\nElige una opción: ")
                try:
                    choice_idx = int(choice) - 1
                    option = list(node.choices.keys())[choice_idx]
                    self.story.choose(option)
                except (ValueError, IndexError):
                    print("Opción inválida, intenta de nuevo.")
            elif self.story.current == "Final":
                break
            else:
                input("\nPresiona Enter para continuar...\n")
                self.story.next_node()
