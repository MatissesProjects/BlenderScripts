import bpy
import numpy as np

x = [ True, False, False]
y = [ False, True, False]
z = [ False, False, True]

class SimpleMovementOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_movement_operator"
    bl_label = "Simple Object Movement Operator"

    def __init__(self):
        self.axisIndex = 0
        self.axes = [x, y, z]

    @classmethod
    def poll(cls, context):
        print(context.active_object)
        return context.active_object is not None
    
    def modal(self, context, event):
        
        # setup exiting the modal mode        
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            return {'CANCELLED'}

        # start next axis
        if event.type in {'E'}:
            bpy.ops.transform.translate(release_confirm=True)
            bpy.ops.transform.translate('INVOKE_DEFAULT', constraint_axis=self.axes[self.axisIndex])
#            bpy.ops.transform.translate('INVOKE_DEFAULT', constraint_axis=self.axes[self.axisIndex])
            self.axisIndex = (self.axisIndex + 1) % len(self.axes)
#            bpy.ops.transform.translate('INVOKE_DEFAULT', constraint_axis=self.axes[self.axisIndex], release_confirm=True)
        return {'PASS_THROUGH'}

    def execute(self, context):       
#        bpy.ops.transform.translate('INVOKE_DEFAULT', constraint_axis=self.axes[self.axisIndex], release_confirm=True)
#        bpy.ops.transform.translate('INVOKE_DEFAULT', constraint_axis=self.axes[self.axisIndex])
        
        # switch over to a modal handler for later added calls
        wm = context.window_manager
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}
     
def main(context):
    for ob in context.scene.objects:
        print(ob)
        
def register():
    bpy.utils.register_class(SimpleMovementOperator)


def unregister():
    bpy.utils.unregister_class(SimpleMovementOperator)

if __name__ == "__main__":
    register()
