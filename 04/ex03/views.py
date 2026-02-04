from django.shortcuts import render


def generate_shades(color_name, start_value, end_value, steps=50):
    """Generate color shades for a given color"""
    shades = []
    step_size = (end_value - start_value) / (steps - 1)
    
    for i in range(steps):
        if color_name == 'noir':  # Black shades
            value = int(start_value + (i * step_size))
            hex_color = f'#{value:02x}{value:02x}{value:02x}'
        elif color_name == 'rouge':  # Red shades
            value = int(start_value + (i * step_size))
            hex_color = f'#{value:02x}0000'
        elif color_name == 'bleu':  # Blue shades
            value = int(start_value + (i * step_size))
            hex_color = f'#0000{value:02x}'
        elif color_name == 'vert':  # Green shades
            value = int(start_value + (i * step_size))
            hex_color = f'#00{value:02x}00'
        
        shades.append(hex_color)
    
    return shades


def index(request):
    """Display color shades table"""
    # Generate 50 shades for each color
    colors = {
        'noir': generate_shades('noir', 0, 255, 50),
        'rouge': generate_shades('rouge', 0, 255, 50),
        'bleu': generate_shades('bleu', 0, 255, 50),
        'vert': generate_shades('vert', 0, 255, 50)
    }
    
    # Transpose the colors dict to create rows
    # Each row will have one shade from each color
    rows = []
    for i in range(50):
        row = {
            'noir': colors['noir'][i],
            'rouge': colors['rouge'][i],
            'bleu': colors['bleu'][i],
            'vert': colors['vert'][i]
        }
        rows.append(row)
    
    context = {
        'columns': ['noir', 'rouge', 'bleu', 'vert'],
        'rows': rows
    }
    
    return render(request, 'index.html', context)
