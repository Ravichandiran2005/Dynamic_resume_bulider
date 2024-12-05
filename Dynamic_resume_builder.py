from fpdf import FPDF
class ResumeBuilder:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
    
    def add_title(self, name, role):
        self.pdf.set_font("Arial", size=16, style='B')
        self.pdf.cell(0, 10, f"{name}", ln=True, align="C")
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(0, 10, f"{role}", ln=True, align="C")
        self.pdf.ln(10)
    
    def add_section(self, title):
        self.pdf.set_font("Arial", size=14, style='B')
        self.pdf.cell(0, 10, title, ln=True)
        self.pdf.ln(5)
    
    def add_text(self, text):
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, text)
        self.pdf.ln(5)

    def save_pdf(self, filename):
        self.pdf.output(filename)

def main():
    print("Welcome to the Dynamic Resume Builder!")
    name = input("Enter your full name: ")
    role = input("Enter your desired role (e.g., Software Engineer): ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    summary = input("Write a brief professional summary: ")
    
    # Skills Section
    print("\nEnter your skills (type 'done' when finished):")
    skills = []
    while True:
        skill = input("Skill: ")
        if skill.lower() == 'done':
            break
        skills.append(skill)
    
    # Experience Section
    print("\nEnter your work experience (type 'done' when finished):")
    experience = []
    while True:
        job = input("Job Title and Company (e.g., Software Engineer at ABC Corp): ")
        if job.lower() == 'done':
            break
        duration = input("Duration (e.g., Jan 2020 - Dec 2023): ")
        details = input("Job Description: ")
        experience.append(f"{job} ({duration})\n{details}")
    
    # Education Section
    print("\nEnter your education details (type 'done' when finished):")
    education = []
    while True:
        degree = input("Degree and Institution (e.g., B.Sc. in Computer Science, XYZ University): ")
        if degree.lower() == 'done':
            break
        duration = input("Duration (e.g., 2016 - 2020): ")
        education.append(f"{degree} ({duration})")
    
    # Build the Resume PDF
    resume = ResumeBuilder()
    resume.add_title(name, role)
    resume.add_section("Contact Information")
    resume.add_text(f"Email: {email}\nPhone: {phone}")
    
    resume.add_section("Professional Summary")
    resume.add_text(summary)
    
    resume.add_section("Skills")
    resume.add_text("\n".join(skills))
    
    resume.add_section("Work Experience")
    resume.add_text("\n\n".join(experience))
    
    resume.add_section("Education")
    resume.add_text("\n".join(education))
    
    # Save PDF
    filename = f"{name.replace(' ', '_')}_Resume.pdf"
    resume.save_pdf(filename)
    print(f"Resume saved as {filename}")

if __name__ == "__main__":
    main()