# Documentação do Código - Minicurso de Reconhecimento Facial

Este projeto utiliza Streamlit e DeepFace para criar uma aplicação de reconhecimento facial. Abaixo está a documentação dos principais arquivos Python presentes na pasta `app/`.

---

## Comandos necessários para rodar a aplicação:

Dentro da pasta raiz do projeto, ou seja, a que possui app/, .gitignore, README.md e requirements.txt, rode:
```bash
pip install -r requirements.txt
```
```bash
sudo apt-get update
```

```bash
sudo apt install libgl1
```


## main.py
Arquivo principal da aplicação Streamlit para reconhecimento facial.

Comando para rodar aplicação:

```bash
streamlit run main.py
```

- Cria a navegação entre as páginas do frontend usando `st.navigation`.
- Executa a página selecionada com `page.run()`.

---

## backend/face_recognition/face_recognition_engine.py
Módulo principal de reconhecimento facial. Utiliza a biblioteca DeepFace para extrair características faciais e realizar comparações.

### Classe: `FaceRecognitionEngine`
Engine de reconhecimento facial que gerencia extração de características e comparação de faces.

- **Atributos:**
  - `fr_model (str)`: Modelo usado para reconhecimento facial (Facenet por padrão).
  - `fd_model (str)`: Modelo usado para detecção facial (centerface por padrão).
  - `threshold (float)`: Limiar de similaridade para considerar faces como matching.

- **Métodos:**
  - `__init__`: Inicializa o engine de reconhecimento facial com modelos padrão.
  - `match_faces(img1, img2)`: Compara duas imagens e verifica se são da mesma pessoa.
    - Parâmetros: `img1`, `img2` (arquivos upados)
    - Retorno: `bool` (True se forem da mesma pessoa, False caso contrário)
  - `__extract_template(img, num_img)`: Extrai o template (template) facial de uma imagem usando DeepFace.
    - Parâmetros: `img` (array numpy), `num_img` (índice da imagem)
    - Retorno: `list` de templates
    - Exceção: `NoFacesException` se nenhuma face for detectada
  - `__check_single_face_detected(templates, num_img)`: Verifica se apenas uma face foi detectada na imagem.
    - Parâmetros: `templates` (lista de templates), `num_img` (índice da imagem)
    - Exceção: `MultiFacesException` se mais de uma face for detectada
  - `__compare_templates(template1, template2)`: Compara dois templates faciais usando distância do cosseno.
    - Parâmetros: `template1`, `template2` (templates)
    - Retorno: `bool` (True se forem da mesma pessoa, False caso contrário)

---

## backend/utils/utils.py
Módulo com funções utilitárias para manipulação de imagens.

### Função: `convert_img_to_array(imagem_upada)`
Converte uma imagem enviada via Streamlit em um array numpy (BGR).
- Parâmetros: `imagem_upada` (objeto FileUploader do Streamlit)
- Retorno: `numpy.ndarray` representando a imagem no formato BGR

---

## backend/exceptions/multi_faces_exception.py
Exceção customizada para quando múltiplas faces são detectadas em uma imagem.

### Classe: `MultiFacesException`
Exceção lançada quando mais de uma face é detectada em uma imagem onde deveria haver apenas uma.
- Parâmetros: `msg (str)` - Mensagem de erro descrevendo o problema

---

## backend/exceptions/no_faces_exception.py
Exceção customizada para quando nenhuma face é detectada em uma imagem.

### Classe: `NoFacesException`
Exceção lançada quando nenhuma face é detectada em uma imagem onde deveria haver pelo menos uma.
- Parâmetros: `msg (str)` - Mensagem de erro descrevendo o problema

---

## frontend/match_faces_page.py
Página Streamlit para comparação 1:1 entre duas faces.

- Permite o upload de duas imagens e exibe o resultado da comparação, indicando se são ou não a mesma pessoa.
- Utiliza o engine de reconhecimento facial para processar as imagens.
- Exibe mensagens de erro caso não haja faces ou haja múltiplas faces em alguma imagem.

---

## frontend/search_faces_page.py
(sem código implementado)

---
