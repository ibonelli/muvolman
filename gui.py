from simple_menu import cMenu
from gui_mc import guiMc
from gui_vol import guiVolumes

menu = cMenu()
menu.add_menu_entry("1. Crear un volumen","cvol")
menu.add_menu_entry("2. Ver un volumen","svol")
menu.add_menu_entry("3. Salir","exit")
cmd = menu.show()
menu.cleanup()

if(cmd=="cvol"):
  svol = guiVolumes()
  svol.show()
  svol.cleanup()
elif(cmd=="svol"):
  mgm = guiMc()
  mgm.show()
  mgm.cleanup()
