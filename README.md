# Khazad (Very early in development, does not work currently)
A terminal-based roguelike that I am currently developing

## Overview

**Khazad** is a procedural dungeon generation project inspired by classic roguelikes like *Angband* and *Rogue*, and themed around the ancient halls of J.R.R. Tolkien’s dwarves. This version focuses on building a scalable, extensible BSP-based dungeon generation system in Python.

Though early in development, the foundation prioritizes clean geometry, testability, and extensibility.

## Features

- 🧱 **Binary Space Partitioning (BSP)** to split the map into dynamic, rectangular regions
- 🧭 Cleanly designed `Rect`, `Point`, and `Node` classes with clear responsibilities
- 💡 Emphasis on readability and modularity — minimal magic, maximum clarity

## File Structure

khazad/
|-- dungeon_generator.py (Core BSP logic, currently in progress)
|-- renderer.py (throw NotImplementedException)
|-- utils/
| |-- types.py (Holds reusable dataclasses such as `Point`)
|-- main.py (throw NotImplementedException, core game loop and entry point for the program)

## Next Steps
- Complete BSP algorithm

## Acknowledgments

Inspired by:
- *Angband*, *Rogue*, *Dungeon Crawl Stone Soup*
- Tolkien's Mines of Moria and the narrative depth of Middle-earth
- Procedural generation techniques documented by the roguelike development community

---

## License

This project is for educational and personal development purposes. MIT License to come later once project structure is stabilized.