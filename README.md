# Automated-report-generation-

COMPANY : CODTECH IT SOLUTIONS

NAME : Nihar Patel

INTERN ID : CT06DF925

DOMAIN : PYTHON PROGRAMMING

DURATION : 6 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

Task Name: Automated Report Generator The Automated Report Generator is a Python-based data analysis and reporting tool that converts raw mobile phone sales data into a structured and visual PDF report. It performs automated data cleaning, generates insightful charts, and compiles everything into a multi-page document using libraries like Pandas, Matplotlib, Seaborn, and ReportLab.

Technologies Used Python – Main programming language.

Pandas – For loading and analyzing CSV data.

Matplotlib & Seaborn – For creating visual charts and heatmaps.

ReportLab – For generating a PDF report with text, images, and tables.

CSV File – Contains mobile sales data like brand, variant, RAM, storage, price, color, year, and location.

How It Works

Data Loading The dataset (mobile_phone_sales_data.csv) is loaded using Pandas. It contains columns like Year, Color, Variant, RAM, Storage, Price, and Location.

Preprocessing If the Brand column is missing, it is extracted from the first word of the Variant field. The script ensures data consistency and drops null values where needed.

Insight Generation Using basic statistical methods, the script calculates:

Total phones sold

Average price

Most common mobile brand

Most popular color

Chart Creation The following visuals are generated and saved as PNG files:
Top 10 Brands Sold – Bar chart

Average Price by Brand – Bar chart

RAM vs Storage – Heatmap

Price Distribution – Histogram

Phones by Year – Bar chart

These visualizations help in understanding sales trends and user preferences.

PDF Report Creation The ReportLab library is used to build a detailed PDF:
A cover page with a title, logo, and brief description.

A summary page with extracted insights.

Visual charts added one by one across multiple pages.

A tabular section showing the full dataset, split into pages with 40 records per page.

Page numbers are added automatically.

Applications Retail & E-commerce: To track sales trends and top-selling products.

Business Intelligence: For generating quick, visual reports from large datasets.

Academic Projects: Ideal for students showcasing real-world data processing.

Sales & Marketing: To identify high-performing products, brands, and pricing strategies.

Automation: Saves time by eliminating manual report creation.

Platform & Tools Platform: Desktop (Windows)

IDE: VS Code

Output: PDF report containing insights, visuals, and tabular data

Highlights Fully automated reporting pipeline

Uses real data for analysis and insights

Clean, readable charts and tables

Professionally formatted multi-page PDF

Easily customizable for other domains

This project effectively demonstrates practical use of Python in data analytics and automation, making it highly relevant for internships, business reporting, or academic evaluation.

Output : 

<img width="1869" height="805" alt="Image" src="https://github.com/user-attachments/assets/72e25aa7-9e1c-4d6a-a036-dd08962cd9f3" />
<img width="1690" height="742" alt="Image" src="https://github.com/user-attachments/assets/8337c091-ebc3-4ef5-b6c5-74a9c5f99db1" />
