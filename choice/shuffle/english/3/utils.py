from lm_eval.utils import weighted_f1_score


def doc_to_choice(doc):
    choices = [doc['A'],doc['B'],doc['C'],doc['D']]
    return choices

def doc_to_text_amh_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                I will give you prompt and list of descriptions that have the same meaing.
                return a letter for the correct choice among four choices given



                {language} Proverb: {proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:"""

    return output.format(language='Amharic',proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])

def doc_to_text_orm_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                I will give you prompt and list of descriptions that have the same meaing.
                return a letter for the correct choice among four choices given



                {language} Proverb: {proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:"""

    return output.format(language='Afann Oromo',proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])

def doc_to_text_eng_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                I will give you prompt and list of descriptions that have the same meaing.
                return a letter for the correct choice among four choices given



                {language} Proverb: {proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:"""

    return output.format(language='English',proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])


def doc_to_text_tir_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                I will give you prompt and list of descriptions that have the same meaing.
                return a letter for the correct choice among four choices given



                {language} Proverb: {proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:"""

    return output.format(language='Tigregya',proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])



def doc_to_text_gez_t1(doc):
    output = """
                You are LLM capable of undersatnding {language} language. 
                I will give you prompt and list of descriptions that have the same meaing.
                return a letter for the correct choice among four choices given



                {language} Proverb: {proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:"""

    return output.format(language='Geez',proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])

