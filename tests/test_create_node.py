from maya import cmds


def test_create_node(maya_scene):
    node = cmds.createNode("transform", name="node_1")
    assert cmds.nodeType(node) == "transform"
    assert node == "node_1"
