# Manim sketches

Short math animations I write in Python while learning [Manim](https://www.manim.community/).

**Watch them here: https://slizora2005.github.io/manim-animations/**

| Animation | What it shows | Source |
|---|---|---|
| Area between a parabola and a semicircle | Riemann rectangles under f(x) = x² − 4 that morph onto f(x) = √(16 − x²) | [`scenes/parabola_area.py`](scenes/parabola_area.py) |
| A sphere and a cube in 3D | Translucent 3D shapes moving through axes with a tilted camera | [`scenes/shapes_3d.py`](scenes/shapes_3d.py) |
| A box that follows ln(2) | `always_redraw` updaters that track a moving expression | [`scenes/updaters.py`](scenes/updaters.py) |

## Render them yourself

Manim needs a few system tools (like LaTeX for the math labels), so follow the [installation guide](https://docs.manim.community/en/stable/installation.html) for your OS first. Then install the pinned version used here and render:

```bash
pip install -r requirements.txt
manim -pqh scenes/parabola_area.py Graphing
manim -pqh scenes/shapes_3d.py HelloWorld
manim -pqh scenes/updaters.py Updaters
```

`-p` opens the video when it's done and `-qh` renders at 1080p. Output goes to `media/`, which is ignored by git.

## Layout

```
scenes/    Python source for each animation
videos/    Rendered MP4s, optimized for web playback
posters/   Preview frames shown before a video plays
index.html The gallery page served by GitHub Pages
```

## License

The code is available under the [MIT License](LICENSE).
