import bpy
from bpy.app.handlers import persistent

@persistent
def load_handler_for_preferences(_):
    import bpy

    print("Changing Preference Defaults!")
    # from bpy import context
    #
    # prefs = context.preferences
    # prefs.use_preferences_save = False
    #
    # kc = context.window_manager.keyconfigs["blender"]
    # kc_prefs = kc.preferences
    # if kc_prefs is not None:
    #     kc_prefs.select_mouse = 'RIGHT'
    #     kc_prefs.spacebar_action = 'SEARCH'
    #     kc_prefs.use_pie_click_drag = True
    #
    # view = prefs.view
    # view.header_align = 'TOP'


@persistent
def load_handler_for_startup(_):
    import bpy
    import addon_utils
    print("Changing Startup Defaults!")

    # Use material preview shading.
    for screen in bpy.data.screens:
        for area in screen.areas:
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.type = 'SOLID'
                    space.shading.use_scene_lights = True

    #enable any addon by default with 
    #	addon_utils.enable("my_addon")
    #disable any addon by default with
    #	addon_utils.disable("my_addon")
    #
    #further settings can be made by initiating: 
    #	addon_utils.enable(module_name, default_set=False, persistent=False, handle_error=None)
    #
    #via https://blender.stackexchange.com/a/32420
    addon_utils.enable("io_rfactor2_gmt_WIP-64_bit")
    addon_utils.enable("jmesh-tools-master")

def register():
    print("Registering to Change Defaults")
    bpy.app.handlers.load_factory_preferences_post.append(load_handler_for_preferences)
    bpy.app.handlers.load_factory_startup_post.append(load_handler_for_startup)

def unregister():
    print("Unregistering to Change Defaults")
    bpy.app.handlers.load_factory_preferences_post.remove(load_handler_for_preferences)
    bpy.app.handlers.load_factory_startup_post.remove(load_handler_for_startup)
