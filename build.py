"""src/app.template.html + src/reference.css + vendor/xlsx.full.min.js -> index.html (단일 파일)"""
import pathlib
r = pathlib.Path(__file__).parent
t = (r / 'src/app.template.html').read_text(encoding='utf8')
t = t.replace('/*REFCSS*/', (r / 'src/reference.css').read_text(encoding='utf8'))
t = t.replace('<!--XLSX-->', '<script>' + (r / 'vendor/xlsx.full.min.js').read_text(encoding='utf8') + '</script>')
(r / 'index.html').write_text(t, encoding='utf8')
print('index.html', len(t))
