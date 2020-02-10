from flask import Blueprint, request, jsonify
from xmldiff import main
from lxml import etree
from operator import attrgetter

comparison_xml = Blueprint("comparison_xml", __name__)

@comparison_xml.route('/')
def index():
    return {"data":"Comparison XML"}

@comparison_xml.route("/compare", methods = ["POST"])
def xml_comparison():

    data = []

    source = request.files['source']
    target = request.files['target']

    source_tree = etree.parse(source)
    target_tree = etree.parse(target)

    _sort_nodes(source_tree, target_tree)

    source_string = etree.tostring(source_tree)    
    target_string = etree.tostring(target_tree)

    result = main.diff_texts(source_string, target_string)

    for r in result:
        data.append(r)

    print(data)

    return jsonify(result = data)

def _sort_nodes(source, target):    
    for node in source.xpath('//*[./*]'):  # searching top-level nodes only: node1, node2 ...
        node[:] = sorted(node, key=attrgetter("tag")) # You can change the sort type to text, attribute

    for node in target.xpath('//*[./*]'):  # searching top-level nodes only: node1, node2 ...
        node[:] = sorted(node, key=attrgetter("tag"))# You can change the sort type to text, attribute
