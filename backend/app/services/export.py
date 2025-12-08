from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from io import BytesIO
from datetime import datetime


def generate_article_pdf(article, include_summary=False, summary_data=None):
    """Generate PDF for article"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor='#2E3B7D',
        spaceAfter=12,
        alignment=TA_CENTER
    )
    
    meta_style = ParagraphStyle(
        'MetaInfo',
        parent=styles['Normal'],
        fontSize=10,
        textColor='gray',
        spaceAfter=8
    )
    
    content_style = ParagraphStyle(
        'Content',
        parent=styles['BodyText'],
        fontSize=11,
        leading=14,
        alignment=TA_LEFT
    )
    
    # Add title
    title = Paragraph(article.title, title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Add metadata
    meta_text = f"""
    <b>Penulis:</b> {article.author_name}<br/>
    <b>Tanggal:</b> {article.published_date.strftime('%d %B %Y')}<br/>
    <b>Kategori:</b> {article.category.name}<br/>
    """
    if article.source_url:
        meta_text += f"<b>Sumber:</b> {article.source_url}<br/>"
    
    meta = Paragraph(meta_text, meta_style)
    elements.append(meta)
    elements.append(Spacer(1, 20))
    
    # Add content
    content_paragraphs = article.content.split('\n')
    for para in content_paragraphs:
        if para.strip():
            elements.append(Paragraph(para, content_style))
            elements.append(Spacer(1, 12))
    
    # Add summary if requested
    if include_summary and summary_data:
        elements.append(Spacer(1, 24))
        summary_title = Paragraph("<b>Ringkasan AI</b>", styles['Heading2'])
        elements.append(summary_title)
        elements.append(Spacer(1, 12))
        
        for key, value in summary_data.items():
            if value:
                label = key.upper()
                summary_para = Paragraph(f"<b>{label}:</b> {value}", content_style)
                elements.append(summary_para)
                elements.append(Spacer(1, 8))
    
    # Build PDF
    doc.build(elements)
    
    # Get the value of the BytesIO buffer
    pdf = buffer.getvalue()
    buffer.close()
    
    return pdf


def generate_article_txt(article, include_summary=False, summary_data=None):
    """Generate TXT for article"""
    content = f"""{article.title}
{'=' * len(article.title)}

Penulis: {article.author_name}
Tanggal: {article.published_date.strftime('%d %B %Y')}
Kategori: {article.category.name}
"""
    
    if article.source_url:
        content += f"Sumber: {article.source_url}\n"
    
    content += f"\n{'-' * 80}\n\n"
    content += article.content
    
    if include_summary and summary_data:
        content += f"\n\n{'-' * 80}\n"
        content += "RINGKASAN AI\n"
        content += f"{'-' * 80}\n\n"
        
        for key, value in summary_data.items():
            if value:
                content += f"{key.upper()}: {value}\n\n"
    
    return content.encode('utf-8')
