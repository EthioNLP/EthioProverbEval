prompt = """
        You are LLM capable of undersatnding {source_language} language. 
        Based on the detailed description provided in {source_language}, generate an appropriate proverb in {target_language} that captures the essence and meaning of the context.

        {source_language} Description: {Description}
        {target_language} Proverb:"""



def doc_to_text_amh(doc):
    output = prompt
    return output.format(source_language="English",target_language="Amharic",Description=doc["Description"])

def doc_to_text_eng(doc):
    output = prompt
    return output.format(source_language="English",target_language="English",Description=doc["Description"])

def doc_to_text_gez(doc):
    output = prompt
    return output.format(source_language="English",target_language="English",Description=doc["Description"])

def doc_to_text_orm(doc):
    output = prompt
    return output.format(source_language="English",target_language="Afaan Oromoo",Description=doc["Description"])

def doc_to_text_tir(doc):
    output = prompt
    return output.format(source_language="English",target_language="Tigrinya",Description=doc["Description"])