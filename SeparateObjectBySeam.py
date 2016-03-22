import bpy
import bmesh

obj = bpy.context.edit_object
me = obj.data
bm = bmesh.from_edit_mesh(me)

# notice in Bmesh polygons are called faces
bm.faces[4].select = True  # select index 4

# Show the updates in the viewport
bmesh.update_edit_mesh(me, True)

bpy.ops.mesh.select_linked(limit=True)
bpy.ops.mesh.separate()
