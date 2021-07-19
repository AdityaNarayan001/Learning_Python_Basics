#we have two method to import
#one is to import full module and other is to import a function from module

import module_to_import_to_modules  #importing full module
from module_to_import_to_modules import kg_to_lbs #importing a function from a module

print(module_to_import_to_modules.kg_to_lbs(70)) #calling module then calling its function

print(kg_to_lbs(70)) #here we are directly calling the function