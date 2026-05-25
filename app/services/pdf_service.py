from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(question, answer):

    print("Generating PDF...")

    # Create reports folder if not exists
    os.makedirs("reports", exist_ok=True)

    file_path = "reports/chat_report.pdf"

    # Create PDF document
    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()
    elements = []

    # Title
    title = Paragraph("<b>GenAI RAG Assistant Report</b>", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 20))

    # Question
    q = Paragraph(f"<b>Question:</b> {question}", styles['BodyText'])
    elements.append(q)
    elements.append(Spacer(1, 12))

    # Answer
    a = Paragraph(f"<b>Answer:</b> {answer}", styles['BodyText'])
    elements.append(a)

    # Build PDF
    doc.build(elements)

    return file_path