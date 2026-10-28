# 🎆 Discord Remote Access TROJAN
**DISCORD RAT REMOVAL** is a simple removal for the rat i created

Please note that this is **NOT** an "HACKING TOOL", but just an tool for being educated about shell commands

**If you're going to fork this repository, star it too while you're at it!**

---

# ⚒️ Setup

Packaging main.py into an .exe with PyInstaller

Install Python dependencies
Download  `requirements.txt ` and `rat-removal.py` and.:
Then install everything:
`pip install -r requirements.txt`

Install PyInstaller
`pip install pyinstaller`

Build the executable
From the folder containing main.py:

`pyinstaller --onefile main.py`

- `--onefile` bundles everything into a single .exe
- Omit it if you want a folder with the .exe plus its dependencies instead (faster startup, easier to inspect)

Useful optional flags:
- `--icon=youricon.ico` — custom icon
- `--noconsole` — hide the console window (GUI apps only — don't use this if your script prints output the user needs to see)
- `--name=YourAppName` — set the output filename
- `--add-data "source;dest"` — bundle extra files (configs, assets)

Find your .exe
After building, it'll be in:

`dist/main.exe`

The `build/` folder and `.spec` file are just intermediate build artifacts and can be deleted.


Run `dist/main.exe` on a clean machine (or VM) without Python installed, to confirm all dependencies were bundled correctly.

---

# 🐛 Bug Reports & Suggestions

**Found a bug? Have an idea?** Let me know [here!](../../issues) Please provide a detailed explanation of the expected behavior, actual behavior, and steps to reproduce, or what you want to see and how it could be done. You can be a small part of this project!
**Active/known bugs:**.
None at the moment!
---

# 📜 Closing Statements

Liked the project? I know you did! Support me, **drop a star!** <br>
here my [Ko-fi link](https://ko-fi.com/rjewi) 
Thank you for choosing my tools! 🙏
