import bpy

from bpy.types import Panel

import humanize
import PIL


class HelloWorldPanel(Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text=f"humanize version {humanize.__version__}")
        row.label(text=f"humanize file {humanize.__file__}")

        row = layout.row()
        row.label(text=f"PIL version {PIL.__version__}")
        row.label(text=f"PIL file {PIL.__file__}")


def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()
