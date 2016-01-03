from simple_menu import cMenu

menu = cMenu()
menu.add_menu_entry("1. Opcion1","cmd1")
menu.add_menu_entry("2. Opcion2","cmd2")
menu.add_menu_entry("3. Opcion3","cmd3")
cmd = menu.show()
menu.cleanup()
print cmd
