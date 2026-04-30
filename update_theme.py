import re

with open('Index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'bg-[#0a0a0a]': 'bg-white',
    'text-white': 'text-gray-900',
    'text-gray-100': 'text-gray-900',
    'text-gray-400': 'text-gray-500',
    'text-gray-300': 'text-gray-600',
    'border-white/10': 'border-gray-200',
    'border-white/20': 'border-gray-200',
    'border-white/5': 'border-gray-100',
    'bg-white/5': 'bg-gray-50',
    'bg-white/10': 'bg-gray-100',
    'hover:bg-white/5': 'hover:bg-gray-50',
    'hover:bg-white/10': 'hover:bg-gray-100',
    'hover:text-white': 'hover:text-gray-900',
    'bg-white/20': 'bg-gray-200',
    'text-siemens-orange/80': 'text-gray-600',
    'text-siemens-orange/70': 'text-siemens-teal',
    'from-siemens-dark to-[#0f0f23]': 'from-teal-50 to-white',
    'bg-gradient-to-t from-siemens-dark/80': 'bg-gradient-to-t from-white/80',
    'from-white/5 to-white/10': 'from-gray-50 to-gray-100',
    'placeholder-gray-500': 'placeholder-gray-400',
    'focus:text-white': 'focus:text-gray-900',
    'grid-bg-dark': 'grid-bg',
    'dna-container-dark': 'dna-container',
    'dna-glow-dark': 'dna-glow'
}

for old, new in replacements.items():
    content = content.replace(old, new)

content = content.replace('text-gray-900 font-bold text-xs">S', 'text-white font-bold text-xs">S')
content = content.replace('text-gray-900 font-bold text-xs">JD', 'text-white font-bold text-xs">JD')
content = content.replace('text-gray-900 font-bold text-xs">MK', 'text-white font-bold text-xs">MK')
content = content.replace('text-gray-900 font-bold text-xs">AL', 'text-white font-bold text-xs">AL')
content = content.replace('text-gray-900 text-sm font-semibold rounded-full hover:shadow-lg', 'text-white text-sm font-semibold rounded-full hover:shadow-lg')
content = content.replace('text-gray-900 font-semibold rounded-full hover:shadow-xl', 'text-white font-semibold rounded-full hover:shadow-xl')
content = content.replace('text-gray-900 font-semibold rounded-xl hover:shadow-lg', 'text-white font-semibold rounded-xl hover:shadow-lg')
content = content.replace('text-gray-900 text-xs font-bold hover:bg-gray-100 transition-colors', 'text-gray-900 text-xs font-bold hover:bg-gray-100 transition-colors') # keep lang toggle

content = content.replace('id="clinical" class="relative py-24 bg-white', 'id="clinical" class="relative py-24 bg-teal-50')
content = content.replace('id="services" class="py-24 bg-white', 'id="services" class="py-24 bg-gray-50')
content = content.replace('id="contact" class="py-24 bg-white', 'id="contact" class="py-24 bg-gray-50')
content = content.replace('class="py-8 bg-white', 'class="py-8 bg-gray-50')
content = content.replace('<footer class="bg-white border-t border-gray-200 text-gray-500 py-16">', '<footer class="bg-gray-50 border-t border-gray-200 text-gray-500 py-16">')

content = content.replace('nav id="navbar"\n        class="fixed top-0 w-full z-50 transition-all duration-500 bg-white backdrop-blur-xl border-b border-gray-200"', 'nav id="navbar"\n        class="fixed top-0 w-full z-50 transition-all duration-500 bg-white/90 backdrop-blur-xl border-b border-gray-200"')

with open('Index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Theme updated")
