# The Lament — Interactive Audio Narrative

Team members:
- Julio Mazo (JulioM-108)
- Miguel Sanchez (Milan08S)

If you want different or additional names, replace the line above with the real team members.

## Project description

"The Lament" is a short interactive psychological horror game set in an abandoned sanatorium. The experience combines a branching narrative with 3D spatial audio to create an immersive and tense atmosphere. Players read short narrative nodes, make decisions that branch the story, and experience environmental and positional sound effects that reinforce the mood.

## Why we made it this way (Design justification)

- We chose Python with PyOpenAL because it allowed for rapid prototyping while giving us full access to the 3D audio spatialization required for an immersive horror experience. Python's concise syntax speeds up iteration on story logic and sound integration.

- Audio is central to the experience: a `SoundManager` handles background music and positional sound effects so the environment can feel alive and threatening. Using an audio library with 3D spatialization made it possible to place sounds in space (left/right/front/back) to increase tension.

- The narrative is implemented as discrete nodes with branching choices. We structured the story with at least two meaningful branches and multiple endings so player choices have weight and increase replayability. This keeps the code modular and easy to expand with new nodes or branches.

- We kept the user interface simple (terminal-based text I/O) to focus effort on audio design and narrative content instead of building a GUI. This decision made the project feasible within the time constraints while still delivering a compelling experience.

## Project structure (brief)

- `main.py` — program entry point; starts the game.
- `src/game.py` — game loop and player interaction logic.
- `src/Story.py` — story node definitions and branching logic.
- `src/sound.py` — `SoundManager` that plays background and positional sound effects (uses PyOpenAL).
- `sounds/` — audio assets used by the game.
- `Requirements.txt` — list of Python dependencies.

## How to run (recommended)

1. Create or activate a Python 3.10+ virtual environment (recommended).

2. Install dependencies:

    ```bash
    pip install -r Requirements.txt
    ```

3. Run the game from the project root:

    ```bash
    python main.py
    ```

On Windows, run the commands using Git Bash, WSL, or a compatible Bash shell if you prefer; `python` must point to your Python 3 interpreter.

## Troubleshooting

- If audio does not play, ensure your system audio devices are available and that `pyopenal` installed correctly. You may need to install system-level OpenAL drivers (e.g., `OpenAL Soft`).

- If you get module import errors, verify you run the command from the project root and that `src` is available as a package (the project uses relative imports from `src`).

## External assets (SharePoint)

We host large media files externally. Please download the background music file and the 1-minute gameplay clip from this SharePoint folder:

https://javerianacaliedu-my.sharepoint.com/:f:/g/personal/misancio_javerianacali_edu_co/Eg6jnJSyqUJPh1a8oZIdG-gBFsQkaL-USleuPHtkeSX8Cg?e=jdj0Zf

Recommended placement after downloading:

- Background music: place the audio file as `Background_Music.wav` in the project sound folder.
- Short gameplay video: place the video file as `Porject_2_SI_Gameplay.mp4`.

Notes:

- The background WAV may be large; GitHub rejects files larger than 100 MB. If the background audio exceeds that size and you want it in the repository, use Git LFS (recommended). Example commands to enable and track WAV files:

```bash
git lfs install
git lfs track "sounds/*.wav"
git add .gitattributes
git add sounds/Background_Music.wav
git commit -m "Add background music via Git LFS"
git push origin dev
```

- Alternatively, keep these large files out of Git and leave them on the SharePoint link; the game will still run if the files are placed locally at the paths above.

- If you place the gameplay video under `assets/`, it is only for demonstration and is not required for running the text-based game.

