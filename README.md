# Blender rF2 Studio
__*Blender Application Templates for the rFactor2 Modder*__

## Introduction
Application Templates for Blender allow re-use of configuration and contents, which is perfect for those that often have the same workflow and don't want to fiddle in the menus first before being able to actually start working on their project.

Modding of PC games, especially racing simulations, is a hobby that often includes the same workflows and tasks.

These rF2 Studio Application Templates are made for the rFactor2 modders with their very own requirements. But these templates do work well for other purposes and can also be modified very easy to each individuals liking and requirements.

### rF2 Studio
This template was created as a generic starting point for all rFactor2 modding purposes and shares the following configuration with all child-templates.
- "Layout" is default workspace
  - 3D view from the default camera perspective
  - Viewport shading "Solid"
    - "Backface Culling" enabled
    - "Cavity" enabled
- Scene configuration
  - "Ambient Occlusion" enabled (with distance set to 10m)
  - "Bloom" enabled (with intensity set to 0.01)
  - "Screen Space Reflections" enabled
    - "Refraction" enabled
    - "Trace Precision" set to 1.0
  - "Volumetrics"
    - "Volumetric Shadows" enabled with samples set to 16
- Scene Collections
  - "Scene01", the default collection consisting of
    - "Cameras", the child-collection for cameras
      - includes a basic camera with "Depth of Field" enabled, focus on empty "Camera_DoF"
    - "Lighting", the child-collection for lights
      - includes a default pointlight
    - "Objects", the child-collection for objects
      - includes a default cube object
  - "MatLibrary", the default collection to organize your materials

Screenshot will be included here later.

### rF2 Studio - Car
This child-template was created with car modeling in mind. It includes additional settings, default objects, and default materials that should kickstart the car modeling process!
- Default Object
  - half cube with mirror modifier (incl. clipping) enabled
- "Modeling" workspace has "Quad View" enabled

Screenshot will be included here later.

### rF2 Studio - Track
This child-template was created with track modeling in mind. It includes additional settings, default objects, and default materials that should kickstart the track modeling process!

Current version is the same as the Car template. This will be updated soon!

Screenshot will be included here later.

## Installation
1. Download the template(s) (e.g. "rF2_Studio.zip") from the [releases](https://github.com/MrFuNK1/Blender-rF2-Studio/releases) 
2. Start Blender
3. Open the App Menu (small blender icon in the top left corner)
4. Click on "Install Application Template..."
5. Browse to the download location of the template(s) and select the template (e.g. "rF2_Studio.zip")
6. Confirm and you are ready to use the template(s)! 

![Installation Screenshot](/screenshots/installation.png)

## Using the rF2 Studio Application Templates

### Using a Desktop Shortcut

Create a new desktop shortcut to the Blender executable or copy an existing shortcut. Edit the shortcut's properties and add the following command line arguments after the blender executable.

#### Linux

`blender --app-template rF2_Studio`

`blender --app-template rF2_Studio_-_Car`

`blender --app-template rF2_Studio_-_Track`


#### Windows

`blender.exe --app-template rF2_Studio`

`blender.exe --app-template rF2_Studio_-_Car`

`blender.exe --app-template rF2_Studio_-_Track`

### Use from within Blender
You can use any application template directly from within Blender. The installed templates are available from the File > New menu.

![Usage Screenshot](/screenshots/usage.png)

### Troubleshooting
Installation is done to the following paths. Each template has to be saved in its own folder (e.g. "rF2 Studio"). Only then you do have the correct entries in the menu.

#### Linux

`~/.config/blender/2.91/scripts/startup/bl_app_templates_user`

#### Windows

`C:\Documents and Settings\%username%\Application Data\Blender Foundation\Blender\2.XX\scripts\startup\bl_app_templates_user`

## Suggested 3rd Party Addons
The following 3rd party addons are suggestions and recommendations to improve the modders life. In case you have already installed the mentioned 3rd party addons, these will be automatically activated (if installed) by the application templates.

Instructions on how to install addons in Blender can be found in the [official Blender manual](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html?highlight=addons#enabling-and-disabling).

### rFactor2 GMT Import Export
Obviously the Import Export addon for rFactor2 GMT files by Traveller is a must have for the rFactor2 modder! The latest info and a download link for the "io_rfactor2_gmt_WIP-64_bit" for Blender 2.80+ can be found in the forum thread on forum.studio-397.com [[WIP] - rFactor2 export scripts for Blender 2.80+ | Studio-397 Forum](https://forum.studio-397.com/index.php?threads/rfactor2-export-scripts-for-blender-2-80.68007/).

### JMesh Tools
This addon for Blender is a mesh and hard surface utilities addon. So it becomes very handy when creating various objects or assets.

Information, documentation, and of course the download is available from the [projects github page](https://github.com/jayanam/jmesh-tools).

## Other interesting 3rd Party Addons or Sources

### For Everyone
[Blenderkit](https://www.blenderkit.com/) - a resource for models, materials, and other things. They have a free plan, and the addon alows to use put them in your project with just a few clicks!

[Julio Sillet 3D Art](https://gumroad.com/juliosillet?sort=page_layout) - lots of free materials you can use in your project. That should speed up things a lot!

### For Track Makers
[Building Tools](https://ranjian0.github.io/building_tools/) - an addon that allows quick creation of buildings using basic shapes and thousands of options to create unique assets.

## Further Reading
[Blender Application Templates in the Blender Manual](https://docs.blender.org/manual/en/latest/advanced/app_templates.html)
