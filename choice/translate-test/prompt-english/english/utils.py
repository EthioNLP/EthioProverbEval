from lm_eval.utils import weighted_f1_score
import os

# Set an environment variable
T=os.getenv('T_PROMPT')
print(T)

output = ["""
                You are LLM capable of undersatnding {language} language. 
                I will give you prompt and list of descriptions that have the same meaing.
                return a letter for the correct choice among four choices given



                {language} Proverb: {Proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:""",
                """
                You are LLM capable of undersatnding language. 
                I will give you prompt and list of descriptions that have the same meaing.
                return a letter for the correct choice among four choices given



                Proverb: {Proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:""",
                """
                Which choice are simmilar 
                  
                Proverb: {Proverb}


                Choices

                A: {A}
                B: {B}
                C: {C}
                D: {D}


                Answer:"""
                  ]

def doc_to_choice(doc):
    choices = [doc['A'],doc['B'],doc['C'],doc['D']]
    return choices

def doc_to_text_amh_t1(doc):
    if T == '1':
        result = output[0].format(language='English',Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output[1].format(Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output[2].format(language='English',Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result


def doc_to_text_tir_t1(doc):
    if T == '1':
        result = output[0].format(language='English',Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output[1].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output[2].format(language='English',Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result

def doc_to_text_orm_t1(doc):
    if T == '1':
        result = output[0].format(language='English',Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output[1].format(Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output[2].format(language='English',Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result

def doc_to_text_gez_t1(doc):
    if T == '1':
        result = output[0].format(language='English',Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output[1].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output[2].format(language='English',Proverb=doc["tranalste"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result
