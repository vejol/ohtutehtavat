from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = toml.loads(content)['tool']['poetry']
        print(toml_dict, '\n')
        name = toml_dict['name']
        description = toml_dict['description']
        license = toml_dict['license']
        authors = toml_dict['authors']
        dependencies = toml_dict['dependencies'].keys()
        dev_dependencies = toml_dict['group']['dev']['dependencies'].keys()


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
