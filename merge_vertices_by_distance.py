bl_info = {
    "name": "Merge Vertices by Distance",
    "blender": (3, 0, 0),
    "category": "Mesh",
    "description": "Merges vertices by a specified distance",
    "author": "Glucka Voxels",
    "version": (1, 0),
}

import bpy


class MESH_OT_merge_vertices_by_distance(bpy.types.Operator):
    bl_idname = "mesh.merge_vertices_by_distance"
    bl_label = "Merge Vertices by Distance"
    bl_options = {'REGISTER', 'UNDO'}
    
    merge_distance: bpy.props.FloatProperty(
        name="Merge Distance",
        description="Distance within which vertices will be merged",
        default=0.01,
        min=0.0,
    )

    def execute(self, context):
        
        bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.mode_set(mode='EDIT')

        bpy.ops.mesh.select_all(action='SELECT')
       
        bpy.ops.mesh.remove_doubles(threshold=self.merge_distance)
      
        bpy.ops.object.mode_set(mode='OBJECT')

        self.report({'INFO'}, f"Vertices merged by distance: {self.merge_distance}")
        return {'FINISHED'}


class VIEW3D_PT_merge_vertices_panel(bpy.types.Panel):
    bl_label = "Merge Vertices by Distance"
    bl_idname = "VIEW3D_PT_merge_vertices_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.merge_vertices_by_distance")

def register():
    bpy.utils.register_class(MESH_OT_merge_vertices_by_distance)
    bpy.utils.register_class(VIEW3D_PT_merge_vertices_panel)

def unregister():
    bpy.utils.unregister_class(MESH_OT_merge_vertices_by_distance)
    bpy.utils.unregister_class(VIEW3D_PT_merge_vertices_panel)

if __name__ == "__main__":
    register()
