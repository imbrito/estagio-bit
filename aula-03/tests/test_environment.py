#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from environment import read_file, write_database_file
import os

class EnvironmentSpec(TestCase):

    def test_it_get_environment(self):
        self.assertEqual("postgresql", os.environ.get("TEST_ADAPTER"))
        self.assertEqual("unicode", os.environ.get("TEST_ENCODING"))
        self.assertEqual("estagio_bit", os.environ.get("TEST_DATABASE"))
        self.assertEqual("5", os.environ.get("TEST_POOL"))
        self.assertEqual("root", os.environ.get("TEST_USERNAME"))
        self.assertEqual("toor", os.environ.get("TEST_PASSWORD"))
        self.assertEqual("5432", os.environ.get("TEST_PORT"))
        self.assertEqual("127.0.0.1", os.environ.get("TEST_HOST"))

    def test_it_docker_compose_file(self, data = read_file("conf/docker-compose.yml")):
        self.assertTrue(isinstance(data, dict))
        self.assertEqual("3", data["version"] )
        self.assertEqual(["db", "elasticsearch", "web"], sorted(list(data["services"].keys())) )
        self.assertEqual(["image", "volumes"], sorted(list(data["services"]["db"].keys())) )
        self.assertEqual("postgres", data["services"]["db"]["image"] )
        self.assertEqual(["./tmp/db:/var/lib/postgresql/data"], data["services"]["db"]["volumes"] )
        self.assertEqual(["depends_on", "image", "ports"], sorted(list(data["services"]["elasticsearch"].keys())) )
        self.assertEqual(["db"], data["services"]["elasticsearch"]["depends_on"] )
        self.assertEqual("elasticsearch:latest", data["services"]["elasticsearch"]["image"] )
        self.assertEqual(["9201:9200"], data["services"]["elasticsearch"]["ports"] )
        self.assertEqual(["build", "command", "depends_on", "ports", "volumes"], sorted(list(data["services"]["web"].keys())) )
        self.assertEqual(".", data["services"]["web"]["build"] )
        self.assertEqual("bundle exec rails s -p 3000 -b '0.0.0.0'", data["services"]["web"]["command"] )
        self.assertEqual(["db"], data["services"]["web"]["depends_on"] )
        self.assertEqual(["3001:3000"], data["services"]["web"]["ports"] )
        self.assertEqual([".:/b2w"], data["services"]["web"]["volumes"] )

    def test_it_elasticsearch_file(self, data = read_file("conf/elasticsearch.json")):
        self.assertTrue(isinstance(data, dict))
        self.assertEqual("My First Node", data.get("name") )
        self.assertEqual("mycluster1", data.get("cluster_name") )
        self.assertEqual("As0vDWeAQ7utvTejnuxDPg", data.get("cluster_uuid") )
        self.assertEqual("6.2.4", data.get("version").get("number") )
        self.assertEqual("ccec39f", data.get("version").get("build_hash") )
        self.assertEqual("2018-04-12T20:37:28.497551Z", data.get("version").get("build_date") )
        self.assertFalse( data.get("version").get("build_snapshot") )
        self.assertEqual("7.2.1", data.get("version").get("lucene_version") )
        self.assertEqual("5.6.0", data.get("version").get("minimum_wire_compatibility_version") )
        self.assertEqual("5.0.0", data.get("version").get("minimum_index_compatibility_version") )
        self.assertEqual("You Know, for Search", data.get("tagline") )

    def test_it_write_database_file(self):
        """
            O desafio é escrever os arquivos database.yml e database.json na pasta conf, os arquivos representam a configuração de 
            um database, e por isso devem ser capazes de ter uma distinção entre cada um dos environments. 
            Os arquivos devem servir para 3 (três) environments distintos, que são: test, development e production.
            
                1) adequar o método write_database_file, para atender a criação de 3 (três) environments;
                2) o atributo database, deverá ser escrito, concatenando a variável de ambiente correspondente e o environment;
                3) escrever 1 (um) único caso de teste, capaz de validar a escrita de ambos os arquivos;
        """
        for end in [".yml",".json"]:
            write_database_file("conf/database{}".format(end))
            self.assertTrue(isinstance(read_file("conf/database{}".format(end)), dict))
        