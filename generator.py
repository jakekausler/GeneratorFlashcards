from ctypes.wintypes import PSHORT
import re
import random

groups = {}
sentences = []
words = {}

PHRASE = 'PE'

VERB = 'VB'
NOUN = 'NN'
ADJECTIVE = 'AJ'
PRONOUN = 'PN'
PARTS_OF_SPEECH = [
    VERB,
    NOUN,
    ADJECTIVE,
    PRONOUN,
]

INFINITIVE = 'INF'
PARTICIPLE = 'PAR'
IMPERATIVE = 'IMP'
INDICATIVE = 'IND'
SUBJUNCTIVE = 'SUB'
OPTATIVE = 'OPT'
MOODS = [
    INFINITIVE,
    PARTICIPLE,
    IMPERATIVE,
    INDICATIVE,
    SUBJUNCTIVE,
    OPTATIVE
]

PRES = 'PRES'
TENSES = [
    PRES
]

NOMINITIVE = 'N'
GENITIVE = 'G'
DATIVE = 'D'
ACCUSATIVE = 'A'
VOCATIVE = 'V'
CASES = [
    NOMINITIVE,
    GENITIVE,
    DATIVE,
    ACCUSATIVE,
    VOCATIVE
]

ACTIVE = 'C'
MIDDLE = 'L'
PASSIVE = 'I'
VOICES = [
    ACTIVE,
    MIDDLE,
    PASSIVE
]

SINGULAR = 'S'
PLURAL = 'P'
NUMBERS = [
    SINGULAR,
    PLURAL
]

FIRST = '1'
SECOND = '2'
THIRD = '3'
PERSONS = [
    FIRST,
    SECOND,
    THIRD
]

MASCULINE = 'M'
FEMININE = 'F'
NEUTER = 'E'
GENDERS = [
    MASCULINE,
    FEMININE,
    NEUTER
]

def choose_valid_word(word):
    choices = filters[word.pos](word)
    if choices:
        return random.choice(choices)[0]

def filter_nouns(word):
    choices = []
    try:
        choices = words[NOUN][word.number][word.case].keys()
    except:
        pass
    return choices

def filter_verbs(word):
    choices = []
    try:
        if word.mood == INFINITIVE:
            choices = words[VERB][words.mood][words.tense][word.voice].keys()
        elif word.mood == PARTICIPLE:
            choices = words[VERB][words.mood][words.tense][word.voice][word.number][word.gender][word.case].keys()
        else:
            choices = words[VERB][words.mood][words.tense][word.voice][word.number][word.person].keys()
    except:
        pass
    return choices

def filter_adjectives(word):
    choices = []
    try:
        if word.baseword == 'PersonalPronoun':
            choices =  words[PRONOUN][word.person][word.number][word.case].keys()
        else:
            choices =  words[PRONOUN][word.person][word.number][word.gender][word.case].keys()
    except:
        pass
    return choices

def filter_pronouns(word):
    choices = []
    try:
        choices = words[PRONOUN]
    except:
        pass
    return choices

def generate_noun(word):
    valid_word = None
    while not valid_word:
        if word.number not in NUMBERS:
            word.number = random.choice(NUMBERS)
        if word.cases not in CASES:
            word.cases = random.choice(CASES)
        valid_word = choose_validchoose_valid_word(word)
    word.baseword = valid_word

