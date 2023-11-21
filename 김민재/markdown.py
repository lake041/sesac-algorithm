import re

html_string = """

"""

urls = re.findall(r'href="([^"]*)"', html_string)
urls = ['https://school.programmers.co.kr' + url for url in urls]
titles = re.findall(r'<a[^>]*>([^<]*)</a><small', html_string)
subtitles = re.findall(r'<small\s+class="part-title">([^<]+)</small>', html_string)
levels = re.findall(r'<span[^>]*>([^<]*)</span>', html_string)
counts = re.findall(r'<td class="finished-count">(\d+,?\d*명)</td>', html_string)
rates = re.findall(r'<td[^>]*class="acceptance-rate"[^>]*>([^<]*)</td>', html_string)

table = "| 제목 | | 난이도 | 완료한 사람 | 정답률 |\n| --- | --- | --- | --- | --- |\n"
for url, title, subtitle, level, count, rate in zip(urls, titles, subtitles, levels, counts, rates):
    if subtitle == "연습문제":
        subtitle = ""
    table += f"| [{title}]({url}) | {subtitle} | {level} | {count} | {rate} |\n"

print(table)