import tkinter as tk
from tkinter import ttk, messagebox

class GPA_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("SGPA & CGPA Calculator - Official College Grading")
        self.root.geometry("1250x820")
        
        self.current_subjects = []   # Current semester subjects
        self.all_semesters = []      # For CGPA calculation

        # Title
        tk.Label(root, text="SGPA & CGPA Calculator (Official Grading System)", 
                 font=("Arial", 18, "bold")).pack(pady=12)

        # Load Sample Button
        tk.Button(root, text="Load Melam Akash Sample (Numbered Subjects)", 
                  command=self.load_sample_data, bg="#FF5722", fg="white", 
                  font=("Arial", 11, "bold")).pack(pady=8)

        # Input Frame
        input_frame = tk.LabelFrame(root, text="Add Subject (IM + EM Marks)", padx=15, pady=15)
        input_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(input_frame, text="Subject Name:").grid(row=0, column=0, sticky="w", pady=6)
        self.name_entry = tk.Entry(input_frame, width=45)
        self.name_entry.grid(row=0, column=1, columnspan=3, pady=6, padx=8)

        tk.Label(input_frame, text="Internal Marks (IM):").grid(row=1, column=0, sticky="w", pady=6)
        self.im_entry = tk.Entry(input_frame, width=12)
        self.im_entry.grid(row=1, column=1, pady=6, padx=8)

        tk.Label(input_frame, text="External Marks (EM):").grid(row=1, column=2, sticky="w", pady=6)
        self.em_entry = tk.Entry(input_frame, width=12)
        self.em_entry.grid(row=1, column=3, pady=6, padx=8)

        tk.Label(input_frame, text="Credits:").grid(row=1, column=4, sticky="w", pady=6)
        self.credits_entry = tk.Entry(input_frame, width=12)
        self.credits_entry.grid(row=1, column=5, pady=6, padx=8)

        tk.Button(input_frame, text="Add Subject", command=self.add_subject, 
                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).grid(row=2, column=0, columnspan=6, pady=12)

        # Table
        self.tree = ttk.Treeview(root, columns=("No", "Subject", "IM", "EM", "Total", "Grade", "GP", "Credits", "Points"), 
                                 show="headings", height=11)
        self.tree.heading("No", text="No.")
        self.tree.heading("Subject", text="Subject Name")
        self.tree.heading("IM", text="IM")
        self.tree.heading("EM", text="EM")
        self.tree.heading("Total", text="Total Marks")
        self.tree.heading("Grade", text="Letter Grade")
        self.tree.heading("GP", text="Grade Point")
        self.tree.heading("Credits", text="Credits")
        self.tree.heading("Points", text="C × GP")

        self.tree.column("No", width=50, anchor="center")
        self.tree.column("Subject", width=320)
        for col in ["IM", "EM", "Total", "Grade", "GP", "Credits", "Points"]:
            self.tree.column(col, width=85, anchor="center")

        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=12)
        tk.Button(btn_frame, text="Calculate SGPA", command=self.calculate_sgpa, 
                  bg="#2196F3", fg="white", width=18).pack(side="left", padx=12)
        tk.Button(btn_frame, text="Add Semester to CGPA", command=self.add_to_cgpa, 
                  bg="#FF9800", fg="white", width=20).pack(side="left", padx=12)
        tk.Button(btn_frame, text="Clear Current Semester", command=self.clear_current, 
                  bg="#f44336", fg="white").pack(side="left", padx=12)

        self.sgpa_label = tk.Label(root, text="Current SGPA : --", font=("Arial", 13, "bold"), fg="blue")
        self.sgpa_label.pack(pady=8)

        # CGPA Section
        tk.Label(root, text="Added Semesters for CGPA Calculation", font=("Arial", 12, "bold")).pack(pady=(20,5))
        self.sem_tree = ttk.Treeview(root, columns=("Sem", "Credits", "SGPA"), show="headings", height=6)
        self.sem_tree.heading("Sem", text="Semester")
        self.sem_tree.heading("Credits", text="Total Credits")
        self.sem_tree.heading("SGPA", text="SGPA")
        self.sem_tree.column("Sem", width=100, anchor="center")
        self.sem_tree.column("Credits", width=150, anchor="center")
        self.sem_tree.column("SGPA", width=150, anchor="center")
        self.sem_tree.pack(pady=8, padx=20, fill="x")

        tk.Button(root, text="Calculate Final CGPA", command=self.calculate_final_cgpa, 
                  bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=15)

        self.final_label = tk.Label(root, text="CGPA : --   |   Class : --   |   Equivalent Percentage : --", 
                                    font=("Arial", 13, "bold"), fg="green", wraplength=900)
        self.final_label.pack(pady=10)

    # ====================== Official Grade Point System ======================
    def get_grade_point(self, total_marks):
        if total_marks >= 91: 
            return 10.0, "O"
        elif total_marks >= 81: 
            return 9.0, "A+"
        elif total_marks >= 71: 
            return 8.0, "A"
        elif total_marks >= 61: 
            return 7.0, "B+"
        elif total_marks >= 51: 
            return 6.0, "B"
        elif total_marks >= 41: 
            return 5.0, "C"
        elif total_marks >= 40: 
            return 4.0, "P"
        else: 
            return 0.0, "F"

    def load_sample_data(self):
        self.clear_current()
        
        sample = [
            ("DATA SCIENCE", 36, 27, 3.0),
            ("WEB TECHNOLOGY", 32, 33, 3.0),
            ("CRYPTOGRAPHY AND NETWORK SECURITY", 21, 31, 3.0),
            ("MACHINE LEARNING", 29, 27, 3.0),
            ("SOFTWARE ENGINEERING", 32, 27, 3.0),
            ("CRYPTOGRAPHY AND NETWORK SECURITY LABORATORY", 30, 49, 1.5),
            ("DATA SCIENCE LABORATORY", 30, 49, 1.5),
            ("ADVANCED PYTHON PROGRAMMING", 31, 53, 3.0),
            ("PROFESSIONAL ETHICS", 76, 0, 0.0),
            ("INTRODUCTION TO INTERNET OF THINGS", 0, 60, 3.0),
        ]

        for i, (name, im, em, credits) in enumerate(sample, 1):
            total = im + em
            gp, letter = self.get_grade_point(total)
            points = round(credits * gp, 3)

            self.current_subjects.append({
                "name": name, "im": im, "em": em, "total": total,
                "gp": gp, "letter": letter, "credits": credits, "points": points
            })

            display_credits = "0" if credits == 0 else f"{credits:.1f}"
            self.tree.insert("", "end", values=(
                i, name[:40], im, em, total, letter, f"{gp:.1f}", 
                display_credits, f"{points:.2f}"
            ))

        messagebox.showinfo("Sample Loaded", "Melam Akash sample loaded with official grading system.\nReady to calculate SGPA.")

    def add_subject(self):
        try:
            name = self.name_entry.get().strip()
            im = int(self.im_entry.get().strip() or 0)
            em = int(self.em_entry.get().strip() or 0)
            credits = float(self.credits_entry.get().strip() or 0)

            if not name:
                raise ValueError("Subject name is required")

            total = im + em
            gp, letter = self.get_grade_point(total)
            points = round(credits * gp, 3)

            self.current_subjects.append({
                "name": name, "im": im, "em": em, "total": total,
                "gp": gp, "letter": letter, "credits": credits, "points": points
            })

            no = len(self.current_subjects)
            display_credits = "0" if credits == 0 else f"{credits:.1f}"

            self.tree.insert("", "end", values=(
                no, name[:40], im, em, total, letter, f"{gp:.1f}", 
                display_credits, f"{points:.2f}"
            ))

            # Clear fields
            self.name_entry.delete(0, tk.END)
            self.im_entry.delete(0, tk.END)
            self.em_entry.delete(0, tk.END)
            self.credits_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Input Error", "Please check your inputs.\nCredits can be decimal (e.g. 1.5)")

    def calculate_sgpa(self):
        if not self.current_subjects:
            messagebox.showwarning("No Subjects", "Please add subjects first.")
            return

        total_credits = sum(sub["credits"] for sub in self.current_subjects if sub["credits"] > 0)
        total_points = sum(sub["points"] for sub in self.current_subjects if sub["credits"] > 0)

        if total_credits == 0:
            self.sgpa_label.config(text="Current SGPA : 0.00", fg="red")
            return

        sgpa = total_points / total_credits
        sgpa_rounded = round(sgpa, 2)

        self.sgpa_label.config(text=f"Current SGPA : {sgpa_rounded:.2f}", fg="green")

    def add_to_cgpa(self):
        if not self.current_subjects:
            messagebox.showwarning("Empty Semester", "Add subjects first.")
            return

        total_credits = sum(sub["credits"] for sub in self.current_subjects if sub["credits"] > 0)
        total_points = sum(sub["points"] for sub in self.current_subjects if sub["credits"] > 0)

        if total_credits == 0:
            messagebox.showwarning("No Credits", "No subjects with positive credits.")
            return

        sgpa = round(total_points / total_credits, 2)
        sem_no = len(self.all_semesters) + 1

        self.all_semesters.append((sem_no, total_credits, sgpa))
        self.sem_tree.insert("", "end", values=(f"Semester {sem_no}", f"{total_credits:.1f}", f"{sgpa:.2f}"))

        messagebox.showinfo("Success", f"Semester {sem_no} added successfully!\nSGPA = {sgpa:.2f}")
        self.clear_current()

    def calculate_final_cgpa(self):
        if not self.all_semesters:
            messagebox.showwarning("No Semesters", "Please add at least one semester.")
            return

        total_credits_all = sum(credits for _, credits, _ in self.all_semesters)
        total_weighted = sum(credits * sgpa for _, credits, sgpa in self.all_semesters)

        cgpa = total_weighted / total_credits_all
        cgpa_rounded = round(cgpa, 2)

        if cgpa_rounded >= 7.5:
            cls = "First Class with Distinction"
        elif cgpa_rounded >= 6.5:
            cls = "First Class"
        elif cgpa_rounded >= 5.5:
            cls = "Second Class"
        elif cgpa_rounded >= 4.0:
            cls = "Pass Class"
        else:
            cls = "Fail"

        percentage = round((cgpa_rounded - 0.5) * 10, 2)

        result_text = f"CGPA : {cgpa_rounded:.2f}   |   Class : {cls}   |   Equivalent % : {percentage}%"
        self.final_label.config(text=result_text)

    def clear_current(self):
        self.current_subjects.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.sgpa_label.config(text="Current SGPA : --", fg="blue")

# ====================== RUN THE APPLICATION ======================
if __name__ == "__main__":
    root = tk.Tk()
    app = GPA_Calculator(root)
    root.mainloop()