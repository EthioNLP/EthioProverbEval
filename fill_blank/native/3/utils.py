from lm_eval.utils import weighted_f1_score


def doc_to_choice(doc):
    choices = [doc['A'],doc['B'],doc['C'],doc['D']]
    return choices

def doc_to_text_amh_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                Given a proverb can you fill the blank with approprate choice word from the choices.
                blank is shown with '___'

                {language} Proverb: {Proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:   
             """

    return output.format(language='Amharic',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])

def doc_to_text_orm_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                Given a proverb can you fill the blank with approprate choice word from the choices.
                blank is shown with '___'

                {language} Proverb: {Proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:   
             """

    return output.format(language='Afann Oromo',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])

def doc_to_text_eng_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                Given a proverb can you fill the blank with approprate choice word from the choices.
                blank is shown with '___'

                {language} Proverb: {Proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:   
             """

    return output.format(language='English',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])


def doc_to_text_tir_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                Given a proverb can you fill the blank with approprate choice word from the choices.
                blank is shown with '___'

                {language} Proverb: {Proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:   
             """

    return output.format(language='Tigregya',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])


def doc_to_text_gez_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                Given a proverb can you fill the blank with approprate choice word from the choices.
                blank is shown with '___'

                {language} Proverb: {Proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:   
             """

    return output.format(language='Geez',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])


