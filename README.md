
# 📊 Consulta de Dados via CNPJ

Aplicação web desenvolvida com **Python** e **Streamlit** para realizar consultas públicas de CNPJs de empresas brasileiras utilizando a API do [CNPJ.ws](https://publica.cnpj.ws/). Os dados são apresentados de forma tabular e também podem ser exportados para um arquivo Excel.

---

## 🚀 Funcionalidades

* Entrada personalizada para CNPJ (com máscara 00.000.000/0000-00)
* Consulta de dados principais da empresa:

  * Razão Social
  * Nome Fantasia
  * Natureza Jurídica
  * Porte
  * Capital Social
  * Situação Cadastral
  * Regime do Simples Nacional
  * CNAE Principal e Atividades Secundárias
  * Localização e contato
  * Informações dos Sócios
  * Inscrições Estaduais
* Download dos dados em formato **.xlsx**

---

## 🖼️ Interface

A interface foi construída com Streamlit, oferecendo uma experiência limpa e intuitiva. Os dados são apresentados em diferentes seções:

* **Dados da Empresa**
* **Atividades Secundárias**
* **Inscrições Estaduais**
* **Sócios**

Além disso, é possível baixar todos os dados consolidados em um único arquivo Excel com múltiplas abas.

---

## 📦 Tecnologias Utilizadas

* [Python 3.10+](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Requests](https://docs.python-requests.org/)
* [OpenPyXL](https://openpyxl.readthedocs.io/)

---

## 🧪 Como Executar Localmente

1. Clone este repositório:

```bash
git clone https://github.com/Adolfo-Hugo/consulta-cnpj-streamlit.git
cd consulta-cnpj-streamlit
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

---

## 📎 Exemplo de Uso

Acesse a aplicação em:
🌐 [Portfólio Interativo](https://adolfohugosilvaportifolio.streamlit.app)

---

## 📇 Contato

* 💼 [LinkedIn](https://www.linkedin.com/in/adolfo-hugo-silva-a298751aa)
* 💻 [GitHub](https://github.com/Adolfo-Hugo)
* 📧 [adolfohugosilva@gmail.com](mailto:adolfohugosilva@gmail.com)
* 📱 WhatsApp: (82) 99683-8463

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