def generate_verb(word):
    valid_word = None
    while not valid_word:
        if word.mood not in MOODS:
            word.mood = random.choice(MOODS)
        if word.voice not in VOICES:
            word.voice = random.choice(VOICES)
        if word.mood == INFINITIVE:
            if word.tense not in TENSES:
                word.tense = random.choice(TENSES)
        elif word.mood == PARTICIPLE:
            if word.tense not in TENSES:
                word.tense = random.choice(TENSES)
            if word.number not in NUMBERS:
                word.number = random.choice(NUMBERS)
            if word.gender not in GENDERS:
                word.gender = random.choice(GENDERS)
            if word.case not in CASES:
                word.case = random.choice(CASES)
        elif word.mood == INDICATIVE:
            if word.tense not in TENSES:
                word.tense = random.choice(TENSES)
            if word.number not in NUMBERS:
                word.number = random.choice(NUMBERS)
            if word.person not in PERSONS:
                word.person = random.choice(PERSONS)
        elif word.mood == SUBJUNCTIVE:
            if word.tense not in TENSES:
                word.tense = random.choice(TENSES)
            if word.number not in NUMBERS:
                word.number = random.choice(NUMBERS)
            if word.person not in PERSONS:
                word.person = random.choice(PERSONS)
        elif word.mood == OPTATIVE:
            if word.tense not in TENSES:
                word.tense = random.choice(TENSES)
            if word.number not in NUMBERS:
                word.number = random.choice(NUMBERS)
            if word.person not in PERSONS:
                word.person = random.choice(PERSONS)
        elif word.mood == IMPERATIVE:
            if word.tense not in TENSES:
                word.tense = random.choice(TENSES)
            if word.number not in NUMBERS:
                word.number = random.choice(NUMBERS)
            if word.person not in PERSONS:
                word.person = random.choice(filter(FIRST.__ne__, PERSONS))
        valid_word = choose_valid_word(word)
    word.baseword = valid_word

def generate_adjective(word):
    valid_word = None
    while not valid_word:
        if word.number not in NUMBERS:
            word.number = random.choice(NUMBERS)
        if word.gender not in GENDERS:
            word.gender = random.choice(GENDERS)
        if word.cases not in CASES:
            word.cases = random.choice(CASES)
        valid_word = choose_valid_word(word)
    word.baseword = valid_word

def generate_pronoun(word):
    valid_word = None
    while not valid_word:
        if word.number not in NUMBERS:
            word.number = random.choice(NUMBERS)
        if word.cases not in CASES:
            word.cases = random.choice(CASES)
        if word.baseword == 'DemonstrativePronoun':    
            if word.gender not in GENDERS:
                word.gender = random.choice(GENDERS)
        valid_word = choose_valid_word(word)
    word.baseword = valid_word

def generate_phrase(phrase):
    pass

def stringify_noun(word):
    return words[NOUN][word.number][word.case][word.baseword][0]

def stringify_verb(word):
    if word.mood == INFINITIVE:
        return words[VERB][word.mood][word.tense][word.voice][word.baseword][0]
    elif word.mood == PARTICIPLE:
        return words[VERB][word.mood][word.tense][word.voice][word.number][word.gender][word.case][word.baseword][0]
    else:
        return words[VERB][word.mood][word.tense][word.voice][word.number][word.person][word.baseword][0]

def stringify_adjective(word):
    return words[ADJECTIVE][word.number][word.gender][word.case][word.baseword][0]

def stringify_pronoun(word):
    if word.baseword == 'PersonalPronoun':
        return words[PRONOUN][word.person][word.number][word.case][word.baseword][0]
    else:
        return words[PRONOUN][word.person][word.number][word.gender][word.case][word.baseword][0]

def stringify_phrase(phrase):
    return phrase.baseword if phrase.baseword else phrase.group

generators = {
    NOUN: generate_noun,
    VERB: generate_verb,
    ADJECTIVE: generate_adjective,
    PRONOUN: generate_pronoun,
    PHRASE: generate_phrase,
}

stringifiers = {
    NOUN: stringify_noun,
    VERB: stringify_verb,
    ADJECTIVE: stringify_adjective,
    PRONOUN: stringify_pronoun,
    PHRASE: stringify_phrase,
}

filters = {
    NOUN: filter_nouns,
    VERB: filter_verbs,
    ADJECTIVE: filter_adjectives,
    PRONOUN: filter_pronouns,
}

class BaseWord:
    def __init__(self):
        self.word = None
    
    def generate(self, group):
        self.word = random.choice(groups[group])

