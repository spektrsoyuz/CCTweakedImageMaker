# Introduction
This program allows you to take any image and create the code needed to display it on the [CC: Tweaked](https://www.curseforge.com/minecraft/mc-mods/cc-tweaked) monitors. The program will copy it to your clipboard, as well as save it to a file. Then you can put the code into [pastebin](https://pastebin.com/) and get it in-game with the `pastebin get` command.

## Installation
1. Clone the repository on your actual computer
```bash
git clone https://github.com/spektrsoyuz/CCTweakedImageMaker.git
```
2. Install the required packages
```bash
pip install -r requirements.txt
```

## Usage
1. Run the program on your real computer
```bash
python main.py <image_path> <num_monitors_wide> <num_monitors_tall>
```
2. Paste the code into [pastebin](https://pastebin.com/)
3. Run the command `pastebin get <code> <filename>` in your Minecraft computer. For example:
```bash
pastebin get 123456789 my_cute_cat
```
4. Run the program/image on the computer. For example:
```bash
my_cute_cat
```