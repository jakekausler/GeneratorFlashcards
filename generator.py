import re
import random

groups = {}
sentences = []

def generate_noun(word):
    pass

def generate_verb(word):
    pass

def generate_adjective(word):
    pass

def generate_pronoun(word):
    pass

def generate_phrase(phrase):
    pass

def stringify_noun(word):
    return word.baseword if word.baseword else word.group

def stringify_verb(word):
    return word.baseword if word.baseword else word.group

def stringify_adjective(word):
    return word.baseword if word.baseword else word.group

def stringify_pronoun(word):
    return word.baseword if word.baseword else word.group

def stringify_phrase(phrase):
    return phrase.baseword if phrase.baseword else phrase.group

generators = {
    'NN': generate_noun,
    'VB': generate_verb,
    'AJ': generate_adjective,
    'PN': generate_pronoun,
    'PE': generate_phrase,
}

stringifiers = {
    'NN': stringify_noun,
    'VB': stringify_verb,
    'AJ': stringify_adjective,
    'PN': stringify_pronoun,
    'PE': stringify_phrase,
}

class BaseWord:
    def __init__(self):
        self.word = None
    
    def generate(self, group):
        self.word = random.choice(groups[group])

class GreekSentencePart:
    def __init__(self, baseword=None, group=None, pos=None, case=None, number=None, tense=None, mood=None, person=None, gender=None):
        self.baseword = baseword
        self.pos = pos
        self.group = group
        self.case = case
        self.number = number
        self.tense = tense
        self.mood = mood
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
    
    def __str__(self):
        return " ".join(str(self.greek)) + "\n" + " ".join(str(self.english))

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
    print(''.join([str(g) for g in greek]))

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
    person=None
    gender=None
    for p in part[2:]:
        if p in ['V', 'N', 'G', 'D', 'A'] or p[0] == 'c':
            case = p
        elif p in ['S', 'P'] or p[0] == 'n':
            number = p
        elif p in ['PRES'] or p[0] == 't':
            tense = p
        elif p in ['IND', 'INF', 'IMP'] or p[0] == 'm':
            mood = p
        elif p in ['1', '2', '3'] or p[0] == 'p':
            person = p
        elif p in ['M', 'F', 'E'] or p[0] == 'g':
            gender = p
    return GreekSentencePart(baseword, group, pos, case, number, tense, mood, person, gender)

def read_all():
    read_groups()
    read_sentences()