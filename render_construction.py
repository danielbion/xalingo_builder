from reportlab.pdfgen import canvas
from reportlab.lib.colors import green, red, blue, white, black
from reportlab.lib.colors import Color
import json

# Load pieces and constructions from JSON
with open('pieces.json', 'r') as f:
    pieces = json.load(f)

with open('constructions.json', 'r') as f:
    constructions = json.load(f)

# Create PDF canvas
c = canvas.Canvas('construction.pdf')

# Define colors
color_map = {
    'green': green,
    'red': red,
    'blue': blue,
    'beige': Color(0.96, 0.96, 0.86)  # Approximate beige
}

# Scale factor for sizes and positions
scale = 60

# Draw each construction on a separate page
def draw_square(c, x, y_bottom, width, height, color):
    c.setFillColor(color)
    c.rect(x, y_bottom, width, height, fill=1, stroke=1)

def draw_triangle(c, x, y_bottom, width, height, color):
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(x, y_bottom)
    p.lineTo(x + width, y_bottom)
    p.lineTo(x + width / 2, y_bottom + height)
    p.close()
    c.drawPath(p, fill=1, stroke=1)

def draw_arc_6(c, x, y, width, height, color):
    c.setFillColor(color)
    c.rect(x, y, width, height, fill=1, stroke=1)
    c.setFillColor(white)
    c.wedge(x + width/5, 
            y - height + (height/3), 
            x + width - (width/5), 
            y + (height/1.5), 
            0, 180, fill=1, stroke=1)
    c.setFillColor(color)

def draw_arc_7(c, x, y, width, height, color):
    c.setFillColor(color)
    c.rect(x, y, width, height, fill=1, stroke=1)
    c.setFillColor(white)
    c.wedge(x + width/5, 
            y - height + (height/3), 
            x + width - (width/5), 
            y + (height/1.5), 
            0, 180, fill=1, stroke=1)
    c.setFillColor(color)

# Draw each construction on a separate page
for level, construction in constructions.items():
    # Calculate construction dimensions
    min_x = min(item['x'] for item in construction)
    max_x = max(item['x'] + next(p['width'] for p in pieces if p['id'] == item['piece_id']) for item in construction)
    total_width = (max_x - min_x) * scale

    min_y = min(item['y'] for item in construction)
    max_y = max(item['y'] + next(p['height'] for p in pieces if p['id'] == item['piece_id']) for item in construction)
    total_height = (max_y - min_y) * scale

    # Page size (A4)
    page_width = 595
    page_height = 842
    offset_x = (page_width - total_width) / 2
    offset_y = (page_height - total_height) / 2

    c.setStrokeColor(black)
    
    for item in construction:
        piece_id = item['piece_id']
        x_pos = (item['x'] * scale) + offset_x
        y_pos = (item['y'] * scale) + offset_y
        
        # Find the piece details
        piece = next(p for p in pieces if p['id'] == piece_id)
        width = piece['width'] * scale
        height = piece['height'] * scale
        color = color_map.get(piece['color'], red)
        
        if piece_id == 'window':
            draw_square(c, x_pos, y_pos, width, height, color)
        elif piece_id == '2x window':
            draw_square(c, x_pos, y_pos, width, height, color)
        elif piece_id == 'tower clock':
            draw_square(c, x_pos, y_pos, width, height, color)
        elif piece_id == 'small roof':
            draw_triangle(c, x_pos, y_pos, width, height, color)
        elif piece_id == 'large roof':
            draw_triangle(c, x_pos, y_pos, width, height, color)
        elif piece_id == 'bridge':
            draw_arc_6(c, x_pos, y_pos, width, height, color)
        elif piece_id == 'door':
            draw_arc_7(c, x_pos, y_pos, width, height, color)
    
    # New page for next construction
    c.showPage()

# Save the PDF
c.save()

print("PDF generated: construction.pdf")