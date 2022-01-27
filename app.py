from jinja2 import Environment, FileSystemLoader
import json 
import argparse
from re import sub
import os

parser=argparse.ArgumentParser()

parser.add_argument('--lan', help='Language to Parse')
parser.add_argument('--out', help='Output directory name')

args = parser.parse_args()

if args.lan is None:
    args.lan = 'dart'

if args.out is None:
    args.out = 'out'

# print (args.lan)
# print(args.out)


env = Environment(loader=FileSystemLoader('templates'))
env.filters['type'] = type
template = env.get_template('flutter_class.j2')

def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])

def gen(jsonDATA, typeData):
    data = {}

    # Class name
    # print([*jsonDATA][0])
    className = [*jsonDATA][0]
    data['className'] = className

    data['items'] = []
    data['typeImports'] = []


    for item in jsonDATA[className]:
        if isinstance(jsonDATA[className][item], dict):
            gen({item: jsonDATA[className][item] }, typeData)
            t = camel_case(item).capitalize() if isinstance(item, str) else item
            data['items'].append({"val": camel_case(item), "type": t})
            data['typeImports'].append(item + '.' + args.lan)
        else:
            t = type(item)
            data['items'].append({"val": camel_case(item), "type": typeData[t.__name__]})

    output_from_parsed_template = template.render(data=data)
    # check if dir exist

    if not os.path.exists(args.out):
        os.mkdir(args.out)

    # # to save the results
    with open(args.out + "/" + className + ".dart", "w") as fh:
        fh.write(output_from_parsed_template)

# load json
f = open('match.json')
jsonDATA = json.load(f)

t = open('types/dart.json')
typeData = json.load(t)

gen(jsonDATA, typeData)