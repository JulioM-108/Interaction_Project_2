from typing import Optional, Tuple, Dict, Union
class StoryNode:
    def __init__(self, text: str, sound: Optional[str] = None, position=Union[str, Tuple[float, float, float]], choices: Optional[Dict[str, str]] = None):
        self.text = text
        self.sound = sound   
        self.position = position
        self.choices = choices if choices else {}


class Story:
    def __init__(self):
        self.nodes = self._create_story()
        self.current = "welcome"

    def _create_story(self):
        return {
            "welcome": StoryNode(
                text="=== Bienvenido al Sanatorio 'El Lamento' ===\n\n"
                     "Eres Alex, un periodista en busca de la verdad del Proyecto Morfeo...\n\n"
                     "Presiona 'Comenzar' para entrar al sanatorio.",
                sound=None,
                position="center",
                choices={"Comenzar": "start"}
            ),

            "start": StoryNode(
                text="La lluvia golpea con fuerza la capucha de tu impermeable.",
                sound="RAIN",
                position="center",
                choices={"Continuar": "node2"}
            ),
            "node2": StoryNode(
                text="Un trueno retumba, iluminando la silueta decrépita del sanatorio.",
                sound="DISTANT_THUNDER",
                position=(5, 0, 0),
                choices={"Continuar": "node3"}
            ),
            "node3": StoryNode(
                text="Empujas la reja de hierro. Se cierra de golpe detrás de ti.",
                sound="IRON_GATE",
                position="back",
                choices={"Continuar": "node6"}
            ),
            "node6": StoryNode(
                text="La puerta principal de madera está entreabierta. La empujas con un crujido.",
                sound="DOOR_CREAKING",
                position="front",
                choices={"Continuar": "node12"}
            ),
            "node12": StoryNode(
                text="¡Cuidado! puedes tomar dos decisiones, pero recuerda que puede ser la última:\n"
                     "1. Tomar las escaleras.\n"
                     "2. Bajar al sótano.",
                sound=None,
                choices={
                    "Subir las escaleras": "stairs15",
                    "Bajar al sótano": "basement15"
                }
            ),

            "stairs15": StoryNode(
                text="Una risa infantil resuena desde las escaleras.",
                sound="CREEPY_LITTLE",
                position=(10, 10, 0),
                choices={"Continuar": "stairs23"}
            ),
            "stairs23": StoryNode(
                text="Cada escalón de madera cruje bajo tu peso.",
                sound="CREAKING_STAIRS",
                position=(0, -10, 0),
                choices={"Continuar": "stairs29"}
            ),
            "stairs29": StoryNode(
                text="Encuentras el diario de una enfermera que habla del 'Proyecto Morfeo'.\n"
                     "La melodía de una caja de música es la clave.",
                sound="CREEPY_OLD_BOX",
                position="center",
                choices={"Continuar": "stairs30"}
            ),
            "stairs30": StoryNode(
                text="La caja fuerte se abre con un clic. Dentro está la cinta maestra del Proyecto Morfeo.",
                sound="SAFE_OPEN",
                position="center",
                choices={"Continuar": "stairs31"}
            ),
            "stairs31": StoryNode(
                text="Los susurros infantiles te rodean: 'No te la llevarás'.\n"
                     "¿Qué haces?",
                sound="CHILD_WHISPERS",
                position="center",
                choices={
                    "Dejar la cinta": "bad_ending",
                    "Aferrarte y saltar por la ventana": "good_ending"
                }
            ),

            "basement15": StoryNode(
                text="Un zumbido eléctrico constante emana del sótano.",
                sound="ELECTRIC_TRANSFORMER_HUM",
                position=(-10, -10, 0),
                choices={"Continuar": "basement27"}
            ),
            "basement27": StoryNode(
                text="Abres la puerta al sótano. El olor a ozono es intenso.",
                sound="SCARY_SQUEAKY_DOOR",
                position="front",
                choices={"Continuar": "basement31"}
            ),
            "basement31": StoryNode(
                text="Encuentras un informe del Proyecto Morfeo junto al panel de control.",
                sound="PAPER_RUSTLE",
                position="center",
                choices={"Continuar": "basement32"}
            ),
            "basement32": StoryNode(
                text="Reactivas el generador. Las cerraduras del sanatorio se abren.",
                sound="GENERATOR_DOOR",
                position="center",
                choices={"Continuar": "basement35"}
            ),
            "basement35": StoryNode(
                text="El Alcaide aparece y carga hacia ti. Hay dos caminos:\n"
                     "1. Escalera principal.\n"
                     "2. Escotilla de mantenimiento.",
                sound="MONSTER_ROAR",
                position="back",
                choices={
                    "Correr a la escalera principal": "bad_ending",
                    "Meterse en el túnel": "good_ending"
                }
            ),
            "good_ending": StoryNode(
                text="Escapas herido pero vivo. Afuera amanece, con sirenas acercándose.\n"
                     "Has logrado salir con la prueba del Proyecto Morfeo.",
                sound="WINNING_SOUND",
                position="center",
                choices={"Continuar": "Final"}
            ),
            "bad_ending": StoryNode(
                text="Crees estar a salvo, pero el sanatorio reclama otra víctima.\n"
                     "Tu voz se une a los lamentos del lugar.",
                sound="LAMENTING_MAN",
                position="center",
                choices={"Continuar": "Final"}
            ),
            "Final": StoryNode(
                text="\nFin de la historia \n",
                sound=None,
                position="center",
            ),
        }

    def get_current(self):
        return self.nodes[self.current]

    def choose(self, option):
        if option in self.nodes[self.current].choices:
            self.current = self.nodes[self.current].choices[option]

    def next_node(self):
        choices = self.nodes[self.current].choices
        if choices:
            self.current = list(choices.values())[0]
