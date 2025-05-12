from lm_eval.utils import weighted_f1_score
import os

# Set an environment variable
T=os.getenv('T_PROMPT')
print(T)

output = {
'amh':["""
                አንተ {language} ቋንቋ መረዳት የምትችል የኮምፒውተር ማሽን ነህ። 
               በመቀጠል ምሳሌያዊ አነጋገር እና ትርጉሞች ሰጥሃለሁ
               ከተሰጡት አራት ምርጫዎች መካከል ለትክክለኛው ምርጫ ፊደል ይመልሱ


                {language} ምሳሌያዊ አነጋገር፦ {Proverb}


                ምርጫ

                ሀ: {A}
                ለ: {B}
                ሐ: {C}
                መ: {D}


                መልስ፦""",
                """
                አንተ ቋንቋዎችን መረዳት የምትችል የኮምፒውተር ማሽን ነህ። 
               በመቀጠል ምሳሌያዊ አነጋገር እና ትርጉሞች ሰጥሃለሁ
               ከተሰጡት አራት ምርጫዎች መካከል ለትክክለኛው ምርጫ ፊደል ይመልሱ


                ምሳሌያዊ አነጋገር፦ {Proverb}


                ምርጫ

                ሀ: {A}
                ለ: {B}
                ሐ: {C}
                መ: {D}


                መልስ፦""",
                """
                የትኛው ምርጫ ተመሳሳይ ነው?

                ምሳሌያዊ አነጋገር፦ {Proverb}


                ምርጫ

                ሀ: {A}
                ለ: {B}
                ሐ: {C}
                መ: {D}


                መልስ፦"""],
'eng':["""
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
                  ],
'tir':["""
       ንስኻ {language} ዝተብሃለ ቋንቋ ናይ ምርዳእ ዓቕሚ ዘለካ ዓብዪ ናይ ቋንቋ ስልጡን ኢኻ። ዝርዝር ተመሳሳሊ ትርጉም ዘለዎም መግለጺታት ምስ መጠየቕታ ክህበካ እየ። ካብቶም ኣርባዕተ ምርጫታት ቕኑዕ ዝኾነ መልሲ ዝሓዘ መማረፂ ፊደል ምረፅ
        {language} ምስላ፡ {Proverb}
        ምርጫታት
        ሀ፡ {A}
        ለ፦ {B}
        ሐ: {C}
        መ: {D}
        መልሲ: """,
        """
        ንስኻ ቋንቋ ናይ ምርዳእ ዓቕሚ ዘለካ ዓብዪ ናይ ቋንቋ ስልጡን ኢኻ። ዝርዝር ተመሳሳሊ ትርጉም ዘለዎም መግለጺታት ምስ መጠየቕታ ክህበካ እየ። ካብቶም ኣርባዕተ ምርጫታት ቕኑዕ ዝኾነ መልሲ ዝሓዘ መማረፂ ፊደል ምረፅ

        ምስላ፡ {Proverb}
        ምርጫታት
        ሀ፡ {A}
        ለ፦ {B}
        ሐ: {C}
        መ: {D}
        መልሲ: """,
        """
        ኣየናይ ምርጫ እዩ ተመሳሳሊ
        ምስላ፡ {Proverb}

        ምርጫታት
        ሀ፡ {A}
        ለ፦ {B}
        ሐ: {C}
        መ: {D} 
        መልሲ: """],
'orm':["""
        Ati LLM dandeetti afaan {language} hubachuu qabdudha.
        Gaaffii fi fillannoowwan hiikaa/eergaa ibsan sif nan laadha. 
        Filannoowwan afur keennaman keessaa quubee deebiin sirri irra jiru naaf deebisii.

        {language} Mammaaksa: {Proverb}
        Filannoowwan
        A: {A}
        B: {B}
        C: {C}
        D: {D}
        Deebii:""",
        """
        Ati LLM dandeetti afaan hubachuu qabdudha. You are LLM capable of understanding language. 
        Gaaffii fi fillannoowwan hiikaa/eergaa ibsan sif nan laadha. 
        Filannoowwan afur keennaman keessaa quubee deebiin sirri irra jiru naaf deebisii.
        Mammaaksa: {Proverb}
        Filannoowwan
        A: {A}
        B: {B}
        C: {C}
        D: {D}
        Deebii:""",
        """
        Fiilannoowwan armaan gadii keessaa kamtuu hiika/eergaa walfakkaataa qaba
        Mammaaksa: {Proverb}

        Filannoowwan
        A: {A}
        B: {B}
        C: {C}
        D: {D}

        Deebii:"""],
'gez':[""" 
       አንተ ውእቱ ኪን ዘትጠይቅ ወዘተአምር ልሳነ ግእዝ። እምዘታሕቱ ዘተዳለዉ እማሬያት በኀርዮ አውስእ (ኅረይ) ፊደለ ዘስንእው  እምዘተደለወ አንጋረ ምሳሌ።
        {language}  አንጋረ ምሳሌ፦ {Proverb}
        Choices
        A: {A}
        B: {B}
        C: {C}
        D: {D}
        አውሥዖት፦""",
        """ 
        አንተ ውእቱ ኪን ዘትጠይቅ ወዘተአምር ልሳነ ግእዝ። እምዘታሕቱ ዘተዳለዉ እማሬያት በኀርዮ አውስእ (ኅረይ) ፊደለ ዘስንእው  እምዘተደለወ አንጋረ ምሳሌ።

        አንጋረ ምሳሌ፦ {Proverb}
        Choices
        A: {A}
        B: {B}
        C: {C}
        D: {D}
        አውሥዖት፦""",
        """ አይ ውእቱ አንጋረ ምሳሌ ዕሩየ ዘኮነ አው ዘይቀርብ ምስለ እለተደለዉ አንጋረ ምሳሌያት እምዘታሕቱ። 

        አንጋረ ምሳሌ፦ {Proverb}

        ሀ: {A}
        ለ: {B}
        ሐ: {C}
        መ: {D}
        አውሥዖት፦"""]

}

def doc_to_choice(doc):
    choices = [doc['A'],doc['B'],doc['C'],doc['D']]
    return choices

def doc_to_text_amh_t1(doc):
    if T == '1':
        result = output['amh'][0].format(language='አማረኛ',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output['amh'][1].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output['amh'][2].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result

def doc_to_text_tir_t1(doc):
    if T == '1':
        result = output['tir'][0].format(language='ትግረኛ',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output['tir'][1].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output['tir'][2].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result

def doc_to_text_orm_t1(doc):
    if T == '1':
        result = output['orm'][0].format(language='Afann Oromo',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output['orm'][1].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output['orm'][2].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result

def doc_to_text_gez_t1(doc):
    if T == '1':
        result = output['gez'][0].format(language='ግእዝ',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output['gez'][1].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output['gez'][2].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result

def doc_to_text_eng_t1(doc):
    if T == '1':
        result = output[0].format(language='English',Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '2':
        result = output[1].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    if T == '3':
        result = output[2].format(Proverb=doc["Proverb"],A=doc['A'],B=doc['B'],C=doc['C'],D=doc['D'])
    return result
