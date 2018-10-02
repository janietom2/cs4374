from JsonReader import *
import pprint
import re


def get_conf_file(conf_file):
    with open(conf_file) as data:
        conf = json.load(data)

    return conf


def search_files_in_repo(repo_name, token):
    github_api_text = "https://api.github.com/search/"
    #extensions = "extension:uml+extension:xml+extension:png+extension:bmp+extension:jpg+filename:uml+extension:js"
    search_repo = github_api_text+'code?access_token='+token+'&q=addClass+repo:'+repo_name
    projects = getJson(search_repo)
    files_found = []
    patterns = ['state machine', 'uml', 'diagram', 'use case']

    for x in range(len(projects['items'])):
        if projects['total_count'] == 0:
            continue
        else:
            for p in patterns:
                if re.search(p, projects['items'][x]['name']):
                    files_found.append(projects['items'][x]['name'] + " | in: " + projects['items'][x]['path'])

    return "Files not found" if len(files_found) == 0 else files_found


tkn = get_conf_file('confi.json')['config']['token']  # Config file load and get token

reps = ['google/mathfu', 'google/flatui', 'google/cameraview', 'google/blockly', 'google/flutter-desktop-embedding']

for repo in reps:
    files = search_files_in_repo(repo, tkn)
    pp = pprint.PrettyPrinter(indent=4)
    print(repo)
    pp.pprint(files)
    print("\n")




