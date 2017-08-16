import re

f = open('example.html')
html = f.read()

pattern_tag_base = r'<{tag}.*?>\s*([.\w\W]*?)\s*</{tag}>'
pattern_tag_content = r'^<.*?>([.\w\W]*?)</.*?>$'


def find_tag(tag, source):
    pattern = re.compile(pattern_tag_base.format(tag=tag))
    m_list = re.finditer(pattern, source)
    if m_list:
        return_list = [m.group() for m in m_list]
        return return_list if len(return_list) > 1 else return_list[0]
    return None


def get_tag_content(tag_string):
    pattern = re.compile(pattern_tag_content)
    m = re.search(pattern, tag_string.strip())
    if m:
        return m.group(1)
    return None


div = find_tag('div', html)
print(div)

p = find_tag('p', div)
print(p)

pattern_div = re.compile(r'<div.*?>([.\w\W]*?)</div>')
m = re.search(pattern_div, html)
div = m.group(1)

pattern_p = re.compile(r'<p.*?>([.\w\W]*?)</p>')
m_list = re.finditer(pattern_p, div)
