import re

def convert_latex_to_plain(text):
    replacements = [
        (r'\$\$\\int_([^\^]*?)\\infty\$\$', '∫[\\1 to ∞]'),
        (r'\$\$\\int_([^\^]*?)\^([^\$]*?)\$\$', '∫[\\1 to \\2]'),
        (r'\$\$\\frac{(.*?)}{(.*?)}\$\$', '(\\1)/(\\2)'),
        (r'\$\$\\ln\s*(.*?)\$\$', 'ln\\1'),
        (r'\$\$([^$]+?)\$\$', '\\1'),
        (r'\\left\[', '['),
        (r'\\right\]', ']'),
        (r'\\to', '→'),
        (r'\\infty', '∞'),
        (r'\\cdot', '*'),
        (r'\\ln', 'ln'),
        (r'\\frac{(.*?)}{(.*?)}', '(\\1)/(\\2)'),
    ]
    
    result = text
    for pattern, replacement in replacements:
        result = re.sub(pattern, replacement, result)
    
    result = re.sub(r'\\[a-zA-Z]+', '', result)
    result = re.sub(r'\s+', ' ', result)
    
    return result.strip()

def process_document(input_text):
    lines = input_text.split('\n')
    processed_lines = []
    
    for line in lines:
        if line.startswith('#') or line.startswith('*'):
            processed_line = convert_latex_to_plain(line)
        else:
            processed_line = convert_latex_to_plain(line)
        processed_lines.append(processed_line)
    
    return '\n'.join(processed_lines)

with open('pre.md', 'r', encoding='utf-8') as f:
    input_text = f.read()

output_text = process_document(input_text)

with open('post.md', 'w', encoding='utf-8') as f:
    f.write(output_text)