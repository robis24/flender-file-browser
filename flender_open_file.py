import bpy
import os

def mainnew(context):
    
    start_areas = context.screen.areas[:]
    bpy.ops.screen.area_split(direction='VERTICAL', factor=0.5)
    for area in context.screen.areas:
        if area not in start_areas:
            area.type = 'FILE_BROWSER'
            bpy.ops.file.bookmark_toggle()

def main(context):

    
    
    
    selectedFile = ''
    
        
    params = bpy.context.area.spaces[0].params
    selectedFile = os.path.join(params.directory, params.filename)
   



#    bpy.ops.image.external_edit(filepath=selectedFile)
    os.system("xdg-open "+selectedFile)


class OpenInNewArea(bpy.types.Operator):
    bl_idname = "screen.openinnew_area"
    bl_label = "Open in new area"
    
            
    def execute(self, context):
        mainnew(context)
        return {'FINISHED'}        
                
    



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
    bpy.utils.register_class(OpenInNewArea)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="File Browser", space_type="FILE_BROWSER")
        kmi = km.keymap_items.new('object.open_file', 'LEFTMOUSE', 'DOUBLE_CLICK')
        kml = kc.keymaps.new(name="File Browser", space_type="FILE_BROWSER")
        kmil = kml.keymap_items.new('screen.openinnew_area', 'O', 'PRESS')

def unregister():
    bpy.utils.unregister_class(OpenFile)
    bpy.utils.unregister_class(OpenInNewArea)
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps["FILE_BROWSER"]
        for kmi in km.keymap_items:
            if kmi.idname == 'object.open_file':
                km.keymap_items.remove(kmi)
                
                
                

if __name__ == "__main__":
    register()