class GreekSentencePart:
    def __init__(self, baseword=None, group=None, pos=None, case=None, number=None, tense=None, mood=None, voice=None, person=None, gender=None):
        self.baseword = baseword
        self.pos = pos
        self.group = group
        self.case = case
        self.number = number
        self.tense = tense
        self.mood = mood
        self.voice = voice
        self.person = person
        self.gender = gender

    def generate(self):
        return generators[self.pos](self)
    
    def __str__(self):
        return stringifiers[self.pos](self)

class EnglishSentencePart:
    def __init__(self):
        pass

class Sentence:
    def __init__(self, greek, english):
        self.greek = greek
        self.english = english
    
    def generate(self):
        for part in self.greek:
            if isinstance(part, GreekSentencePart):
                part.generate()
    
    def __str__(self):
        return " ".join([str(p) for p in self.greek]) + "\n" + " ".join([str(p) for p in self.english])

def read_groups():
    with open("groups.txt", encoding="utf8") as f:
        lines = f.readlines()
        new_group = True
        group = ""
        for line in [l.strip() for l in lines]:
            if new_group:
                group = line
                groups[group] = []
                new_group = False
            elif not line:
                new_group = True
            else:
                if line[0] == "*":
                    groups[group].append(parse_sentence(line[1:]))
                else:
                    groups[group].append(line)
            

def read_sentences():
    with open("sentences.txt", encoding="utf8") as f:
        lines = f.readlines()
        for line in [l.strip() for l in lines]:
            if not line or line[0] == "#":
                continue
            sentences.append(parse_sentence(line))
            

def read_forms():
    with open("forms.txt", encoding="utf8") as f:
        lines = f.readlines()
        new_pos = True
        pos = ""
        for line in [l.strip() for l in lines]:
            if not line or line[0] == "#":
                continue
            if new_pos:
                pos = line
                words[pos] = {}
                new_pos = False
            else:
                parts = line.split(" ")
                baseword = parts[0]
                word = parts[1]
                translation = parts[2]
                parts = parts[3:]
                current_dict = words[pos]
                while parts:
                    if parts[0] not in current_dict:
                        current_dict[parts[0]] = {}
                    current_dict = current_dict[parts[0]]
                    del parts[0]
                current_dict[baseword] = (word, translation)
    print(words)

def parse_sentence(s):
    greek, english = s.split("\t")

    greek_parts = re.findall(r'\[.*?\]', greek)
    for group in greek_parts:
        greek = greek.replace(group, "*")
    greek = greek.split("*")
    if len(greek) > 1:
        for i in range(len(greek)-1, 0, -1):
            greek.insert(i, parse_greek_sentence_part(greek_parts[i-1]))
    greek = list(filter(('').__ne__, greek))

    sentence = Sentence(greek, english)
    # sentence.generate()
    # print(sentence)
    return sentence

def parse_greek_sentence_part(part):
    part = part[1:-1].split(' ')
    baseword = None
    group = None
    if part[0] in groups:
        group = part[0]
    else:
        baseword = part[0]
    pos = part[1]
    case=None
    number=None
    tense=None
    mood=None
    voice=None
    person=None
    gender=None
    for p in part[2:]:
        if p in ['V', 'N', 'G', 'D', 'A'] or p[0] == 'c':
            case = p
        elif p in ['S', 'P'] or p[0] == 'n':
            number = p
        elif p in ['PRES'] or p[0] == 't':
            tense = p
        elif p in ['IND', 'INF', 'IMP', 'PAR'] or p[0] == 'm':
            mood = p
        elif p in ['C', 'L', 'I'] or p[0] == 'v':
            voice = p
        elif p in ['1', '2', '3'] or p[0] == 'p':
            person = p
        elif p in ['M', 'F', 'E'] or p[0] == 'g':
            gender = p
    return GreekSentencePart(baseword, group, pos, case, number, tense, mood, voice, person, gender)

def read_all():
    read_groups()
    read_sentences()
    read_forms()