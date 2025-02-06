# World Bounds Editor 🗺️

A simple GUI-based tool for modifying `GenericWorldEntity` world bounds in game files for ARMA Reforger world editor projects.  
Supports automatic conversion from km to meters and ensures existing data integrity.

## Features 🚀
✅ Updates `boundMins` and `boundMaxs` inside the `GenericWorldEntity world {` block  
✅ Removes old/default values while retaining existing layer data. 
✅ Converts `km` to meters automatically  
✅ Provides a user-friendly **Tkinter GUI**  
✅ Open-source under **MIT License**  

## Installation & Usage 🛠️

1. **Clone the repository:**

git clone https://github.com/wwarma2/ReforgerBoundsPatcher.git

2. **Install required dependencies** (Python 3 required):

pip install tkinter

3. **Run the script**:

python fixWorldBounds.py

4. **Select the layer file**, enter world size, Y min/max values, and click **Save**!

## License 📜
This project is licensed under the **MIT License** – free to use and modify.

## Contributing 🤝
Feel free to fork this repository and submit **pull requests**! Any improvements are welcome.

## Author 💡
Created by **Rev** (armaconflict.com)
