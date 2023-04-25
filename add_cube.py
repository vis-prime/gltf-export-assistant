import bpy


class AddCubeOperator(bpy.types.Operator):
    bl_idname = "object.add_cube_operator"
    bl_label = "Add Cube"

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(AddCubeOperator)


def unregister():
    bpy.utils.unregister_class(AddCubeOperator)
