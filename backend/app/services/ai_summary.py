"""Mock AI Summary Service"""


def generate_summary(content, filters, length='medium'):
    """
    Generate AI summary based on content and filters.
    This is a mock implementation - replace with real LLM API integration.
    """
    
    # Mock summary responses in Indonesian
    summary = {}
    
    if 'who' in filters:
        summary['who'] = extract_who(content, length)
    
    if 'when' in filters:
        summary['when'] = extract_when(content, length)
    
    if 'where' in filters:
        summary['where'] = extract_where(content, length)
    
    if 'what' in filters:
        summary['what'] = extract_what(content, length)
    
    if 'why' in filters:
        summary['why'] = extract_why(content, length)
    
    if 'how' in filters:
        summary['how'] = extract_how(content, length)
    
    return summary


def extract_who(content, length):
    """Extract WHO information (mock)"""
    if length == 'short':
        return "Pelaku utama yang terlibat dalam peristiwa ini."
    elif length == 'long':
        return "Para pelaku utama yang terlibat dalam peristiwa ini meliputi pejabat pemerintah, tokoh masyarakat, dan pihak-pihak terkait lainnya yang memainkan peran penting dalam kejadian tersebut."
    return "Pelaku utama yang terlibat dalam peristiwa ini meliputi pejabat dan pihak-pihak terkait."


def extract_when(content, length):
    """Extract WHEN information (mock)"""
    if length == 'short':
        return "Peristiwa terjadi baru-baru ini."
    elif length == 'long':
        return "Peristiwa ini terjadi pada waktu yang telah ditentukan sebelumnya, dengan rangkaian kejadian yang berlangsung dalam periode tertentu dan melibatkan berbagai tahapan penting."
    return "Peristiwa ini terjadi dalam periode waktu tertentu dengan tahapan-tahapan penting."


def extract_where(content, length):
    """Extract WHERE information (mock)"""
    if length == 'short':
        return "Lokasi kejadian di wilayah yang ditentukan."
    elif length == 'long':
        return "Lokasi kejadian berada di wilayah strategis yang memiliki signifikansi khusus, melibatkan beberapa tempat penting dan area yang menjadi pusat perhatian dalam peristiwa tersebut."
    return "Lokasi kejadian berada di wilayah strategis yang ditentukan."


def extract_what(content, length):
    """Extract WHAT information (mock)"""
    if length == 'short':
        return "Kejadian utama yang terjadi."
    elif length == 'long':
        return "Kejadian utama yang terjadi meliputi serangkaian peristiwa penting yang memiliki dampak signifikan, dengan berbagai aspek yang perlu diperhatikan dan konsekuensi yang luas terhadap situasi terkini."
    return "Kejadian utama meliputi serangkaian peristiwa penting dengan dampak signifikan."


def extract_why(content, length):
    """Extract WHY information (mock)"""
    if length == 'short':
        return "Alasan utama di balik peristiwa ini."
    elif length == 'long':
        return "Alasan dan latar belakang di balik peristiwa ini mencakup berbagai faktor kompleks, termasuk kondisi sosial, ekonomi, dan politik yang saling berkaitan, serta motivasi berbagai pihak yang terlibat."
    return "Alasan di balik peristiwa ini mencakup berbagai faktor sosial, ekonomi, dan politik."


def extract_how(content, length):
    """Extract HOW information (mock)"""
    if length == 'short':
        return "Cara kejadian berlangsung."
    elif length == 'long':
        return "Kronologi dan cara kejadian berlangsung dimulai dari tahap awal, berkembang melalui berbagai fase, dan mencapai klimaks dengan serangkaian tindakan dan reaksi dari berbagai pihak yang terlibat dalam situasi tersebut."
    return "Kronologi kejadian berlangsung melalui berbagai fase dengan tindakan dari pihak terlibat."
