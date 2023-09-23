!pip install transformers
import spacy
import transformers

class SmartBot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.bart = transformers.AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
        self.tokenizer = transformers.AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

    def process_document(self, document):
        """Processes a document to extract the relevant text and data.

        Args:
            document: The document to process.

        Returns:
            A dictionary of the extracted text and data.
        """

        doc = self.nlp(document)

        # Extract the relevant text from the document.
        text = doc.text

        return {"text": text}

    def generate_response(self, query, document):
        """Generates a response to a user query about a document.

        Args:
            query: The user query.
            document: The document to query.

        Returns:
            A response to the user query.
        """

        # Tokenize the input for the BART model.
        input_text = f"Query: {query}\nDocument: {document}"
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=1024, truncation=True)

        # Generate a response to the user query using the BART language model.
        response_ids = self.bart.generate(input_ids, max_length=1024, num_return_sequences=1)

        # Decode the response.
        response = self.tokenizer.decode(response_ids[0], skip_special_tokens=True)

        return response

    def query(self, query, document):
        """Queries a document and returns a response to the user query.

        Args:
            query: The user query.
            document: The document to query.

        Returns:
            A response to the user query.
        """

        response = self.generate_response(query, document)

        return response

# Example usage:

smart_bot = SmartBot()

# Process the document.

document = "This is a document about the history of the world."
document_info = smart_bot.process_document(document)

# Ask a question about the document.

query = "What is the relationship between the United States and the United Kingdom?"

# Generate a response to the question.

response = smart_bot.generate_response(query, document)

# Print the response.

print(response)

import spacy
import transformers

class SmartBot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.bart = transformers.AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
        self.tokenizer = transformers.AutoTokenizer.from_pretrained("facebook/bart-large-cnn")

    def process_document(self, document):
        """Processes a document to extract the relevant text and data.

        Args:
            document: The document to process.

        Returns:
            A dictionary of the extracted text and data.
        """
        doc = self.nlp(document)
        # Extract the relevant text from the document.
        text = doc.text
        return {"text": text}

    def generate_response(self, query, document):
        """Generates a response to a user query about a document.

        Args:
            query: The user query.
            document: The document to query.

        Returns:
            A response to the user query.
        """
        # Tokenize the input for the BART model.
        input_text = f"Query: {query}\nDocument: {document}"
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=1024, truncation=True)

        # Generate a response to the user query using the BART language model.
        response_ids = self.bart.generate(input_ids, max_length=1024, num_return_sequences=1)

        # Decode the response.
        response = self.tokenizer.decode(response_ids[0], skip_special_tokens=True)

        return response

    def query(self, query, document):
        """Queries a document and returns a response to the user query.

        Args:
            query: The user query.
            document: The document to query.

        Returns:
            A response to the user query.
        """
        response = self.generate_response(query, document)
        return response

# Example usage:

smart_bot = SmartBot()

# Process the document.
document = "The relationship between the United States and the United Kingdom has evolved significantly over time. In this document, we explore the historical context and key events that have shaped this relationship."
document_info = smart_bot.process_document(document)

# Ask a question about the document.
query = "What are some key events that have shaped the relationship between the United States and the United Kingdom?"

# Generate a response to the question.
response = smart_bot.generate_response(query, document)

# Print the response.
print(response)


!pip install PyPDF2
import spacy
import transformers
import PyPDF2
from transformers import pipeline
from google.colab import files

class SmartBot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.bart = transformers.AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
        self.tokenizer = transformers.AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.document = None
        self.qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

    def process_document(self, pdf_path):
        text = ""
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        self.document = text

    def generate_response(self, query):
        result = self.qa_pipeline(question=query, context=self.document)
        return result['answer']

    def start_conversation(self):
        print("Hello! How can I help you today? Please upload a PDF document.")

        while True:
            uploaded_files = files.upload()

            if not uploaded_files:
                print("No PDF file uploaded. Please upload a PDF document.")
                continue

            pdf_file_name = list(uploaded_files.keys())[0]
            self.process_document(pdf_file_name)
            print("Bot: Document uploaded and processed. You can now ask questions.")

            while True:
                user_input = input("User: ")

                if user_input.lower() == "exit":
                    print("Goodbye!")
                    return

                response = self.generate_response(user_input)
                print("Bot:", response)

if __name__ == "__main__":
    smart_bot = SmartBot()
    smart_bot.start_conversation()



