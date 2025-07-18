import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Step 1: Read Data
def read_data(filename):
    return pd.read_csv(filename)

# Step 2: Analyze Data
def analyze_data(df):
    summary = {
        "Total Students": len(df),
        "Average Score": round(df['Score'].mean(), 2),
        "Highest Score": df['Score'].max(),
        "Lowest Score": df['Score'].min()
    }
    return summary

# Step 3: Generate Chart
def generate_chart(df):
    plt.figure(figsize=(6, 4))
    plt.bar(df['Name'], df['Score'], color='skyblue')
    plt.title('Student Scores')
    plt.xlabel('Students')
    plt.ylabel('Scores')
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig('chart.png')
    plt.close()

# Step 4: Generate PDF Report
def generate_pdf_report(summary):
    doc = SimpleDocTemplate("sample_report.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    flowables = []

    flowables.append(Paragraph("Student Score Report", styles['Title']))
    flowables.append(Spacer(1, 20))

    for key, value in summary.items():
        flowables.append(Paragraph(f"<b>{key}:</b> {value}", styles['Normal']))
        flowables.append(Spacer(1, 10))

    flowables.append(Spacer(1, 20))
    flowables.append(Paragraph("Scores Chart:", styles['Heading2']))
    flowables.append(Image('chart.png', width=400, height=300))

    doc.build(flowables)
    print("PDF Report Generated: sample_report.pdf")

# Main Execution
if __name__ == "__main__":
    df = read_data('data.csv')
    summary = analyze_data(df)
    generate_chart(df)
    generate_pdf_report(summary)
