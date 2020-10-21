#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Cristina Tur -*-

import re

with open('plat.tet45_gk.xml', 'r') as file:
    content = file.read()

content=re.sub(r'(<text n=")(.+\.?)(">)', r'\$ \2\n', content)
#content=re.sub(r'<text>', r'\$', content)
content=re.sub(r'(<div1 type="book" n=")(\d+)("/?>)', r'\2\n', content)
content=re.sub(r'(\d+)a', r'\1_1',content)
content=re.sub(r'(\d+)b', r'\1_2',content)
content=re.sub(r'(\d+)c', r'\1_3',content)
content=re.sub(r'(\d+)d', r'\1_4',content)
content=re.sub(r'(\d+)e', r'\1_5',content)
content=re.sub(r'(\d+)f', r'\1_6',content)
content=re.sub(r'(<milestone unit="section" n=")(\d+_\d)("/?>)', r'\2\n', content)

content=re.sub(r'<bibl\s?n?=?"?\w*\.?\s?\w*\.?\s?\d*\.?\d*"?>\w*\.?\w*\s?\w*\.?\s?\d*\.?\d*<?/?b?i?b?l?>?', r'', content)
content=re.sub(r'<.?/?\w+\.?.?/?>', r' ', content)
content=re.sub(r'(<\w+)(\s\w+="\w+\s?(\w+)?")*(/?>)', r'', content)
content=re.sub(r'<\w+ \w+="\w+"\s\w+="\d+"/>', r'', content)
content=re.sub(r'&mdash;', r'―', content)
content=re.sub(r'&rdquo;', r'»', content)
content=re.sub(r'&ldquo;', r'«', content)
content=re.sub(r'&dagger;', r'\+', content)
content=re.sub(r'&.+;', r'', content)
content=re.sub(r';', r';', content)
content=re.sub(r':', r'·', content)

