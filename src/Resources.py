from pathlib import Path

BASE_DIR = Path(__file__).parent
AUDIO_DIR = Path(r"C:\Users\julio\OneDrive\Universidad\Noveno_Semestre\S.Interaction\M2\Interaction_Project_2\sounds")

def key_from_filename(fn: str) -> str:
    return Path(fn).stem.replace(" ", "_").upper()
AUDIO = {
    "BACKGROUND_MUSIC": {
        "path": AUDIO_DIR / "BACKGROUND_MUSIC.wav",
        "loop": False,
        "gain": 0.8
    },
    "CHILD_WHISPERS": {
        "path": AUDIO_DIR / "Child_whispers.wav",
        "loop": False,
        "gain": 0.8
    },
    "CREAKING_STAIRS": {
        "path": AUDIO_DIR / "Creaking_Stairs.wav",
        "loop": False,
        "gain": 0.8
    },
    "CREEPY_LITTLE": {
        "path": AUDIO_DIR / "Creepy_Little.wav",
        "loop": False,
        "gain": 0.8
    },
    "CREEPY_OLD_BOX": {
        "path": AUDIO_DIR / "Creepy_Old_Box.wav",
        "loop": False,
        "gain": 0.8
    },
    "DISTANT_THUNDER": {
        "path": AUDIO_DIR / "Distant_Thunder.wav",
        "loop": False,
        "gain": 0.7
    },
    "DOOR_CREAKING": {
        "path": AUDIO_DIR / "Door_Creaking.wav",
        "loop": False,
        "gain": 0.8
    },
    "ELECTRIC_TRANSFORMER_HUM": {
        "path": AUDIO_DIR / "Electric_Transformer_Hum.wav",
        "loop": True,
        "gain": 1.0
    },
    "GENERATOR_DOOR": {
        "path": AUDIO_DIR / "Generator_Door.wav",
        "loop": False,
        "gain": 0.8
    },
    "IRON_GATE": {
        "path": AUDIO_DIR / "Iron_Gate.wav",
        "loop": False,
        "gain": 0.9
    },
    "LAMENTING_MAN": {
        "path": AUDIO_DIR / "Lamenting_Man.wav",
        "loop": False,
        "gain": 0.8
    },
    "MONSTER_ROAR": {
        "path": AUDIO_DIR / "Monster_Roar.wav",
        "loop": False,
        "gain": 1.0
    },
    "PAPER_RUSTLE": {
        "path": AUDIO_DIR / "PAPER_RUSTLE.wav",
        "loop": False,
        "gain": 0.7
    },
    "RAIN": {
        "path": AUDIO_DIR / "rain.wav",
        "loop": True,
        "gain": 0.4
    },
    "SAFE_OPEN": {
        "path": AUDIO_DIR / "Safe_Open.wav",
        "loop": False,
        "gain": 0.8
    },
    "SCARY_SQUEAKY_DOOR": {
        "path": AUDIO_DIR / "Scary_Squeaky_Door.wav",
        "loop": False,
        "gain": 0.85
    },
    "WINNING_SOUND": {
        "path": AUDIO_DIR / "Winning_Sound.wav",
        "loop": False,
        "gain": 0.8
    },
}

def get_audio(key: str):
    if not key:
        return None
    return AUDIO.get(key.upper())

def validate_audio_files():
    missing = []
    for k, meta in AUDIO.items():
        p = meta["path"]
        if not p.exists():
            missing.append((k, str(p)))
    return missing
