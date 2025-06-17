#!/usr/bin/env python3
"""
Script para gerar imagens representativas para a página inicial
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Diretório das imagens
IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
os.makedirs(IMAGE_DIR, exist_ok=True)

def create_image_with_text(filename, text, background_color=(255, 228, 230), text_color=(199, 21, 133)):
    """Cria uma imagem com texto centralizado"""
    # Configuração da imagem
    width, height = 800, 400
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)
    
    # Desenhar um gradiente simples
    for y in range(height):
        r = int(background_color[0] * (1 - y/height * 0.3))
        g = int(background_color[1] * (1 - y/height * 0.3))
        b = int(background_color[2] * (1 - y/height * 0.3))
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Tentar carregar uma fonte, senão usar a fonte padrão
    try:
        font_size = 50
        font = ImageFont.truetype("Arial.ttf", font_size)
    except IOError:
        try:
            # Tente outro nome de fonte comum
            font = ImageFont.truetype("DejaVuSans.ttf", 50)
        except IOError:
            # Use a fonte padrão se não conseguir carregar nenhuma
            font = ImageFont.load_default()
    
    # Adicionar texto
    text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (300, 50)
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    # Desenhar borda decorativa
    border_width = 10
    draw.rectangle([(border_width, border_width), 
                   (width - border_width, height - border_width)], 
                  outline=text_color, width=border_width)
    
    # Desenhar texto
    draw.text(position, text, fill=text_color, font=font)
    
    # Desenhar elementos decorativos específicos para cada imagem
    if "root" in filename.lower():
        # Para o método de encontrar raízes (função cruzando o eixo x)
        draw.line([(100, height//2), (width-100, height//2)], fill=text_color, width=3)  # eixo x
        draw.line([(width//2, 100), (width//2, height-100)], fill=text_color, width=3)  # eixo y
        
        # Desenha uma curva que cruza o eixo x
        points = []
        for x in range(100, width-100, 5):
            # Cria uma função senoidal que cruza o eixo x
            rel_x = (x - width/2) / 100
            y = height/2 - 80 * rel_x * (rel_x**2 - 2)
            points.append((x, y))
        
        # Desenha a curva
        if len(points) >= 2:
            for i in range(1, len(points)):
                draw.line([points[i-1], points[i]], fill=text_color, width=4)
                
        # Marca a raiz
        draw.ellipse([(width//2-8, height//2-8), (width//2+8, height//2+8)], 
                     fill=(255, 105, 180), outline=text_color, width=2)
    
    else:
        # Para o método de Gauss (matriz e vetor)
        # Desenha uma matriz simplificada
        cell_size = 40
        rows, cols = 3, 4
        start_x = (width - cols * cell_size) // 2
        start_y = (height - rows * cell_size) // 2
        
        for i in range(rows):
            for j in range(cols):
                x1 = start_x + j * cell_size
                y1 = start_y + i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                
                # Desenha o retângulo da célula
                draw.rectangle([(x1, y1), (x2, y2)], outline=text_color, width=2)
                
                # Adiciona um caractere na célula (a, b, c, etc.)
                cell_text = chr(97 + i * cols + j) if j < cols - 1 else str(i+1)
                text_pos = (x1 + cell_size//2 - 5, y1 + cell_size//2 - 10)
                draw.text(text_pos, cell_text, fill=text_color, font=font)
                
        # Coluna de "=" para separar a matriz dos resultados
        draw.text((start_x + (cols-1) * cell_size - 5, start_y + cell_size), "=", fill=text_color, font=font)
    
    # Salvar imagem
    filepath = os.path.join(IMAGE_DIR, filename)
    image.save(filepath)
    print(f"Imagem criada: {filepath}")
    return filepath

if __name__ == "__main__":
    # Criar as imagens
    create_image_with_text("root-finding.png", "Cálculo de Raízes")
    create_image_with_text("linear-system.png", "Eliminação de Gauss")
    
    print("Imagens geradas com sucesso!")
