# 📊 First End-to-End Data Pipeline & Analytics Dashboard

Select your language / Selecione o idioma:
* [🇧🇷 Versão em Português](#-versão-em-português)
* [🇺🇸 English Version](#-english-version)

---

## 🇧🇷 Versão em Português

### 📌 Sobre o Projeto
Este é o meu primeiro projeto estruturado de Engenharia de Dados ponta a ponta (*End-to-End*). O objetivo principal foi sair da teoria e compreender, na prática, como os dados são extraídos, tratados, protegidos e visualizados em um cenário profissional corporativo.

### 💡 Minha Metodologia de Engenharia Reversa e Aprendizado
Para mim, copiar e colar código pronto sem entender o fundamento não funciona. Como um profissional em busca de posições de **Estágio** ou **Júnior**, eu uso uma abordagem ativa e intencional para fixar conceitos na memória muscular, linha por linha, comando por comando.

Este repositório reflete um código escrito por mim, mas lapidado através do método de **Engenharia Reversa Assistida por IA**:

#### Como eu construo e estudo meus projetos:
1. **Mapeamento da Arquitetura de Blocos:** Antes de digitar uma única linha, eu desenho a lógica macro do pipeline para entender o fluxo de governança (Origem ➔ Tratamento ➔ Segurança ➔ Destino).
2. **Desenvolvimento Ativo:** Eu escrevo as linhas de código estruturais e coloco a mão na massa no terminal, enfrentando os erros de frente.
3. **Refatoração Crítica com IA (Meu Mentor Sênior 24/7):** Eu não uso a Inteligência Artificial apenas para gerar código; eu a utilizo como um tutor particular. Eu a provoco a me explicar o **porquê** de cada decisão sintática, funcional e estrutural.
4. **Domínio da Sintaxe e Delimitadores:** Através desse processo de engenharia reversa, fiz questão de decifrar o papel exato de cada caractere na estrutura do código:
   * `{}` (Chaves): Compreendi seu papel em f-strings e dicionários de mapeamento (como na renomeação de eixos no Plotly: `labels={'coluna': 'Nome Prático'}`).
   * `[]` (Colchetes): Dominei para indexação e localização de colunas no Pandas, aprendendo a debugar na prática os temidos erros de `KeyError`.
   * `()` (Parênteses): Fixei o controle de escopo na passagem de argumentos em funções e chamadas de métodos, evitando fechamentos precoces que quebram a aplicação.
5. **Repetição Deliberada:** Após compreender os fundamentos, os *specifiers* de formatação (como a correção de `:,.0f` para tratar inteiros) e as melhores práticas, eu reescrevo o pipeline do zero para fixar o conhecimento por completo.

### 🛡️ O Pilar Mais Importante: Segurança, Governança e LGPD
Mover dados de um lado para o outro é a parte simples da engenharia. O mercado real exige governança. Por isso, decidi que nenhum projeto meu será apenas "funcional"; ele precisa ser **seguro**. Antes de pensar em gráficos bonitos, o foco absoluto deste pipeline foi a conformidade com a **LGPD (Lei Geral de Proteção de Dados)**.

* **Criptografia e Mascaramento:** Implementei uma camada de segurança robusta desenvolvendo rotinas de criptografia para dados pessoais sensíveis encontrados na camada Raw, garantindo que nenhuma informação identificável de clientes seguisse desprotegida para as etapas seguintes.
* **Gerenciamento de Variáveis de Ambiente:** Garanti a política de *Zero Exposição* de chaves e credenciais no código. O arquivo `.env` (que gerencia as chaves criptográficas) e o ambiente virtual foram estritamente isolados do repositório público via `.gitignore`.
* Entender a segurança desde a base é o que me prepara para ser o profissional maduro e consciente que o mercado corporativo exige.

### 🏗️ Arquitetura e Fluxo dos Dados (Medallion Architecture)
O pipeline foi estruturado utilizando o conceito de camadas para garantir a qualidade, rastreabilidade e integridade do dado:

1. **Camada Raw (Bruta):** Recepção dos dados originais em formato JSON (`vendas_brutas.json`).
2. **Camada Silver (Prata):** Limpeza de dados nulos, padronização de esquemas, normalização de strings e aplicação de criptografia/segurança.
3. **Camada Gold (Ouro):** Agregação dos indicadores financeiros de negócio, salvando o resultado final no formato altamente otimizado **Parquet** (`vendas_v1_final.parquet`).
4. **Camada Analytics (Dashboard):** Interface interativa construída em Python utilizando **Streamlit** e gráficos dinâmicos com **Plotly Express**.

### 👨‍💻 O Processo de Aprendizado Line-by-Line (Sintaxe e Lógica)
Para fixar os comandos na mente, eu fiz questão de estudar e testar função por função. A IA me auxiliou a decifrar e dominar os fundamentos da linguagem que costumam confundir quem está começando:

* **Controle de Fluxo e Robustez (Escudos de Proteção):** Aprendi a implementar blocos `try/except` para criar defesas no carregamento de arquivos, garantindo que a aplicação não quebre caso o arquivo de dados esteja corrompido ou ausente.
* **Filtros Dinâmicos no Pandas:** Compreendi o uso do método `.isin()` combinado com seleções de listas reativas (`st.sidebar.multiselect`) para atualizar os KPIs de vendas e os gráficos instantaneamente.
* **Interface Secura:** Implementei validações de estado do DataFrame (`if not df_filtrado.empty`) para evitar falhas visuais na renderização de gráficos do Plotly quando nenhum filtro estiver selecionado.

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Manipulação de Dados:** Pandas (com estudos contínuos paralelos em PySpark para cenários de Big Data)
* **Visualização:** Streamlit & Plotly Express
* **Armazenamento:** Arquivos estruturados em formato colunar Parquet

### 🚀 Como Executar o Projeto

1. Clone o repositório:
git clone https://github.com/NewBugBountyHunter/first_end_to_end_pipeline.git

2. Acesse a pasta do projeto:
cd first_end_to_end_pipeline

3. Crie e ative um ambiente virtual:
# No Windows:
python -m venv .venv
.venv\Scripts\activate

# No Linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

4. Instale as dependências:
pip install -r data/gold/requirements.txt

5. Execute o servidor do Streamlit:
streamlit run dashboard.py

### 🎯 Conclusão e Próximos Passos
Este projeto representa o meu "ponto de partida". Sei que meu nível técnico atual é inicial e considero meu perfil adequado para posições de entrada, mas a disciplina de abrir het terminal, ler os logs de erro, entender os *specifiers* de formatação e debugar schemas me deu a base necessária para encarar desafios reais de engenharia.

Estou ativamente estudando e praticando de forma exaustiva para me tornar um Engenheiro de Dados qualificado. Conexões, feedbacks e críticas construtivas são sempre muito bem-vindos!

---

## 🇺🇸 English Version

### 📌 About the Project
This is my first structured end-to-end Data Engineering pipeline. The primary goal was to step away from pure theory and understand, in practice, how data is extracted, transformed, secured, and visualized within a professional corporate environment.

### 💡 My Reverse Engineering and Learning Methodology
To me, copying and pasting ready-made code without understanding the underlying fundamentals does not work. As an aspiring professional looking for **Internship** or **Junior** roles, I adopt an active and intentional approach to lock concepts into my muscle memory, line by line, command by command.

This repository reflects code written by me, but refined through a **Reverse Engineering Assisted by AI** methodology:

#### How I build and study my projects:
1. **Mapping the Block Architecture:** Before writing a single line of code, I map out the macro logic of the pipeline to understand the data governance flow (Source ➔ Processing ➔ Security ➔ Destination).
2. **Active Development:** I write the structural lines of code and get hands-on experience directly in the terminal, facing debugging errors head-on.
3. **Critical Refactoring with AI (My 24/7 Senior Mentor):** I do not use Artificial Intelligence simply to generate code; I use it as a private tutor. I challenge it to explain the **why** behind every single syntactic, functional, and structural decision.
4. **Mastering Syntax and Delimiters:** Through this reverse engineering process, I made it a point to decipher the exact role of every character within the codebase:
   * `{}` (Curly Braces): Understood their role in f-strings and mapping dictionaries (such as axes renaming in Plotly: `labels={'column_name': 'Practical Name'}`).
   * `[]` (Square Brackets): Mastered for indexing and locating columns within Pandas DataFrames, learning to debug the notorious `KeyError` exceptions in practice.
   * `()` (Parentheses): Locked down scope control when passing arguments into functions and executing method calls, avoiding premature closures that break application flow.
5. **Deliberate Repetition:** After completely understanding the fundamentals, formatting specifiers (such as adjusting `:,.0f` to handle integers and decimals properly), and architectural best practices, I wipe the slate clean and rewrite the pipeline from scratch to fully consolidate my knowledge.

### 🛡️ The Ultimate Pillar: Security, Governance, and Compliance (LGPD/GDPR)
Moving data from point A to point B is the easy part of engineering. The real-world market demands data governance. Because of this, I decided that none of my projects will ever be just "functional"; they must be **secure**. Before designing any chart, the absolute focus of this pipeline was compliance with data protection principles.

* **Encryption and Masking:** I implemented a robust security layer by developing encryption routines for sensitive personally identifiable information (PII) found in the Raw layer, ensuring that no unmasked client data progressed into downstream steps.
* **Environment Variables Management:** Enforced a strict *Zero Exposure* policy for keys and secrets. The `.env` file (which manages the cryptographic keys) and the virtual environment were completely isolated from the public repository via `.gitignore`.
* Mastering security from the ground up prepares me to be the mature and conscious engineer that the corporate landscape demands.

### 🏗️ Data Architecture & Flow (Medallion Architecture)
The pipeline was structured utilizing the medallion architecture to ensure data quality, traceability, and schema integrity:

1. **Raw Layer:** Ingestion of original data source in JSON format (`vendas_brutas.json`).
2. **Silver Layer:** Missing values handling, schema standardization, string normalization, and data encryption/security application.
3. **Gold Layer:** Aggregation of business financial key performance indicators (KPIs), saving the final output into the highly optimized column-oriented **Parquet** format (`vendas_v1_final.parquet`).
4. **Analytics Layer (Dashboard):** Interactive user interface built in Python leveraging **Streamlit** and dynamic charting with **Plotly Express**.

### 👨‍💻 Line-by-Line Learning Process (Syntax & Logic)
To truly grasp the code, I studied and tested function by function. The AI assisted me in breaking down and mastering core concepts that often challenge beginners:

* **Control Flow and Robustness (Defense Shields):** Learned to implement `try/except` blocks to build safety nets during file loading operations, ensuring the application handles corrupt or missing data gracefully without crashing.
* **Dynamic Filters in Pandas:** Mastered the use of the `.isin()` method paired with reactive multi-select lists (`st.sidebar.multiselect`) to refresh sales KPIs and charts instantly based on user input.
* **Safe Interface Rendering:** Implemented DataFrame state validations (`if not df_filtrado.empty`) to avoid UI errors when rendering Plotly charts if no filters are selected by the user.

### 🛠️ Technologies Used
* **Language:** Python
* **Data Manipulation:** Pandas (with parallel ongoing studies in PySpark for Big Data scenarios)
* **Visualization:** Streamlit & Plotly Express
* **Storage:** Colunar structured files in Parquet format

### 🚀 How to Run the Project

1. Clone the repository:
git clone https://github.com/NewBugBountyHunter/first_end_to_end_pipeline.git

2. Navigate into the project folder:
cd first_end_to_end_pipeline

3. Create and activate a virtual environment:
# On Windows:
python -m venv .venv
.venv\Scripts\activate

# On Linux/macOS:
python3 -m venv .venv
source .venv/bin/activate

4. Install the required dependencies:
pip install -r data/gold/requirements.txt

5. Run the Streamlit server:
streamlit run dashboard.py

### 🎯 Conclusion & Next Steps
This project marks my professional "starting point". While my current technical level is introductory and I classify myself within entry-level roles, the discipline of reading error logs, managing environment variables, adjusting data types, and debugging schemas has provided me with the core foundation required to tackle production-ready challenges.

I am actively studying and practicing exhaustively to become a highly qualified Data Engineer. Connections, feedback, and constructive critiques are always highly appreciated!