import json
import yaml

file = open("./input.yml", "r")

line_input = yaml.load(file, Loader=yaml.Loader)

icon_data = {}
lines = []
for line in line_input:
    if (line['hex'] not in icon_data):
        icon_data[line['hex']] = { 'id': len(icon_data) + 1, 'hex': line['hex'] }
    lines.append({
        'id': line['id'],
        'icon': icon_data[line['hex']]['id']
    })

icons = list(icon_data.values())

lines_file = open("./lines.json", "w")
icons_file = open("./icons.json", "w")

lines_file.write(json.dumps(lines, indent=2))
icons_file.write(json.dumps(icons, indent=2))
