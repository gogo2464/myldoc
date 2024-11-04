import os
import sys
import lief

mfc = lief.parse(sys.argv[1])
zap = lief.parse(sys.argv[2])

cmd = zap

mfc_rsrc_manager = mfc.resources_manager
cmd_rsrc_manager = cmd.resources_manager

mfc_icons = mfc_rsrc_manager.icons
cmd_icons = cmd_rsrc_manager.icons

mfc_rsrc_manager.change_icon(mfc_icons[0], cmd_icons[0])


builder = lief.PE.Builder(mfc)
builder.build_resources(True)
builder.build()

print("patched!")
builder.write("out.exe")