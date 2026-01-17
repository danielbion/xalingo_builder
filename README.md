# Xalingo Builder - Render Pieces to PDF

Este projeto gera um arquivo PDF com a renderização de cada peça definida no arquivo `pieces.json` usando o `constructions.json`.

## Instalação

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Uso

Execute o script Python:
```
python render_construction.py
```

Isso criará um arquivo `construction.pdf` contendo a renderização visual de todas as peças.

## Descrição

- Cada peça é desenhada com base em seu formato (square, triangle, arc), largura, altura e cor.
- As formas são escaladas por um fator de 50 pixels por unidade.
- As peças são arranjadas em uma grade no PDF.

## Troubleshooting

- Certifique-se de que o arquivo `construction.json` está no mesmo diretório.
- Se houver erros de cor, verifique se as cores estão definidas no `color_map`.
