import anytree
from anytree import Node, RenderTree
from anytree.exporter import DotExporter

data = ["abc", "abd", "aec", "add", "adcf"]

nodes = {}
first_node = None

for elem in data:
    parent_node = None
    parent_node_name = ""
    for i, val in enumerate(elem):
        if i not in nodes:
            nodes[i] = {}
        key = parent_node_name + val
        if key not in nodes[i]:
            print("Creating new node for ", key)
            nodes[i][key] = Node(key, parent=parent_node, display_name=val)

        if first_node is None:
            first_node = nodes[i][key]
        parent_node = nodes[i][key]
        parent_node_name = val

print(nodes)
DotExporter(nodes[0]["a"],
            nodeattrfunc=lambda node: 'label="{}"'.format(node.display_name)).to_dotfile("./graph.dot")