import bpy
import os

def main(context):

    
    
    
    selectedFile = ''
    for screenArea in bpy.context.window.screen.areas:
        if screenArea.type == 'FILE_BROWSER':
            params = screenArea.spaces[0].params
            selectedFile = os.path.join(params.directory, params.filename)
            print(selectedFile)
            break



#    bpy.ops.image.external_edit(filepath=selectedFile)
    os.system("xdg-open "+selectedFile)


class OpenFile(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.open_file"
    bl_label = "Open File"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(OpenFile)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="File Browser", space_type="FILE_BROWSER")
        kmi = km.keymap_items.new('object.open_file', 'O', 'PRESS')

def unregister():
    bpy.utils.unregister_class(OpenFile)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps["FILE_BROWSER"]
        for kmi in km.keymap_items:
            if kmi.idname == 'object.open_file':
                km.keymap_items.remove(kmi)
                break

if __name__ == "__main__":
    register()

