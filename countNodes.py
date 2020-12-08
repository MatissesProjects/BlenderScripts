import bpy

def countMaterialNodes(material, total_nodes=0):
    next_depth_materials = []
    if material.name == 'Dots Stroke':
        return 0, next_depth_materials
    all_nodes = material.node_tree.nodes
    
    # if we need to remove other nodes in the future reenable this bit for their exact name
#    for node in all_nodes:
#        print(node.name)
    
    filtered_nodes = list(filter(lambda x: "Reroute" not in x.name, all_nodes))
    filtered_nodes = list(filter(lambda x: "Frame" not in x.name, filtered_nodes))
    total_nodes += len(list(filtered_nodes))
    
    for layer_node in filtered_nodes:
        if 'node_tree' in dir(layer_node):
            next_depth_materials.append(layer_node)
    return total_nodes, next_depth_materials

def countAllMaterials(allMaterials):
    # want to create a breadth first search
    for material in allMaterials:
        # current layer, get count, and get other layers
        total_nodes, next_depth_materials = countMaterialNodes(material)
        # start next layers searches
        for layerMaterial in next_depth_materials:
#            print(layerMaterial)
            nextLayerNodes, newMaterials = countMaterialNodes(layerMaterial)
#            print(f'{layerMaterial.name}, {nextLayerNodes}')
            total_nodes += nextLayerNodes
            next_depth_materials += newMaterials
        print(f'for {material.name} the total nodes used are {total_nodes}')

countAllMaterials(bpy.data.materials)
print('done')