content = re.sub(r'\*a\)/\|', r'ᾌ', content)
content = re.sub(r'\*a\)\\\|', r'ᾊ', content)
content = re.sub(r'\*a\)=\|', r'ᾎ', content)
content = re.sub(r'\*h\)/\|', r'ᾜ', content)
content = re.sub(r'\*h\)\\\|', r'ᾚ', content)
content = re.sub(r'\*h\)=\|', r'ᾞ', content)
content = re.sub(r'\*w\)/\|', r'ᾬ', content)
content = re.sub(r'\*w\)\\\|', r'ᾪ', content)
content = re.sub(r'\*w\)=\|', r'ᾮ', content)
content = re.sub(r'\*a\(/\|', r'ᾍ', content)
content = re.sub(r'\*a\(\\\|', r'ᾋ', content)
content = re.sub(r'\*a\(=\|', r'ᾏ', content)
content = re.sub(r'\*h\(/\|', r'ᾝ', content)
content = re.sub(r'\*h\(\\\|', r'ᾛ', content)
content = re.sub(r'\*h\(=\|', r'ᾟ', content)
content = re.sub(r'\*w\(/\|', r'ᾭ', content)
content = re.sub(r'\*w\\\(\|', r'ᾫ', content)
content = re.sub(r'\*w=\(\|', r'ᾯ', content)
content = re.sub(r'a\)/\|', r'ᾄ', content)
content = re.sub(r'a\)\\\|', r'ᾂ', content)
content = re.sub(r'a\)=\|', r'ᾆ', content)
content = re.sub(r'h\)/\|', r'ᾔ', content)
content = re.sub(r'h\)\\\|', r'ᾒ', content)
content = re.sub(r'h\)=\|', r'ᾖ', content)
content = re.sub(r'w\)/\|', r'ᾤ', content)
content = re.sub(r'w\)\\\|', r'ᾢ', content)
content = re.sub(r'w\)=\|', r'ᾦ', content)
content = re.sub(r'a\(/\|', r'ᾅ', content)
content = re.sub(r'a\(\\\|', r'ᾃ', content)
content = re.sub(r'a\(=\|', r'ᾇ', content)
content = re.sub(r'h\(/\|', r'ᾕ', content)
content = re.sub(r'h\(\\\|', r'ᾓ', content)
content = re.sub(r'h\(=\|', r'ᾗ', content)
content = re.sub(r'w\(/\||w\(/\|', r'ᾥ', content)
content = re.sub(r'w\\\(\||w\(\\\|', r'ᾣ', content)
content = re.sub(r'w=\(\||w\(=\|', r'ᾧ', content)
content = re.sub(r'\*a\)/|\*\)/a', r'Ἄ', content)
content = re.sub(r'\*a\)\\|\*\)\\a', r'Ἂ', content)
content = re.sub(r'\*a\)=|\*\)=', r'Ἆ', content)
content = re.sub(r'\*e\)/|\*\)/e', r'Ἔ', content)
content = re.sub(r'\*e\)\\|\*\)\\e', r'Ἒ', content)
content = re.sub(r'\*h\)/|\*\)/h', r'Ἤ', content)
content = re.sub(r'\*h\)\\|\*\)\\h', r'Ἢ', content)
content = re.sub(r'\*h\)=|\*\)=h', r'Ἦ', content)
content = re.sub(r'\*i\)/|\*\)/i', r'Ἴ', content)
content = re.sub(r'\*i\)\\|\*\)\\i', r'Ἲ', content)
content = re.sub(r'\*i\)=|\*\)=i', r'Ἶ', content)
content = re.sub(r'\*o\)/|\*\)/0', r'Ὄ', content)
content = re.sub(r'\*o\)\\|\*\)\\o', r'Ὂ', content)
content = re.sub(r'\*w\)/|\*\)/w', r'Ὤ', content)
content = re.sub(r'\*w\)\\|\*\)\\w', r'Ὤ', content)
content = re.sub(r'\*w\)=|\*\)=w', r'Ὦ', content)
content = re.sub(r'\*a\(/|\*\(/a', r'Ἅ', content)
content = re.sub(r'\*a\(\\|\*\(\\a', r'Ἃ', content)
content = re.sub(r'\*a\(=|\*\(=a', r'Ἇ', content)
content = re.sub(r'\*e\(/|\*\(/e', r'Ἕ', content)
content = re.sub(r'\*e\(\\|\*\(\\e', r'Ἓ', content)
content = re.sub(r'\*h\(/|\*\(/h', r'Ἥ', content)
content = re.sub(r'\*h\(\\|\*\(\\h', r'Ἣ', content)
content = re.sub(r'\*h\(=|\*\(=h', r'Ἧ', content)
content = re.sub(r'\*i\(/|\*\(/i', r'Ἵ', content)
content = re.sub(r'\*i\(\\|\*\(\\i', r'Ἳ', content)
content = re.sub(r'\*i\(=|\*\(=i', r'Ἷ', content)
content = re.sub(r'\*o\(/|\*\(/o', r'Ὅ', content)
content = re.sub(r'\*o\(\\|\*\(\\o', r'Ὃ', content)
content = re.sub(r'\*u\(/|\*\(/u', r'Ὕ', content)
content = re.sub(r'\*u\(\\|\*\(\\u', r'Ὓ', content)
content = re.sub(r'\*u\(=|\*\(=u', r'Ὗ', content)
content = re.sub(r'\*w\(/|\*\(/w', r'Ὥ', content)
content = re.sub(r'\*w\\\(|\*\(\\w', r'Ὣ', content)
content = re.sub(r'\*w=\(|\*\(=w', r'Ὧ', content)
content = re.sub(r'\*a\)\||\*\)\|a', r'ᾈ', content)
content = re.sub(r'\*h\)\|', r'ᾘ', content)
content = re.sub(r'\*w\)\|', r'ᾠ', content)
content = re.sub(r'\*a\(\|', r'ᾉ', content)
content = re.sub(r'\*h\(\|', r'ᾙ', content)
content = re.sub(r'\*w\(\|', r'ᾩ', content)
content = re.sub(r'\*a\|', r'ᾼ', content)
content = re.sub(r'\*h\|', r'ῌ', content)
content = re.sub(r'\*w\|', r'ῼ', content)
content = re.sub(r'a/\|', r'ᾴ', content)
content = re.sub(r'a\\\|', r'ᾲ', content)
content = re.sub(r'a=\|', r'ᾷ', content)
content = re.sub(r'h/\|', r'ῄ', content)
content = re.sub(r'h\\\|', r'ῂ', content)
content = re.sub(r'h=\|', r'ῇ', content)
content = re.sub(r'w/\|', r'ῴ', content)
content = re.sub(r'w\\\|', r'ῲ', content)
content = re.sub(r'w=\|', r'ῷ', content)
content = re.sub(r'\*a/|\*/a', r'Ά', content)
content = re.sub(r'\*a\\\*\\a', r'Ὰ', content)
content = re.sub(r'\*e/|\*/e', r'Έ', content)
content = re.sub(r'\*e\\|\*\\e', r'Ὲ', content)
content = re.sub(r'\*h/|\*/h', r'Ή', content)
content = re.sub(r'\*h\\|\*\\h', r'Ὴ', content)
content = re.sub(r'\*i/|\*/i', r'Ί', content)
content = re.sub(r'\*i\\|\*\\i', r'Ὶ', content)
content = re.sub(r'\*o/|\*/o', r'Ό', content)
content = re.sub(r'\*o\\|\*\\o', r'Ὸ', content)
content = re.sub(r'\*u/|\*/u', r'Ύ', content)
content = re.sub(r'\*u\\|\*\\u', r'Ὺ', content)
content = re.sub(r'\*w/|\*/w', r'Ώ', content)
content = re.sub(r'\*w\\|\*\\w', r'Ὼ', content)
content = re.sub(r'\*a\)|\*\)a', r'Ἀ', content)
content = re.sub(r'\*\)e|\*e\)', r'Ἐ', content)
content = re.sub(r'\*h\)|\*\)h', r'Ἠ', content)
content = re.sub(r'\*i\)|\*\)i', r'Ἰ', content)
content = re.sub(r'\*o\)|\*\)o', r'Ὀ', content)
content = re.sub(r'\*w\)|\*\)w', r'Ὠ', content)
content = re.sub(r'\*a\(|\*\(a', r'Ἁ', content)
content = re.sub(r'\*e\(|\*\(e', r'Ἑ', content)
content = re.sub(r'\*h\(|\*\(h', r'Ἡ', content)
content = re.sub(r'\*i\(|\*\(i', r'Ἱ', content)
content = re.sub(r'\*o\(|\*\(o', r'Ὁ', content)
content = re.sub(r'\*u\(|\*\(u', r'Ὑ', content)
content = re.sub(r'\*w\(|\*\(w', r'Ὡ', content)
content = re.sub(r'\*r\(|\*\(r', r'Ῥ', content)
content = re.sub(r'a\)/', r'ἄ', content)
content = re.sub(r'a\)\\', r'ἂ', content)
content = re.sub(r'a\)=', r'ἆ', content)
content = re.sub(r'e\)/', r'ἔ', content)
content = re.sub(r'e\)\\', r'ἒ', content)
content = re.sub(r'h\)/', r'ἤ', content)
content = re.sub(r'h\)\\', r'ἢ', content)
content = re.sub(r'h\)=', r'ἦ', content)
content = re.sub(r'i\)/', r'ἴ', content)
content = re.sub(r'i\)\\', r'ἲ', content)
content = re.sub(r'i\)=', r'ἶ', content)
content = re.sub(r'o\)/', r'ὄ', content)
content = re.sub(r'o\)\\', r'ὂ', content)
content = re.sub(r'u\)/', r'ὔ', content)
content = re.sub(r'u\)\\', r'ὒ', content)
content = re.sub(r'u\)=', r'ὖ', content)
content = re.sub(r'w\)/', r'ὤ', content)
content = re.sub(r'w\)\\', r'ὢ', content)
content = re.sub(r'w\)=', r'ὦ', content)
content = re.sub(r'a\(/', r'ἅ', content)
content = re.sub(r'a\(\\', r'ἃ', content)
content = re.sub(r'a\(=', r'ἇ', content)
content = re.sub(r'e\(/', r'ἕ', content)
content = re.sub(r'e\(\\', r'ἓ', content)
content = re.sub(r'h\(/', r'ἥ', content)
content = re.sub(r'h\(\\', r'ἣ', content)
content = re.sub(r'h\(=', r'ἧ', content)
content = re.sub(r'i\(/', r'ἵ', content)
content = re.sub(r'i\(\\', r'ἳ', content)
content = re.sub(r'i\(=', r'ἷ', content)
content = re.sub(r'o\(/', r'ὅ', content)
content = re.sub(r'o\(\\', r'ὃ', content)
content = re.sub(r'u\(/', r'ὕ', content)
content = re.sub(r'u\(\\', r'ὓ', content)
content = re.sub(r'u\(=', r'ὗ', content)
content = re.sub(r'w\(/', r'ὥ', content)
content = re.sub(r'w\\\(', r'ὣ', content)
content = re.sub(r'w=\(', r'ὧ', content)
content = re.sub(r'a\|', r'ᾳ', content)
content = re.sub(r'h\|', r'ῃ', content)
content = re.sub(r'w\|', r'ῳ', content)
content = re.sub(r'a\)', r'ἀ', content)
content = re.sub(r'e\)', r'ἐ', content)
content = re.sub(r'h\)', r'ἠ', content)
content = re.sub(r'i\)', r'ἰ', content)
content = re.sub(r'o\)', r'ὀ', content)
content = re.sub(r'u\)', r'ὐ', content)
content = re.sub(r'w\)', r'ὠ', content)
content = re.sub(r'a\(', r'ἁ', content)
content = re.sub(r'e\(', r'ἑ', content)
content = re.sub(r'h\(', r'ἡ', content)
content = re.sub(r'i\(', r'ἱ', content)
content = re.sub(r'o\(', r'ὁ', content)
content = re.sub(r'u\(', r'ὑ', content)
content = re.sub(r'w\(', r'ὡ', content)
content = re.sub(r'r\)', r'ῤ', content)
content = re.sub(r'r\(', r'ῥ', content)
content = re.sub(r'a/', r'ά', content)
content = re.sub(r'a\\', r'ὰ', content)
content = re.sub(r'a=', r'ᾶ', content)
content = re.sub(r'e/', r'έ', content)
content = re.sub(r'e\\', r'ὲ', content)
content = re.sub(r'h/', r'ή', content)
content = re.sub(r'h\\', r'ὴ', content)
content = re.sub(r'h=', r'ῆ', content)
content = re.sub(r'i/', r'ί', content)
content = re.sub(r'i\\', r'ὶ', content)
content = re.sub(r'i=', r'ῖ', content)
content = re.sub(r'o/', r'ό', content)
content = re.sub(r'o\\', r'ὸ', content)
content = re.sub(r'u/', r'ύ', content)
content = re.sub(r'u\\', r'ὺ', content)
content = re.sub(r'u=', r'ῦ', content)
content = re.sub(r'w/', r'ώ', content)
content = re.sub(r'w\\', r'ὼ', content)
content = re.sub(r'w=', r'ῶ', content)
content = re.sub(r'\*a', r'Α', content)
content = re.sub(r'\*b', r'Β', content)
content = re.sub(r'\*c', r'Ξ', content)
content = re.sub(r'\*d', r'Δ', content)
content = re.sub(r'\*e', r'Ε', content)
content = re.sub(r'\*f', r'Φ', content)
content = re.sub(r'\*g', r'Γ', content)
content = re.sub(r'\*h', r'Η', content)
content = re.sub(r'\*i', r'Ι', content)
content = re.sub(r'\*k', r'Κ', content)
content = re.sub(r'\*l', r'Λ', content)
content = re.sub(r'\*m', r'Μ', content)
content = re.sub(r'\*n', r'Ν', content)
content = re.sub(r'\*o', r'Ο', content)
content = re.sub(r'\*p', r'Π', content)
content = re.sub(r'\*q', r'Θ', content)
content = re.sub(r'\*r', r'Ρ', content)
content = re.sub(r'\*s', r'Σ', content)
content = re.sub(r'\*t', r'Τ', content)
content = re.sub(r'\*u', r'Υ', content)
content = re.sub(r'\*w', r'Ω', content)
content = re.sub(r'\*x', r'Χ', content)
content = re.sub(r'\*y', r'Ψ', content)
content = re.sub(r'\*z', r'Ζ', content)
content = re.sub(r'a', r'α', content)
content = re.sub(r'b', r'β', content)
content = re.sub(r'c', r'ξ', content)
content = re.sub(r'd', r'δ', content)
content = re.sub(r'e', r'ε', content)
content = re.sub(r'f', r'φ', content)
content = re.sub(r'g', r'γ', content)
content = re.sub(r'h', r'η', content)
content = re.sub(r'i', r'ι', content)
content = re.sub(r'k', r'κ', content)
content = re.sub(r'l', r'λ', content)
content = re.sub(r'm', r'μ', content)
content = re.sub(r'n', r'ν', content)
content = re.sub(r'o', r'ο', content)
content = re.sub(r'p', r'π', content)
content = re.sub(r'q', r'θ', content)
content = re.sub(r'r', r'ρ', content)
content = re.sub(r's', r'σ', content)
content = re.sub(r't', r'τ', content)
content = re.sub(r'u', r'υ', content)
content = re.sub(r'w', r'ω', content)
content = re.sub(r'x', r'χ', content)
content = re.sub(r'y', r'ψ', content)
content = re.sub(r'z', r'ζ', content)

