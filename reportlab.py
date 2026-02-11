from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def create_requirements_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Custom Style
    title_style = styles['Title']
    heading_style = styles['Heading2']
    normal_style = styles['BodyText']
    bullet_style = ParagraphStyle('Bullet', parent=styles['BodyText'], bulletIndent=10, leftIndent=20)

    # Title
    story.append(Paragraph("Amazon Data Analysis Project Requirements", title_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("This document outlines 21 distinct tasks to develop your skills in Pivot Tables, DAX, and Data Visualization using the Amazon dataset.", normal_style))
    story.append(Spacer(1, 24))

    # Section 1: Pivot Tables
    story.append(Paragraph("Part 1: Pivot Table Tasks", heading_style))
    tasks_pivot = [
        "<b>Data Cleaning & Setup:</b> Clean 'discounted_price' and 'actual_price' (remove symbols). Convert 'rating' and 'rating_count' to numeric. Parse 'category' to create a 'Main Category' column.",
        "<b>Category Summary:</b> Create a Pivot Table showing Rows: 'Main Category', Values: Count of 'product_id' and Average of 'rating'.",
        "<b>Pricing Deep Dive:</b> Create a Pivot Table showing Rows: 'Main Category', Values: Average 'actual_price' vs Average 'discounted_price'.",
        "<b>Rating Matrix:</b> Group 'rating' into bins (3.0-3.5, 3.5-4.0, etc.). Create a matrix with Rows: 'Main Category', Columns: Rating Bins, Values: Count of products.",
        "<b>Top Sellers:</b> Create a Pivot Table filtered to show the Top 10 products by 'rating_count'. Display product name, price, and rating.",
        "<b>Discount Buckets:</b> Group 'discount_percentage' into bins (0-10%, 10-20%...). Show product count and average rating per bin.",
        "<b>Hierarchy Analysis:</b> Create a hierarchy of Main Category > Sub Category. Show Total 'rating_count' to identify niche popular categories."
    ]
    for task in tasks_pivot:
        story.append(Paragraph(f"• {task}", bullet_style))
        story.append(Spacer(1, 6))
    story.append(Spacer(1, 12))

    # Section 2: DAX
    story.append(Paragraph("Part 2: DAX (Data Analysis Expressions) Tasks", heading_style))
    tasks_dax = [
        "<b>Basic Measures:</b> Create measures for 'Total Products' (COUNTROWS) and 'Avg Selling Price' (AVERAGE).",
        "<b>Revenue Proxy:</b> Estimate value: SUMX('Amazon', [discounted_price] * [rating_count]).",
        "<b>High Rated Count:</b> Measure: CALCULATE([Total Products], 'Amazon'[rating] >= 4.5).",
        "<b>Percent High Rated:</b> Measure: DIVIDE([High Rated Count], [Total Products], 0).",
        "<b>Review Tier Segment:</b> Calculated Column: IF([rating_count] > 10000, 'High', IF([rating_count] > 1000, 'Medium', 'Low')).",
        "<b>Price Rank:</b> Measure ranking products by price within their category: RANKX(ALLEXCEPT(...), [discounted_price]).",
        "<b>Discount Efficiency:</b> Measure: DIVIDE(SUM([actual_price] - [discounted_price]), SUM([actual_price])). Shows overall % saved."
    ]
    for task in tasks_dax:
        story.append(Paragraph(f"• {task}", bullet_style))
        story.append(Spacer(1, 6))
    story.append(Spacer(1, 12))

    # Section 3: Visuals
    story.append(Paragraph("Part 3: Visualization & Dashboard Tasks", heading_style))
    tasks_visuals = [
        "<b>KPI Header:</b> Create Cards for 'Total Products', 'Avg Rating', 'Avg Discount %', and 'Revenue Proxy'.",
        "<b>Category Volume:</b> Bar Chart showing 'Main Category' vs 'Total Products'. Sort descending.",
        "<b>Price vs. Rating:</b> Scatter Plot. X-axis='discounted_price', Y-axis='rating'. Legend='Main Category'.",
        "<b>Discount Heatmap:</b> Treemap. Group='Main Category', Size='Revenue Proxy', Color='Avg Discount %'.",
        "<b>Top Products List:</b> Multi-row Card or Table showing Top 5 products by 'rating_count' with their prices.",
        "<b>Rating Distribution:</b> Histogram or Column Chart showing distribution of Ratings (rounded bins).",
        "<b>Interactivity:</b> Add Slicers for 'Main Category' and 'Review Tier' to filter the entire dashboard."
    ]
    for task in tasks_visuals:
        story.append(Paragraph(f"• {task}", bullet_style))
        story.append(Spacer(1, 6))

    doc.build(story)

create_requirements_pdf('Amazon_Project_Requirements.pdf')