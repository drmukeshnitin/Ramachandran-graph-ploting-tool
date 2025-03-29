import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from Bio import PDB
from tkinter import ttk

def extract_phi_psi_angles(pdb_file):
    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure("protein", pdb_file)
    model = structure[0]
    phi_psi_angles = []
    
    for chain in model:
        polypeptides = PDB.PPBuilder().build_peptides(chain)
        for poly in polypeptides:
            phi_psi = poly.get_phi_psi_list()
            for angles in phi_psi:
                if None not in angles:
                    phi = angles[0] * 180.0 / np.pi
                    psi = angles[1] * 180.0 / np.pi
                    phi_psi_angles.append((phi, psi))
    
    return np.array(phi_psi_angles)

def classify_regions(phi, psi):
    if (-140 <= phi <= -40 and 50 <= psi <= 180) or (-180 <= phi <= -140 and -180 <= psi <= 0):
        return "Most Favorable"
    elif (-140 <= phi <= 40 and -100 <= psi <= 100):
        return "Favorable"
    elif (-180 <= phi <= 180 and -180 <= psi <= 180):
        return "Allowed"
    else:
        return "Disallowed"

def generate_ramachandran_report(phi_psi_angles, output_file):
    classifications = [classify_regions(phi, psi) for phi, psi in phi_psi_angles]
    df = pd.DataFrame(phi_psi_angles, columns=["Phi", "Psi"])
    df["Region"] = classifications
    
    total = len(df)
    percentages = df["Region"].value_counts(normalize=True) * 100
    summary = pd.DataFrame(percentages).reset_index()
    summary.columns = ["Region", "Percentage"]
    summary["Percentage"] = summary["Percentage"].apply(lambda x: f"{x:.2f}%")
    
    df.to_csv(output_file, index=False)
    summary.to_csv("ramachandran_summary.csv", index=False)
    messagebox.showinfo("Success", "Ramachandran report and summary saved successfully!")

def plot_ramachandran(phi_psi_angles):
    plt.figure(figsize=(10, 8), dpi=300)
    
    sns.kdeplot(x=phi_psi_angles[:, 0], y=phi_psi_angles[:, 1], cmap="coolwarm", fill=True, alpha=0.6)
    
    colors = {"Most Favorable": "lime", "Favorable": "gold", "Allowed": "dodgerblue", "Disallowed": "red"}
    region_data = {region: [] for region in colors.keys()}
    
    for phi, psi in phi_psi_angles:
        region = classify_regions(phi, psi)
        region_data[region].append((phi, psi))
    
    for region, color in colors.items():
        data = np.array(region_data[region])
        if len(data) > 0:
            plt.scatter(data[:, 0], data[:, 1], s=20, color=color, label=region, alpha=0.9, edgecolors='black')
    
    total = sum(len(v) for v in region_data.values())
    percentages = {region: (len(v) / total) * 100 for region, v in region_data.items() if len(v) > 0}
    
    plt.subplots_adjust(right=0.75)
    for index, (region, color) in enumerate(percentages.items()):
        plt.text(190, 140 - (index * 30),
                 f"{region}: {percentages[region]:.2f}%", 
                 fontsize=5, color=colors[region], fontweight='bold',
                 bbox=dict(facecolor='white', edgecolor=colors[region], boxstyle='round,pad=0.5'))
    
    plt.xlim(-180, 180)
    plt.ylim(-180, 180)
    plt.xlabel("Φ (phi) Angles", fontsize=5, fontweight='bold', color='black')
    plt.ylabel("Ψ (psi) Angles", fontsize=5, fontweight='bold', color='black')
    plt.title("Ramachandran Plot", fontsize=14, fontweight='bold', color='darkblue')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    plt.savefig("ramachandran_plot.png", dpi=300, bbox_inches='tight')
    plt.show()

def upload_pdb():
    file_path = filedialog.askopenfilename(filetypes=[("PDB files", "*.pdb")])
    if file_path:
        angles = extract_phi_psi_angles(file_path)
        generate_ramachandran_report(angles, "ramachandran_report.csv")
        plot_ramachandran(angles)
        messagebox.showinfo("Success", "Ramachandran plot saved as ramachandran_plot.png")

# GUI Setup
root = tk.Tk()
root.title("Ramachandran Plot Generator")
root.geometry("500x350")
root.configure(bg='#1e1e1e')

frame = tk.Frame(root, bg='#2b2b2b', padx=20, pady=20)
frame.pack(pady=20)

title_label = tk.Label(frame, text="Ramachandran Plot Generator", font=("Arial", 18, "bold"), fg='cyan', bg='#2b2b2b')
title_label.pack()

description_label = tk.Label(frame, text="Upload a PDB file to generate a Ramachandran Plot", font=("Arial", 12), fg='white', bg='#2b2b2b')
description_label.pack(pady=10)

upload_button = tk.Button(frame, text="Upload PDB File", command=upload_pdb, font=("Arial", 12, "bold"), fg='white', bg='#007acc', relief='raised', padx=10, pady=5)
upload_button.pack(pady=10)

exit_button = tk.Button(frame, text="Exit", command=root.quit, font=("Arial", 12, "bold"), fg='white', bg='#ff3333', relief='raised', padx=10, pady=5)
exit_button.pack(pady=5)

root.mainloop()