content=re.sub(r's', r'σ', content)
content=re.sub(r'σ(\s|\n|\,|\.|;|·)', r'ς\1', content)
content=re.sub(r'(\d)_1', r'\1a', content)
content=re.sub(r'(\d)_2', r'\1b', content)
content=re.sub(r'(\d)_3', r'\1c', content)
content=re.sub(r'(\d)_4', r'\1d', content)
content=re.sub(r'(\d)_5', r'\1e', content)
content=re.sub(r'(\d)_6', r'\1f', content)

works=re.split('\$', content, maxsplit=8)

work1=works[1]
work2=works[2]
work3=works[3]
work4=works[4]
work5=works[5]
work6=works[6]
work7=works[7]
work8=works[8]

final_file1 = open('Plato_Alcib1.xml', 'w')
final_file1.write(work1)
final_file1.close()

final_file2 = open('Plato_Alcib2.xml', 'w')
final_file2.write(work2)
final_file2.close()

final_file3 = open('Plato_Hipparchus.xml', 'w')
final_file3.write(work3)
final_file3.close()

final_file4 = open('Plato_Lovers.xml', 'w')
final_file4.write(work4)
final_file4.close()

final_file5 = open('Plato_Theag.xml', 'w')
final_file5.write(work5)
final_file5.close()

final_file6 = open('Plato_Charm.xml', 'w')
final_file6.write(work6)
final_file6.close()

final_file7 = open('Plato_Laches.xml', 'w')
final_file7.write(work7)
final_file7.close()

final_file8 = open('Plato_Lys.xml', 'w')
final_file8.write(work8)
final_file8.close()