Ramachandran graph ploting tool-
 Ramachandran Plot Generator

 Overview
The Ramachandran Plot Generator is a graphical tool for analyzing the backbone dihedral angles (Φ, Ψ) of a protein structure from a PDB file. It generates a high-resolution Ramachandran plot with a density heatmap and scatter points, visually distinguishing most favorable, favorable, allowed, and disallowed regions with percentage calculations.

The tool features a colorful GUI for ease of use and produces a comprehensive report file detailing the classifications of dihedral angles.


![Screenshot from 2025-03-30 03-19-33](https://github.com/user-attachments/assets/9b328187-0041-4fa2-b438-420c4f026c8c)

![Figure_1](https://github.com/user-attachments/assets/7bc6557a-6d04-4c12-a7c4-78f6c23e19a1)



---

 Features
- Upload PDB Files: Easily select and analyze protein structure files.
- Ramachandran Plot Visualization:
  - Uses Seaborn to generate a cool-warm gradient heatmap.
  - Scatter points for individual residues.
  - Displays percentages for each region (Most Favorable, Favorable, Allowed, Disallowed).
  - Phi (Φ) and Psi (Ψ) labels are clearly represented.
- Report Generation:
  - Saves a CSV file listing each residue's dihedral angles and classification.
  - Summary file with region percentages.
- Professional GUI:
  - Colorful fonts and stylish buttons.
  - Easy-to-use interface with PDB file upload functionality.

---

 Installation
 Prerequisites
Ensure you have Python 3.x installed along with the following dependencies:
```sh
pip install numpy matplotlib seaborn pandas biopython tkinter
```

---

 Usage
 Running the Tool
To launch the graphical interface, execute the script:
```sh
python ramachandran_plot.py
```
 Steps to Use:
1. Click "Upload PDB File".
2. Select a .pdb file from your computer.
3. The tool processes the file and generates:
   - A Ramachandran plot (saved as `ramachandran_plot.png`).
   - A detailed CSV report (`ramachandran_report.csv`).
   - A summary CSV file (`ramachandran_summary.csv`) with region percentages.
4. The visual representation of the plot is displayed with distinct colors for each region.

---

 Output Files
1. ramachandran_plot.png – The high-resolution Ramachandran plot.
2. ramachandran_report.csv – Detailed report of dihedral angles and classifications.
3. ramachandran_summary.csv – Summary with region percentages.

---

 Example Output
 Ramachandran Plot
The generated Ramachandran plot will include:
- Heatmap background (cool-warm gradient).
- Scatter points categorized into:
  - Most Favorable (Lime)
  - Favorable (Gold)
  - Allowed (Dodgerblue)
  - Disallowed (Red)
- Region percentages displayed outside the plot area.

---

 License
This project is open-source and available under the MIT License.

---
For suggestions or bug reports, feel free to open an issue on GitHub!

---

 Contact
For any queries, contact Mukesh Nitin at drmukeshnitin@gmail.com or raise an issue on GitHub.

---

