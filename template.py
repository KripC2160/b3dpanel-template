
import bpy

class Panel(bpy.types.Panel): #replace the class name 

    #Replace names and ids with desired ones
    bl_label = "Panel Template"
    bl_idname = "pTemp"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Template"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tools

classes = ( #add the classes here
    Panel, 
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
if __name__ == "__main__":
    register() 
